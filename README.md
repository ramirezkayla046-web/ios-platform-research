# iOS Platform Security Research

Independent security research into the iOS device communication stack, service namespace, and USB protocol surface.

**Researcher:** Javier Martinez ([@ramirezkayla046-web](https://github.com/ramirezkayla046-web))  
**Platform:** Arch Linux · pymobiledevice3 · libimobiledevice ecosystem  

---

## Key Finding: Frozen Lockdownd Attack Surface

> **Apple's lockdownd-accessible service surface for a paired host has remained identical across iOS 18.7.2 and iOS 26.4 beta — exactly 10 services, unchanged across two major chip generations.**

This was determined by running `iosctl probe-all` against two devices simultaneously:

| Device | Chip | iOS Version | Build | Services Reachable |
|---|---|---|---|---|
| iPhone XS Max (iPhone11,6) | A12 Bionic | 18.7.2 | 22H124 | **10 / 285** |
| iPhone 17 Pro (iPhone18,2) | A19 Pro | 26.4 (beta) | 23E5234a | **10 / 285** |

### The 10 Reachable Services (Both Devices, Over Paired USB)

| Service | Category | Notes |
|---|---|---|
| `com.apple.afc` | File Access | `/var/mobile/Media` read/write |
| `com.apple.amfi.lockdown` | Security | AMFI — Developer Mode enable/query |
| `com.apple.bluetooth.BTPacketLogger` | Bluetooth | BT packet capture stream |
| `com.apple.companion_proxy` | Watch | Apple Watch communication channel |
| `com.apple.internal.devicecompute.CoreDeviceProxy` | CoreDevice | Internal CoreDevice proxy — present on both |
| `com.apple.mobile.diagnostics_relay` | Diagnostics | Device diagnostics, reboot, MobileGestalt |
| `com.apple.mobile.heartbeat` | Transport | Keepalive / connection maintenance |
| `com.apple.mobile.insecure_notification_proxy` | Notifications | Darwin notifications — **no auth required** |
| `com.apple.mobile.notification_proxy` | Notifications | Darwin notifications |
| `com.apple.mobileactivationd` | Activation | iCloud activation daemon |

### Notable Observations

**`com.apple.mobile.insecure_notification_proxy`** accepts connections without additional authentication beyond pairing. This service allows posting and observing Darwin notifications on the device — a potential vector for triggering device-side behavior from a paired host.

**`com.apple.internal.devicecompute.CoreDeviceProxy`** is marked internal but responds on both retail iOS 18.7.2 and iOS 26.4 beta. Its presence on non-developer builds is undocumented.

**`com.apple.bluetooth.BTPacketLogger`** being in the reachable set means a paired host can capture Bluetooth traffic without Developer Mode enabled.

**275 of 285 probed services** returned `InvalidService` on both devices — consistent with Apple's migration of developer and diagnostic services to the RemoteXPC/RSD tunnel (introduced iOS 17) rather than direct lockdownd access.

### Services With Non-Standard Failure Modes

Two services returned errors distinct from `InvalidService`:

| Service | Error | Interpretation |
|---|---|---|
| `com.apple.accessibility.axAuditDaemon.remoteserver` | `{'MessageType': 'Result', 'Number': 3}` | Service exists, active, but rejected with error code 3 — entitlement or trust level mismatch |
| `com.apple.iosdiagnostics.relay` | Non-standard error | Service present but access controlled |

These are candidates for further investigation — they respond differently from the 273 `InvalidService` returns, indicating they exist on the lockdownd surface but enforce additional access controls.

---

## Methodology

### Tool: iosctl

Custom Python CLI built on pymobiledevice3 for automated iOS device recon and service probing.

```
~/apple/research/iosctl/
├── main.py                  — CLI entrypoint
├── commands/
│   ├── scan.py              — device detection and info
│   ├── services.py          — lockdown service enumeration
│   └── probe_all.py         — full service surface probe
├── services.json            — 285-entry service corpus (partial of 1,408 total)
└── logs/                    — timestamped probe reports (JSON + txt)
```

### Probe Methodology

For each service identifier in the corpus, `probe_all` attempts to open a raw lockdown service connection via `pymobiledevice3`'s `start_lockdown_service()` API. Failures are fingerprinted by exception type and message:

| Status | Condition |
|---|---|
| `SUCCESS` | Service connection accepted |
| `NOT_FOUND` | `InvalidServiceError` — lockdownd does not recognize identifier |
| `DENIED` | Service exists but access refused (entitlement missing) |
| `REQUIRES_TUNNEL` | iOS 17+ RSD/CoreDevice service, won't answer on lockdownd |
| `UNPAIRED` | Device trust not established |
| `TIMEOUT` | No response within 8 seconds |
| `FAIL` | Non-standard error response |

### Service Corpus

The probe corpus is a subset of a larger 1,408-entry `com.apple.*` service namespace enumerated via:
- Live lockdown service enumeration over USB
- Source analysis of `pymobiledevice3`, `libimobiledevice`, and related toolchain repos
- Correlation with lockdown key corpus and environment trigger datasets

Full corpus documentation: [`ios-services.md`](ios-services.md)

---

## Probe Results

Raw JSON and human-readable reports for each probe run:

| File | Device | iOS | Result |
|---|---|---|---|
| [`probe_a12_ios18.7.2.json`](probe-results/probe_a12_ios18.7.2.json) | iPhone XS Max (A12) | 18.7.2 | 10 SUCCESS / 285 |
| [`probe_a19_ios26.4b.json`](probe-results/probe_a19_ios26.4b.json) | iPhone 17 Pro (A19) | 26.4 beta | 10 SUCCESS / 285 |

Diff script: [`probe-results/diff.py`](probe-results/diff.py)

Run your own diff:
```bash
python3 probe-results/diff.py \
    probe-results/probe_a12_ios18.7.2.json \
    probe-results/probe_a19_ios26.4b.json
```

---

## Related Research

| Document | Description |
|---|---|
| [`ios-services.md`](ios-services.md) | 1,408 `com.apple.*` service identifier reference |
| [`usb-tunnel-stack.md`](usb-tunnel-stack.md) | USB transport stack capability matrix |
| [`libimobiledevice-tools.md`](libimobiledevice-tools.md) | libimobiledevice v1.4.0 full tool reference |
| [`pymobiledevice3-cli.md`](pymobiledevice3-cli.md) | pymobiledevice3 complete CLI surface |

---

## Environment

```
Host OS   : Arch Linux (kernel 6.19.8-arch1-1)
Python    : 3.14 (venvs/pmd3)
Tools     : pymobiledevice3 (latest), libimobiledevice 1.4.0
Transport : USB via usbmuxd 1.1.1
```

---

## Responsible Disclosure

This research was conducted on personally owned devices. No vulnerabilities have been exploited. Service reachability data reflects normal paired-host access as documented by Apple's developer tooling. Findings are shared for educational and security research purposes.

---

*Research ongoing. Contributions and device data from other iOS versions welcome via issues or PRs.*
