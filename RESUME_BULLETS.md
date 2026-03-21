# Resume Bullets — iOS Platform Security Engineer

> Copy-paste ready. Tailor to the specific job posting by leading with the most relevant bullets.

---

## Technical Skills Section

**iOS Platform & Mobile Security**
- Deep working knowledge of the iOS device communication stack: lockdown protocol, usbmuxd transport, AFC, MobileBackup2, RemoteXPC/RSD (iOS 17+)
- Hands-on experience with libimobiledevice, pymobiledevice3, go-ios, idevicerestore, libirecovery
- Enumerated 1,400+ `com.apple.*` service identifiers via live device inspection and source analysis
- Familiar with iOS trust model: pairing records, lockdown sessions, AMFI, Developer Mode, CoreDevice feature APIs
- Experience with iOS 17+ CoreDevice tunnel architecture (RSD, tunneld, RemoteXPC)

---

## Experience / Projects Section

**iOS Platform Security Research** *(Independent, 2025–2026)*
- Systematically mapped the full iOS device service namespace by combining source-level analysis of the libimobiledevice ecosystem with live device enumeration, producing a structured reference corpus of 1,408 `com.apple.*` service identifiers
- Built `iosctl`, a Python CLI tool wrapping pymobiledevice3 for automated device scanning, service enumeration, and endpoint probing — enabling repeatable recon workflows across multiple iOS targets
- Analyzed capability differences across USB transport implementations (libusbmuxd, libimobiledevice, pymobiledevice3, go-ios, idevicerestore) with particular focus on recovery/DFU mode access and iOS 17+ tunnel transport
- Documented the iOS 17+ RemoteXPC/RSD transport shift and its implications for tooling compatibility — mapping affected services and the new `CoreDevice` feature API surface
- Extracted and catalogued lockdown key corpus, environment triggers, and restore operation sequences from libimobiledevice and pymobiledevice3 source trees

---

## Targeting These Roles

### MDM / Enterprise Mobility (Jamf, Kandji, Mosyle, Addigy, Workspace ONE)
Lead with:
- lockdown protocol knowledge
- profile/provisioning management
- CoreDevice feature APIs (install app, list processes, reboot, etc.)
- iOS 17+ tunnel architecture impact on MDM tooling

### Mobile Security (Crowdstrike, SentinelOne, Lookout, Zimperium)
Lead with:
- service namespace enumeration and attack surface analysis
- AMFI, Developer Mode, trust boundary understanding
- syslog, crash report, diagnostics relay access
- pcap / traffic capture experience

### Device Forensics / DFIR (Cellebrite, Oxygen Forensics, MSAB, government/law enforcement contractors)
Lead with:
- AFC service access and file extraction
- MobileBackup2 protocol implementation knowledge
- lockdown pairing record lifecycle
- idevicerestore / DFU mode / irecovery familiarity

### iOS Tooling / Platform (Corellium, Apple, dev tool startups)
Lead with:
- pymobiledevice3 CLI surface depth
- instruments + debugserver proxy architecture
- DeveloperDiskImage mounting workflow
- iOS 17+ CoreDevice and RSD tunnel mechanics

---

## Keywords to Include (ATS optimization)

`iOS security` · `mobile device management` · `MDM` · `lockdown protocol` · `usbmuxd` · `libimobiledevice` · `pymobiledevice3` · `AFC` · `MobileBackup2` · `CoreDevice` · `RemoteXPC` · `DFU mode` · `idevicerestore` · `Python` · `reverse engineering` · `iOS internals` · `device forensics` · `AMFI` · `Developer Mode` · `USB transport` · `go-ios`
