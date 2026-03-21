# iOS Platform Security Research

> Deep enumeration of the iOS device communication stack — lockdown services, usbmuxd transport, AFC, pymobiledevice3 CLI surface, and the full `com.apple.*` service namespace.

---

## What This Is

This repository documents the results of systematically mapping the iOS device interface layer from the ground up — using source-level analysis of the open-source toolchain (`libimobiledevice`, `pymobiledevice3`, `libusbmuxd`, `go-ios`, `idevicerestore`) combined with live device enumeration.

The goal: produce a complete, accurate reference for engineers working in mobile security, MDM, device forensics, or iOS automation.

---

## Repository Structure

```
ios-platform-research/
├── README.md                        ← You are here
├── docs/
│   ├── ios-services.md              ← Full com.apple.* service namespace (1,400+ entries)
│   ├── libimobiledevice-tools.md    ← All idevice* tools, flags, versions
│   ├── usb-tunnel-stack.md          ← USB/tunnel transport capability analysis
│   └── pymobiledevice3-cli.md       ← Complete CLI surface of pymobiledevice3
├── data/
│   ├── services.json                ← Machine-readable service list
│   └── tools.json                   ← Tool inventory with versions
└── iosctl/
    ├── main.py                      ← CLI entrypoint
    └── commands/
        ├── scan.py                  ← Device scan
        ├── services.py              ← Service enumeration
        └── probe_all.py             ← Full probe runner
```

---

## Key Findings

### Service Namespace Coverage
- **1,408 unique `com.apple.*` service identifiers** enumerated from live device + source analysis
- Covers: accessibility, AFC, AMFI, AirTunes DACP, backup, CoreDevice, debugserver, diagnostics, lockdown, instruments, usbmux, and more
- Includes services not documented in Apple's public developer documentation

### Lockdown Layer
- Full lockdown key corpus extracted from restore ops and device communication logs
- Covers pairing state, activation state, brick state, host attach/detach, disk usage, and device name change notifications

### USB Transport Stack
- Mapped capability differences across: `libusbmuxd`, `netmuxd`, `go-ios`, `raw-gadget`, `libimobiledevice`, `idevicerestore`
- Identified `iproxy`-based TCP forwarding, utun interface tunneling, and recovery/DFU-mode USB access paths

### pymobiledevice3 CLI Surface
- 20 top-level command groups documented with subcommands and flags
- Covers: activation, AFC, AMFI, apps, backup2, crash, developer, diagnostics, lockdown, mounter, notification, pcap, processes, profile, provision, remote, restore, springboard, syslog, usbmux

---

## Toolchain Versions Mapped

| Tool | Version |
|---|---|
| libimobiledevice | 1.4.0 / 1.4.0-6-gc4f1118 |
| idevicerestore | 1.0.0-270-g405fcd1 |
| libirecovery | 1.3.1 |
| libtatsu | 1.0.5-3-g60a39f3 |
| ideviceinstaller | 1.2.0 |
| irecovery | 1.1.0 / 1.0.1 |
| pymobiledevice3 | Python 3.14 venv |

---

## iosctl — Custom Enumeration Tool

`iosctl` is a thin Python CLI built on top of pymobiledevice3 for scripted device recon:

```bash
python3 iosctl/main.py scan        # Detect and identify connected devices
python3 iosctl/main.py services    # Enumerate accessible lockdown services
python3 iosctl/main.py probe-all   # Run full service probe across all endpoints
```

---

## Use Cases

This reference is useful for engineers working on:

- **MDM / Enterprise Mobility** — understanding the full service surface available to management profiles
- **Mobile Security Research** — mapping attack surface and trust boundaries on iOS
- **Device Forensics / DFIR** — knowing which services expose what data over USB
- **iOS Automation / Tooling** — building reliable tooling on top of the lockdown/usbmux layer

---

## Related Projects

- [pymobiledevice3](https://github.com/doronz88/pymobiledevice3) — Python iOS device interface library
- [libimobiledevice](https://libimobiledevice.org) — C library for iOS device communication
- [go-ios](https://github.com/danielpaulus/go-ios) — Go implementation of iOS device protocol

---

## Author

Security researcher focused on the iOS platform communication stack. Available for full-time roles in mobile security, MDM infrastructure, and iOS tooling.

📍 San Francisco Bay Area  
🔗 [LinkedIn](#) · [GitHub](#)
