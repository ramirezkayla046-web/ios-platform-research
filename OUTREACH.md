# LinkedIn Post + Outreach Templates

---

## LinkedIn Post

**Use this as-is or adjust the tone. Post it when the GitHub repo is live and link to it.**

---

I spent the last few months systematically mapping the iOS device communication stack from the ground up.

Not from docs — Apple doesn't have great docs for this. From source.

I pulled apart libimobiledevice, pymobiledevice3, go-ios, libusbmuxd, and idevicerestore, then cross-referenced everything against live device enumeration. The result:

→ 1,408 com.apple.* service identifiers catalogued and categorized
→ Full USB/tunnel transport capability matrix across 7 tools
→ Complete pymobiledevice3 CLI surface documented (20 command groups)
→ All libimobiledevice tools documented with flags, versions, and related services
→ A breakdown of the iOS 17+ RemoteXPC/RSD transport shift and what it breaks

I also built iosctl — a small Python CLI on top of pymobiledevice3 for automated device scanning, service enumeration, and bulk service probing.

Everything is on GitHub: [LINK]

I'm actively looking for full-time roles in mobile security, MDM infrastructure, or iOS platform engineering in the Bay Area. If you're working on iOS device management, mobile threat defense, or anything that touches the lockdown/usbmux layer — I'd love to talk.

#iOS #MobileSecurity #MDM #iOSSecurity #libimobiledevice #pymobiledevice3

---

## Cold Outreach Templates

### MDM Companies (Jamf, Kandji, Mosyle, Addigy)

**Subject:** iOS device stack engineer — lockdown/CoreDevice/RSD experience

Hi [Name],

I've been doing deep technical work on the iOS device communication layer — the lockdown protocol, usbmuxd transport, CoreDevice feature APIs, and the iOS 17+ RemoteXPC/RSD tunnel shift.

I recently published a full reference mapping 1,400+ com.apple.* service identifiers, a capability matrix across the open-source iOS toolchain, and a Python tool for automated service enumeration. [GitHub link]

I'm looking for a full-time role in the Bay Area and [Company] seems like a natural fit given how much of your product lives at this layer. Would you be open to a quick chat?

[Your name]

---

### Mobile Security Companies (Crowdstrike, SentinelOne, Lookout, Zimperium)

**Subject:** iOS platform security researcher — device surface mapping

Hi [Name],

I've been mapping the iOS device attack surface from the protocol layer up — specifically the lockdown service namespace, USB transport stack, AMFI/Developer Mode trust boundaries, and the diagnostic/instruments APIs.

I published the work here: [GitHub link] — 1,400+ service identifiers categorized, full tool capability matrix, and notes on how the iOS 17 CoreDevice/RSD shift affects tooling.

I'm looking for a full-time role in mobile security. If [Company] is growing the iOS side of the team, I'd love to talk.

[Your name]

---

### Device Forensics (Cellebrite, Oxygen, MSAB, contractors)

**Subject:** iOS device protocol experience — libimobiledevice/pymobiledevice3/idevicerestore

Hi [Name],

I've been doing hands-on work with the full iOS device extraction stack — AFC file access, MobileBackup2 protocol, lockdown pairing lifecycle, idevicerestore/DFU mode, and libirecovery.

I mapped the complete tool inventory across libimobiledevice 1.4.0 and documented how the iOS 17+ transport shift affects legacy extraction workflows. [GitHub link]

Open to full-time roles. Would [Company] have any openings that fit this background?

[Your name]

---

### iOS Tooling / Platform (Corellium, Apple, dev tool startups)

**Subject:** iOS device protocol + pymobiledevice3 depth

Hi [Name],

I've done a thorough mapping of the pymobiledevice3 CLI surface, the CoreDevice feature API, and the iOS 17+ RemoteXPC/RSD tunnel architecture. I also built a small Python tool on top of it for automated device recon.

Published reference here: [GitHub link]

Looking for full-time work on iOS platform or developer tooling in the Bay Area. Happy to chat if there's a fit at [Company].

[Your name]

---

## Where to Post / Who to Target

**LinkedIn search terms to find hiring managers:**
- "iOS security engineer" site:linkedin.com
- "mobile device management engineer" Jamf OR Kandji OR Mosyle
- "iOS platform engineer" Apple OR Corellium
- "mobile threat defense" Crowdstrike OR Lookout

**Communities to engage in (post your GitHub there too):**
- Reddit: r/jailbreakdevelopers, r/netsec, r/iOSProgramming
- Twitter/X: follow and engage with @doronz88 (pymobiledevice3 author), @danielpaulus (go-ios author)
- GitHub: star + watch the pymobiledevice3 and go-ios repos — comment on issues to get visibility

**Bug bounty angle (secondary income while job hunting):**
- Apple Security Research Device Program: https://security.apple.com/research-device/
- HackerOne Apple program
- Your service enumeration work is directly relevant as a recon methodology
