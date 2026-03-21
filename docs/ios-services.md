# iOS Service Namespace Reference

> Enumerated `com.apple.*` service identifiers from live device inspection and source-level analysis.  
> Total: **1,408 unique service identifiers** across the iOS platform service namespace.

---

## How This Was Generated

Services were extracted via a combination of:
- Live lockdown service enumeration over USB using `pymobiledevice3` and `libimobiledevice`
- Source analysis of `pymobiledevice3`, `libimobiledevice`, and related toolchain repos
- Correlation with `lockdown_keys`, `env_triggers`, and `ios_services` extracted data sets

---

## Service Categories

### Accessibility (`com.apple.accessibility.*`)

| Service Identifier | Notes |
|---|---|
| `com.apple.accessibility.Accessibility` | Core accessibility daemon |
| `com.apple.accessibility.AccessibilityUIServer` | UI server for accessibility features |
| `com.apple.accessibility.AccessibilityUIServer.xpc` | XPC endpoint |
| `com.apple.accessibility.axAuditDaemon.remoteserver` | Accessibility audit daemon remote server |
| `com.apple.accessibility.axAuditDaemon.remoteserver.shim.remote` | Shim/tunnel variant |
| `com.apple.accessibility.cache.darken.system.colors.enabled` | Cached pref: darken system colors |
| `com.apple.accessibility.cache.differentiate.without.color` | Cached pref: differentiate without color |
| `com.apple.accessibility.cache.enhance.background.contrast` | Cached pref: enhance contrast |
| `com.apple.accessibility.cache.enhance.text.legibility` | Cached pref: text legibility |
| `com.apple.accessibility.cache.invert.colors` | Cached pref: invert colors |
| `com.apple.accessibility.cache.prefers.horizontal.text` | Cached pref: horizontal text |
| `com.apple.accessibility.cache.reduce.motion` | Cached pref: reduce motion |
| `com.apple.accessibility.classic.wob.status` | White-on-black status |
| `com.apple.accessibility.commandandcontrol.status` | Command & Control status |
| `com.apple.accessibility.mediaaccessibilityd` | Media accessibility daemon |
| `com.apple.accessibility.mediaaccessibilityd.xpc` | XPC endpoint |
| `com.apple.accessibility.voiceovertouch.status` | VoiceOver status |
| `com.apple.accessibility.zoomtouch.status` | Zoom status |

---

### AFC — Apple File Conduit (`com.apple.afc*`)

| Service Identifier | Notes |
|---|---|
| `com.apple.afc` | **Primary AFC service** — `/var/mobile/Media` access |
| `com.apple.afc2` | AFC2 — root filesystem access (requires jailbreak entitlement) |
| `com.apple.afc.shim.remote` | Remote/tunnel shim variant |

---

### AMFI — Apple Mobile File Integrity (`com.apple.amfi.*`)

| Service Identifier | Notes |
|---|---|
| `com.apple.amfi.lockdown` | AMFI lockdown interface — Developer Mode enable/query |
| `com.apple.amfi.lockdown.shim.remote` | Shim/tunnel variant |

---

### AirTunes / DACP (`com.apple.AirTunes.DACP.*`)

| Service Identifier | Notes |
|---|---|
| `com.apple.AirTunes.DACP.device-prevent-playback` | Prevent playback notification |
| `com.apple.AirTunes.DACP.devicevolume` | Device volume |
| `com.apple.AirTunes.DACP.devicevolumechanged` | Volume change notification |
| `com.apple.AirTunes.DACP.mutetoggle` | Mute toggle |
| `com.apple.AirTunes.DACP.nextitem` | Next track |
| `com.apple.AirTunes.DACP.pause` | Pause |
| `com.apple.AirTunes.DACP.play` | Play |
| `com.apple.AirTunes.DACP.previtem` | Previous track |
| `com.apple.AirTunes.DACP.repeatadv` | Repeat advanced |
| `com.apple.AirTunes.DACP.shuffletoggle` | Shuffle toggle |
| `com.apple.AirTunes.DACP.volumedown` | Volume down |
| `com.apple.AirTunes.DACP.volumeup` | Volume up |

---

### CoreDevice (`com.apple.coredevice.*`)

The CoreDevice stack is the modern (iOS 17+) replacement for many legacy lockdown services.

| Service Identifier | Notes |
|---|---|
| `com.apple.coredevice.appservice` | App management service |
| `com.apple.coredevice.deviceinfo` | Device info query |
| `com.apple.coredevice.diagnosticsservice` | Diagnostics |
| `com.apple.coredevice.feature.capturesysdiagnose` | Capture sysdiagnose |
| `com.apple.coredevice.feature.debugserverproxy` | Debug server proxy |
| `com.apple.coredevice.feature.fetchappicons` | Fetch app icons |
| `com.apple.coredevice.feature.getdeviceinfo` | Get device info |
| `com.apple.coredevice.feature.getdisplayinfo` | Get display info |
| `com.apple.coredevice.feature.getlockstate` | Get lock state |
| `com.apple.coredevice.feature.installapp` | Install application |
| `com.apple.coredevice.feature.installroot` | Install root |
| `com.apple.coredevice.feature.launchapplication` | Launch application |
| `com.apple.coredevice.feature.listapps` | List installed apps |
| `com.apple.coredevice.feature.listprocesses` | List running processes |
| `com.apple.coredevice.feature.listroots` | List roots |
| `com.apple.coredevice.feature.monitorprocesstermination` | Monitor process termination |
| `com.apple.coredevice.feature.querymobilegestalt` | Query MobileGestalt |
| `com.apple.coredevice.feature.rebootdevice` | Reboot device |
| `com.apple.coredevice.feature.sendmemorywarningtoprocess` | Send memory warning |
| `com.apple.coredevice.feature.sendsignaltoprocess` | Send signal to process |
| `com.apple.coredevice.feature.spawnexecutable` | Spawn executable |
| `com.apple.coredevice.feature.transferFiles` | Transfer files |
| `com.apple.coredevice.feature.uninstallapp` | Uninstall application |
| `com.apple.coredevice.feature.uninstallroot` | Uninstall root |
| `com.apple.coredevice.fileservice.control` | File service control channel |
| `com.apple.coredevice.fileservice.data` | File service data channel |
| `com.apple.coredevice.openstdiosocket` | Open stdio socket |

---

### Debug / Developer Tools (`com.apple.debugserver*`, `com.apple.dt.*`, `com.apple.instruments.*`)

| Service Identifier | Notes |
|---|---|
| `com.apple.debugserver` | LLDB debug server |
| `com.apple.debugserver.DVTSecureSocketProxy` | Secure debug proxy (Xcode) |
| `com.apple.debugserver.DVTSecureSocketProxy.applist` | App list for debug proxy |
| `com.apple.dt.coredevice.tunnelservice.client` | CoreDevice tunnel client (iOS 17+) |
| `com.apple.dt.devicearbitration` | Device arbitration |
| `com.apple.dt.remotepairing` | Remote pairing |
| `com.apple.dt.remotepairingdeviced.lockdown.shim.remote` | Remote pairing shim |
| `com.apple.instruments.remoteserver.DVTSecureSocketProxy` | Instruments remote server |
| `com.apple.instruments.server.services.device.applictionListing` | App listing |
| `com.apple.instruments.server.services.deviceinfo` | Device info via instruments |
| `com.apple.instruments.server.services.device.xpccontrol` | XPC control |
| `com.apple.instruments.server.services.filetransfer.debuginbox` | Debug inbox file transfer |
| `com.apple.internal.dt.coredevice.untrusted.tunnelservice` | Untrusted tunnel service |
| `com.apple.internal.dt.remote.debugproxy` | Internal remote debug proxy |

---

### Lockdown (`com.apple.mobile.lockdown*`)

| Service Identifier | Notes |
|---|---|
| `com.apple.mobile.lockdown` | **Core lockdown service** |
| `com.apple.mobile.lockdownd` | Lockdown daemon |
| `com.apple.mobile.lockdown_cache` | Lockdown cache |
| `com.apple.mobile.lockdown.activation_state` | Activation state notification |
| `com.apple.mobile.lockdown.BonjourPairingServiceChanged` | Bonjour pairing change |
| `com.apple.mobile.lockdown.BonjourServiceChanged` | Bonjour service change |
| `com.apple.mobile.lockdown.brick_state` | Brick state notification |
| `com.apple.mobile.lockdown.device_name_changed` | Device name change |
| `com.apple.mobile.lockdown.disk_usage_changed` | Disk usage change |
| `com.apple.mobile.lockdown.host_attached` | Host attach event |
| `com.apple.mobile.lockdown.host_detached` | Host detach event |
| `com.apple.mobile.lockdown.host_paired` | Host pairing event |

---

### Mobile Core Services (`com.apple.mobile.*`)

| Service Identifier | Notes |
|---|---|
| `com.apple.mobile.backup` | MobileBackup |
| `com.apple.mobile.debug` | Debug interface |
| `com.apple.mobile.diagnostics_relay` | Diagnostics relay |
| `com.apple.mobile.heartbeat` | Keep-alive heartbeat |
| `com.apple.mobile.insecure_notification_proxy` | Insecure notification proxy |
| `com.apple.mobile.internal` | Internal interface |
| `com.apple.mobile.iTunes` | iTunes sync service |
| `com.apple.iTunes` | iTunes (top-level) |
| `com.apple.disk_usage` | Disk usage query |

---

### Find My / iCloud (`com.apple.icloud.*`)

| Service Identifier | Notes |
|---|---|
| `com.apple.icloud.findmydeviced.findkit.magSafe.added` | MagSafe accessory added |
| `com.apple.icloud.findmydeviced.findkit.magSafe.attach` | MagSafe attach |
| `com.apple.icloud.findmydeviced.findkit.magSafe.detach` | MagSafe detach |
| `com.apple.icloud.findmydeviced.findkit.magSafe.removed` | MagSafe removed |
| `com.apple.icloud.findmydeviced.localActivationLockInfoChanged` | Activation lock change |

---

### Device Management (`com.apple.devicemanagementclient.*`, `com.apple.configurator.*`)

| Service Identifier | Notes |
|---|---|
| `com.apple.devicemanagementclient.devicePostureChanged` | Device posture change (MDM) |
| `com.apple.devicemanagementclient.longLivedTokenChanged` | Long-lived token change |
| `com.apple.configurator.usbrestrictedmode` | USB restricted mode (configurator) |
| `com.apple.mobileactivationd` | Mobile activation daemon |
| `com.apple.mobileactivationd.shim.remote` | Activation daemon shim |

---

### iOS Diagnostics / Logging

| Service Identifier | Notes |
|---|---|
| `com.apple.iosdiagnostics.relay` | iOS diagnostics relay |
| `com.apple.mobile.syslog_relay` | Syslog relay (used by `idevicesyslog`) |

---

### Internal / Compute (`com.apple.internal.*`)

| Service Identifier | Notes |
|---|---|
| `com.apple.internal.devicecompute.CoreDeviceProxy` | CoreDevice proxy (internal) |
| `com.apple.internal.devicecompute.CoreDeviceProxy.shim.remote` | Shim variant |

---

## Notes on `.shim.remote` Variants

Many services have a `*.shim.remote` counterpart. These are tunnel/proxy variants used when the device is connected over a network tunnel (RemoteXPC / RSD) rather than direct USB. They became prominent in iOS 17 with the introduction of `tunneld` and CoreDevice's new transport layer.

## Notes on `.xpc` Variants

Services ending in `.xpc` are XPC endpoint identifiers used for inter-process communication on-device. They appear in lockdown enumeration but are not directly invokable over the host-device protocol — they represent the daemon's internal IPC surface.
