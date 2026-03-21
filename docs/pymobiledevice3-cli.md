# pymobiledevice3 CLI Reference

> Complete command surface of `pymobiledevice3` — the Python Swiss-army CLI for iOS device interaction.  
> Mapped from source and live `--help` enumeration. Python 3.14 / venv install.

---

## Global Options

| Flag | Short | Type | Description |
|---|---|---|---|
| `--reconnect` | | bool | Auto-reconnect if device disconnects mid-command |
| `--verbose` | `-v` | int | Increase logging verbosity (repeatable) |
| `--color` / `--no-color` | | bool | Colorize output (default: on) |
| `--install-completion` | | | Install shell completion |
| `--show-completion` | | | Print shell completion script |
| `--help` | `-h` | | Show help and exit |

---

## Command Groups

### `activation`
Perform iCloud activation/deactivation or query the current state.

```bash
python3 -m pymobiledevice3 activation --help
```

Key operations: activate, deactivate, query activation state.

---

### `afc`
Browse, push, and pull files via the AFC service (`/var/mobile/Media`).

```bash
python3 -m pymobiledevice3 afc --help
```

Key operations: ls, pull, push, rm, mkdir, stat. Operates over `com.apple.afc` lockdown service.

---

### `amfi`
Enable Developer Mode or query its current state.

```bash
python3 -m pymobiledevice3 amfi --help
```

Related service: `com.apple.amfi.lockdown`, `com.apple.amfi.lockdown.shim.remote`

---

### `apps`
List, query, install, uninstall, and inspect apps on the device.

```bash
python3 -m pymobiledevice3 apps --help
```

Key operations: list, install, uninstall, lookup. Uses `com.apple.mobile.installation_proxy`.

---

### `backup2`
Create, inspect, and restore MobileBackup2 backups.

```bash
python3 -m pymobiledevice3 backup2 --help
```

Related service: `com.apple.mobile.backup`. Implements full MobileBackup2 protocol.

---

### `bonjour`
Browse devices over Bonjour (mDNS discovery).

```bash
python3 -m pymobiledevice3 bonjour --help
```

---

### `companion`
List paired companion devices (Apple Watch, etc.).

```bash
python3 -m pymobiledevice3 companion --help
```

---

### `crash`
Manage crash reports on the device.

```bash
python3 -m pymobiledevice3 crash --help
```

Key operations: list, pull, clear crash reports from device.

---

### `developer`
Developer tooling for iOS devices. Requires Developer Mode enabled and DeveloperDiskImage mounted.

```bash
python3 -m pymobiledevice3 developer --help
```

Key operations: shell, instrument, debug proxy, process listing, app launch.  
Related services: `com.apple.instruments.remoteserver.DVTSecureSocketProxy`, `com.apple.debugserver.DVTSecureSocketProxy`

---

### `diagnostics`
Reboot/shutdown device or access other diagnostics services.

```bash
python3 -m pymobiledevice3 diagnostics --help
```

Key operations: restart, shutdown, sleep, ioregistry, MobileGestalt queries.  
Related service: `com.apple.mobile.diagnostics_relay`

---

### `lockdown`
Pair/unpair device or access other lockdown services.

```bash
python3 -m pymobiledevice3 lockdown --help
```

Key operations: pair, unpair, get-value, set-value, start-service, browse.  
Core service: `com.apple.mobile.lockdown` / `com.apple.mobile.lockdownd`

---

### `mounter`
Mount/unmount DeveloperDiskImage or query related info.

```bash
python3 -m pymobiledevice3 mounter --help
```

Required before using `developer` commands on older iOS versions.

---

### `notification`
Post or observe Darwin notifications via `notification_proxy`.

```bash
python3 -m pymobiledevice3 notification --help
```

Related service: `com.apple.mobile.notification_proxy`, `com.apple.mobile.insecure_notification_proxy`

---

### `pcap`
Sniff device network traffic.

```bash
python3 -m pymobiledevice3 pcap --help
```

Captures packets from device interfaces. Output compatible with Wireshark/tcpdump.

---

### `power-assertion`
Create a power assertion to prevent device sleep.

```bash
python3 -m pymobiledevice3 power-assertion --help
```

---

### `processes`
View process list using the diagnosticsd API.

```bash
python3 -m pymobiledevice3 processes --help
```

Related service: `com.apple.mobile.diagnostics_relay`

---

### `profile`
Manage installed profiles or install SSL certificates.

```bash
python3 -m pymobiledevice3 profile --help
```

Key operations: list, install, remove profiles. Used in MDM enrollment flows.

---

### `provision`
Manage installed provisioning profiles.

```bash
python3 -m pymobiledevice3 provision --help
```

Related tool: `ideviceprovision`

---

### `remote`
Create and browse RemoteXPC tunnels (RSD/tunneld) for developer services.

```bash
python3 -m pymobiledevice3 remote --help
```

Related services: `com.apple.internal.dt.coredevice.untrusted.tunnelservice`, `com.apple.dt.coredevice.tunnelservice.client`  
This is the modern iOS 17+ tunnel mechanism replacing the older lockdown service proxy.

---

### `restore`
Restore/erase IPSWs, fetch blobs, and manage devices in Recovery/DFU.

```bash
python3 -m pymobiledevice3 restore --help
```

Wraps `idevicerestore` and related DFU/recovery operations.

---

### `springboard`
Interact with SpringBoard UI — icons, wallpapers, orientation, shell.

```bash
python3 -m pymobiledevice3 springboard --help
```

---

### `syslog`
Watch syslog messages from the device in real time.

```bash
python3 -m pymobiledevice3 syslog --help
```

Related service: `com.apple.mobile.syslog_relay`

---

### `usbmux`
Inspect usbmuxd-connected devices and forward TCP ports.

```bash
python3 -m pymobiledevice3 usbmux --help
```

Key operations: list devices, port-forward (iproxy equivalent).  
Transport: `com.apple.mobile.lockdown.host_attached` / usbmuxd socket

---

## Service → Command Mapping (Quick Reference)

| com.apple.* service | pymobiledevice3 command |
|---|---|
| `com.apple.afc` | `afc` |
| `com.apple.amfi.lockdown` | `amfi` |
| `com.apple.mobile.backup` | `backup2` |
| `com.apple.mobile.diagnostics_relay` | `diagnostics`, `processes` |
| `com.apple.mobile.lockdown` | `lockdown` |
| `com.apple.mobile.notification_proxy` | `notification` |
| `com.apple.debugserver.DVTSecureSocketProxy` | `developer` |
| `com.apple.instruments.remoteserver.DVTSecureSocketProxy` | `developer` |
| `com.apple.dt.coredevice.tunnelservice.client` | `remote` |
| `com.apple.mobile.installation_proxy` | `apps` |
