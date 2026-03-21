# USB & Tunnel Transport Stack Analysis

> Capability mapping across the iOS USB communication toolchain.  
> Covers: `libusbmuxd`, `netmuxd`, `go-ios`, `raw-gadget`, `libimobiledevice`, `idevicerestore`, `libirecovery`.

---

## Transport Architecture Overview

```
Host (Linux/macOS)
│
├── usbmuxd daemon  ←──────────────────────── manages USB device connections
│   └── libusbmuxd  ←──────────────────────── library interface to usbmuxd
│       └── iproxy  ←──────────────────────── TCP port forwarding over USB
│
├── libimobiledevice  ←─────────────────────── high-level device protocol layer
│   ├── lockdownd client  ←─────────────────── pairing, service start, key query
│   └── service clients (afc, backup, etc.)
│
├── pymobiledevice3  ←──────────────────────── Python implementation (no C dependency)
│   └── RemoteXPC / RSD tunnel  ←───────────── iOS 17+ network tunnel transport
│
└── go-ios  ←───────────────────────────────── standalone Go implementation
```

---

## Component Capability Matrix

| Capability | libusbmuxd | libimobiledevice | pymobiledevice3 | go-ios | idevicerestore |
|---|:---:|:---:|:---:|:---:|:---:|
| USB device detection | ✅ | ✅ | ✅ | ✅ | ✅ |
| TCP port forwarding (iproxy) | ✅ | ✅ | ✅ | ✅ | ❌ |
| Lockdown pairing | ❌ | ✅ | ✅ | ✅ | ❌ |
| Service enumeration | ❌ | ✅ | ✅ | ✅ | ❌ |
| AFC file transfer | ❌ | ✅ | ✅ | ✅ | ❌ |
| Backup (MobileBackup2) | ❌ | ✅ | ✅ | ✅ | ❌ |
| Syslog streaming | ❌ | ✅ | ✅ | ✅ | ❌ |
| App install/uninstall | ❌ | ✅ | ✅ | ✅ | ❌ |
| Recovery mode access | ❌ | partial | ✅ | partial | ✅ |
| DFU mode access | ❌ | ❌ | ✅ | ❌ | ✅ |
| IPSW restore | ❌ | ❌ | ✅ | ❌ | ✅ |
| RemoteXPC / RSD tunnel (iOS 17+) | ❌ | ❌ | ✅ | partial | ❌ |
| Network tunnel (utun interface) | ❌ | ❌ | ✅ | partial | ❌ |
| USB gadget emulation | ❌ | ❌ | ❌ | ❌ | ❌ |

`raw-gadget` (separate): USB gadget framework — can emulate USB devices at the kernel level. Not part of the standard iOS communication stack but relevant for USB attack surface research.

---

## Component Details

### libusbmuxd
**Role:** USB multiplexer daemon client library  
**Transport:** Direct usbmuxd socket (`/var/run/usbmuxd`)  
**Key capability:** `iproxy` — forwards a local TCP port to a port on the connected iOS device over USB. Foundation for all other tools.

```bash
# Port-forward device port 22 to localhost:2222
iproxy 2222 22
```

**Versions mapped:** Core library, no versioned binary.

---

### libimobiledevice
**Role:** High-level iOS device protocol implementation in C  
**Depends on:** libusbmuxd, libplist, libssl  
**Version:** 1.4.0 / 1.4.0-6-gc4f1118

**Tool inventory (all at v1.4.0):**

| Tool | Purpose |
|---|---|
| `idevice_id` | List connected device UDIDs |
| `ideviceinfo` | Query device lockdown values |
| `idevicepair` | Manage host-device pairing |
| `idevicesyslog` | Stream device syslog |
| `idevicebackup` / `idevicebackup2` | Create/restore backups |
| `idevicecrashreport` | Pull crash reports |
| `idevicescreenshot` | Capture device screenshot |
| `idevicename` | Get/set device name |
| `idevicedate` | Get/set device date |
| `idevicedebug` | Attach debugger |
| `idevicedebugserverproxy` | Proxy debug server connections |
| `idevicediagnostics` | Diagnostics relay |
| `ideviceenterrecovery` | Put device in recovery mode |
| `ideviceimagemounter` | Mount DeveloperDiskImage |
| `ideviceinstaller` | Install/uninstall IPAs |
| `idevicenotificationproxy` | Send/receive Darwin notifications |
| `ideviceprovision` | Manage provisioning profiles |
| `idevicesetlocation` | Spoof GPS location |
| `idevicedevmodectl` | Toggle Developer Mode |
| `idevicebtlogger` | Bluetooth log capture |

---

### pymobiledevice3
**Role:** Pure-Python iOS device protocol implementation  
**Advantage over libimobiledevice:** No C compilation required; supports iOS 17+ RemoteXPC/tunneld transport  
**Version:** Installed in Python 3.14 venv

Key differentiator: implements the **RSD (Remote Service Discovery) tunnel** protocol introduced in iOS 17, which replaced many direct lockdown service connections with an encrypted XPC tunnel over USB or Wi-Fi.

```bash
# Start a tunnel to the device (iOS 17+)
python3 -m pymobiledevice3 remote start-tunnel

# Connect developer services over the tunnel
python3 -m pymobiledevice3 developer --rsd <host> <port> shell
```

---

### go-ios
**Role:** Go implementation of the iOS device protocol  
**Advantage:** Single static binary, no runtime dependencies, good for CI/CD  
**Codebase:** Modern, actively maintained

---

### idevicerestore
**Role:** Full IPSW restore, Recovery mode, and DFU mode operations  
**Version:** 1.0.0-270-g405fcd1  
**Depends on:** libirecovery 1.3.1, libtatsu 1.0.5

**Capability breakdown:**

| Module | Purpose |
|---|---|
| `normal.c` | Normal mode restore operations |
| `recovery.c` | Recovery mode management |
| `dfu.c` | DFU mode management |
| `asr.c` | Apple Software Restore protocol |
| `img3.c` / `img4.c` | IMG3/IMG4 firmware image handling |
| `ipsw.c` | IPSW archive extraction |
| `download.c` | Firmware download |
| `fdr.c` | Factory Data Restore |
| `locking.c` | Device locking during restore |
| `limera1n.c` | limera1n exploit support (legacy) |
| `ftab.c` / `fls.c` / `mbn.c` | Baseband firmware formats |
| `ace3.c` | ACE3 chip operations |

---

### libirecovery
**Role:** Low-level USB communication for Recovery and DFU mode  
**Versions:** 1.1.0 (SSHRD tooling), 1.0.1 (ramdisk tooling), 1.3.1 (idevicerestore)  
**Tool:** `irecovery` — direct recovery/DFU mode shell

---

## iOS 17+ Transport Shift: RemoteXPC / RSD

Starting with iOS 17, Apple shifted developer services from direct lockdown service connections to an encrypted RemoteXPC tunnel:

1. Device creates a `tunneld` service over USB
2. Host connects via `com.apple.internal.dt.coredevice.untrusted.tunnelservice`
3. An encrypted XPC channel is established (RSD — Remote Service Discovery)
4. Developer services (debug server, instruments, etc.) are multiplexed over this tunnel

**Impact:** Tools that only implement the legacy lockdown protocol (libimobiledevice ≤ 1.4.0) cannot access developer services on iOS 17+ without the tunnel. `pymobiledevice3` and newer `go-ios` versions handle this correctly.

**Relevant services:**
- `com.apple.internal.dt.coredevice.untrusted.tunnelservice`
- `com.apple.dt.coredevice.tunnelservice.client`
- `com.apple.internal.devicecompute.CoreDeviceProxy`
- `com.apple.internal.devicecompute.CoreDeviceProxy.shim.remote`
