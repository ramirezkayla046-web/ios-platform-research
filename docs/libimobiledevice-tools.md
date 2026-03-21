# libimobiledevice Tool Reference

> Complete tool inventory for `libimobiledevice` v1.4.0 / v1.4.0-6-gc4f1118.  
> All tools confirmed present in build at `/opt/limd-debug/` and `/opt/limd-puredebug/`.

---

## Build Variants

Two build configurations were mapped:

| Path | Version | Notes |
|---|---|---|
| `/opt/limd-debug/` | `1.4.0` | Standard debug build |
| `/opt/limd-puredebug/` | `1.4.0-6-gc4f1118` | Pure debug build (6 commits ahead of 1.4.0 tag) |

Both builds include identical tool sets. The `-puredebug` variant contains additional debug symbols and logging.

---

## Tool Reference

### `idevice_id`
List connected iOS device UDIDs, or check if a specific device is connected.

```bash
idevice_id -l                    # List all connected device UDIDs
idevice_id -n                    # List devices with network (WiFi) connection
```

**Man page:** `idevice_id.1`

---

### `ideviceinfo`
Query lockdown values from a connected iOS device.

```bash
ideviceinfo                      # Dump all lockdown values
ideviceinfo -k DeviceName        # Query specific key
ideviceinfo -d -u <UDID>         # Target specific device
ideviceinfo -x                   # Output as XML plist
ideviceinfo -q com.apple.mobile.backup  # Query specific domain
```

**Man page:** `ideviceinfo.1`  
**Key domains:** `com.apple.mobile.backup`, `com.apple.xcode.developerdomain`, `com.apple.fairplay`

---

### `idevicepair`
Manage pairing relationships between host and iOS device.

```bash
idevicepair pair                 # Pair with connected device
idevicepair unpair               # Remove pairing
idevicepair validate             # Validate existing pairing
idevicepair list                 # List all paired devices
idevicepair systembuid           # Get system BUID
```

**Man page:** `idevicepair.1`

---

### `idevicesyslog`
Stream syslog output from the connected iOS device.

```bash
idevicesyslog                    # Stream all syslog
idevicesyslog -m "keyword"       # Filter by keyword match
idevicesyslog -e "pattern"       # Exclude matching lines
idevicesyslog -d                 # Include debug messages
idevicesyslog -k "process"       # Filter by process name
```

**Version:** `idevicesyslog 1.4.0-6-gc4f1118`  
**Man page:** `idevicesyslog.1`  
**Related service:** `com.apple.mobile.syslog_relay`

---

### `idevicebackup`
Create and restore iOS backups (legacy MobileBackup protocol).

```bash
idevicebackup backup <dir>       # Create backup to directory
idevicebackup restore <dir>      # Restore from directory
```

**Version:** `idevicebackup 1.4.0`  
**Man page:** `idevicebackup.1`  
**Note:** Superseded by `idevicebackup2` for modern devices.

---

### `idevicebackup2`
Create, inspect, and restore iOS backups (MobileBackup2 protocol).

```bash
idevicebackup2 backup --full -u <UDID> <dir>   # Full backup
idevicebackup2 restore --system <dir>           # Restore with system files
idevicebackup2 info <dir>                       # Show backup info
idevicebackup2 list <dir>                       # List backup contents
idevicebackup2 unback <dir>                     # Unpack backup to filesystem
idevicebackup2 encryption on <password>         # Enable backup encryption
idevicebackup2 changepw <old> <new>             # Change backup password
```

**Version:** `idevicebackup2 1.4.0`  
**Man page:** `idevicebackup2.1`  
**Related service:** `com.apple.mobile.backup`

---

### `idevicecrashreport`
Pull crash reports from the device.

```bash
idevicecrashreport <dir>         # Pull all crash reports to directory
idevicecrashreport -k <dir>      # Keep crash reports on device after pull
idevicecrashreport -e <dir>      # Extract crash reports
```

**Version:** `idevicecrashreport 1.4.0`  
**Man page:** `idevicecrashreport.1`

---

### `idevicescreenshot`
Capture a screenshot from the connected iOS device.

```bash
idevicescreenshot                # Save screenshot to current directory
idevicescreenshot image.png      # Save to specified file
```

**Version:** `idevicescreenshot 1.4.0`  
**Man page:** `idevicescreenshot.1`

---

### `idevicename`
Get or set the device name.

```bash
idevicename                      # Get current device name
idevicename "My iPhone"          # Set device name
```

**Version:** `idevicename 1.4.0`  
**Man page:** `idevicename.1`

---

### `idevicedate`
Get or set the device date/time.

```bash
idevicedate                      # Get current device time
idevicedate -s                   # Sync device time to host time
idevicedate --set "2025-01-01"   # Set specific date
```

**Version:** `idevicedate 1.4.0`  
**Man page:** `idevicedate.1`

---

### `idevicedebug`
Attach a debugger to a running process on the device.

```bash
idevicedebug run <app_id>        # Launch and debug app by bundle ID
```

**Version:** `idevicedebug 1.4.0`  
**Man page:** `idevicedebug.1`  
**Requires:** DeveloperDiskImage mounted

---

### `idevicedebugserverproxy`
Proxy `debugserver` connections from the device to a local port for use with LLDB.

```bash
idevicedebugserverproxy <port>   # Forward debug server to local port
```

**Version:** `idevicedebugserverproxy 1.4.0`  
**Man page:** `idevicedebugserverproxy.1`  
**Related service:** `com.apple.debugserver.DVTSecureSocketProxy`

---

### `idevicediagnostics`
Access device diagnostics — reboot, sleep, shutdown, ioregistry.

```bash
idevicediagnostics restart       # Restart device
idevicediagnostics shutdown      # Shut down device
idevicediagnostics sleep         # Put device to sleep
idevicediagnostics diagnostics All          # Dump all diagnostic info
idevicediagnostics mobilegestalt <key>      # Query MobileGestalt
idevicediagnostics ioregistry <plane>       # Dump IORegistry
```

**Version:** `idevicediagnostics 1.4.0`  
**Man page:** `idevicediagnostics.1`  
**Related service:** `com.apple.mobile.diagnostics_relay`

---

### `ideviceenterrecovery`
Put a connected iOS device into Recovery mode.

```bash
ideviceenterrecovery             # Enter recovery mode
ideviceenterrecovery -u <UDID>   # Target specific device
```

**Version:** `ideviceenterrecovery 1.4.0`  
**Man page:** `ideviceenterrecovery.1`

---

### `ideviceimagemounter`
Mount or unmount a DeveloperDiskImage on the device.

```bash
ideviceimagemounter <image> <signature>     # Mount image
ideviceimagemounter -l                      # List mounted images
ideviceimagemounter -u <mount_path>         # Unmount image
```

**Version:** `ideviceimagemounter 1.4.0`  
**Man page:** `ideviceimagemounter.1`  
**Note:** Required before using developer tools on iOS < 17.

---

### `ideviceinstaller`
Install, uninstall, and list apps on the device.

```bash
ideviceinstaller -i app.ipa      # Install IPA
ideviceinstaller -U <bundle_id>  # Uninstall by bundle ID
ideviceinstaller -l              # List installed apps
ideviceinstaller -l -o list.plist  # Save app list as plist
```

**Version:** `ideviceinstaller 1.2.0`  
**Man page:** `ideviceinstaller.1`

---

### `idevicenotificationproxy`
Post or observe Darwin notifications via the notification proxy.

```bash
idevicenotificationproxy -o <notification>   # Observe notification
idevicenotificationproxy -p <notification>   # Post notification
```

**Version:** `idevicenotificationproxy 1.4.0`  
**Man page:** `idevicenotificationproxy.1`  
**Related services:** `com.apple.mobile.notification_proxy`, `com.apple.mobile.insecure_notification_proxy`

---

### `ideviceprovision`
Manage provisioning profiles on the device.

```bash
ideviceprovision list            # List installed profiles
ideviceprovision copy <uuid> <output.mobileprovision>  # Export profile
ideviceprovision install <file.mobileprovision>         # Install profile
ideviceprovision remove <uuid>   # Remove profile
```

**Version:** `ideviceprovision 1.4.0`  
**Man page:** `ideviceprovision.1`

---

### `idevicesetlocation`
Spoof GPS location on the device (requires DeveloperDiskImage).

```bash
idevicesetlocation <lat> <lon>   # Set location
idevicesetlocation reset         # Reset to real location
```

**Version:** `idevicesetlocation 1.4.0`  
**Man page:** `idevicesetlocation.1`

---

### `idevicedevmodectl`
Toggle Developer Mode on/off (iOS 16+).

```bash
idevicedevmodectl status         # Query Developer Mode state
idevicedevmodectl enable         # Enable Developer Mode
```

**Version:** `idevicedevmodectl 1.4.0`  
**Man page:** `idevicedevmodectl.1`  
**Related service:** `com.apple.amfi.lockdown`

---

### `idevicebtlogger`
Capture Bluetooth logs from the device.

```bash
idevicebtlogger <output.pklg>    # Capture BT log to PacketLogger format
```

**Version:** `idevicebtlogger 1.4.0`  
**Man page:** `idevicebtlogger.1`

---

### `idevicerestore`
Restore or erase a device using an IPSW firmware file.

```bash
idevicerestore -t <file.ipsw>    # Restore with IPSW
idevicerestore -e <file.ipsw>    # Erase and restore
idevicerestore -l                # Latest firmware URL lookup
idevicerestore -d                # Enable debug output
```

**Version:** `idevicerestore 1.0.0-270-g405fcd1`  
**Depends on:** `libirecovery 1.3.1`, `libtatsu 1.0.5-3-g60a39f3`  
**Man page:** `idevicerestore.1`

---

### `irecovery`
Direct Recovery/DFU mode shell for low-level device access.

```bash
irecovery -s                     # Open recovery shell
irecovery -c "setenv auto-boot true"  # Send iBoot command
irecovery -f <file>              # Send file to device
irecovery -r                     # Reboot device
```

**Versions:** `irecovery 1.1.0` (SSHRD tooling), `irecovery 1.0.1` (ramdisk tooling)
