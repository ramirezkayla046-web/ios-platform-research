#!/usr/bin/env python3
"""
Generate data/services.json from the raw ios_services.txt list.
Run once: python3 scripts/build_services_json.py
"""

import json
import os

RAW_FILE = os.path.expanduser("~/cli_map/ios_services.txt")
OUT_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "services.json")

# Category rules: if any segment matches, assign that category
CATEGORY_MAP = [
    ("accessibility",       ["accessibility"]),
    ("afc",                 ["afc"]),
    ("amfi",                ["amfi"]),
    ("airtunes",            ["AirTunes", "airtunes"]),
    ("app_store",           ["appstored", "AppStore"]),
    ("app_protection",      ["appprotection"]),
    ("apps",                ["applicationaccess", "ApplicationService", "appplaceholder"]),
    ("assistant",           ["assistant"]),
    ("audio",               ["coreaudio", "audio", "AirTunes"]),
    ("backup",              ["backup", "MobileBackup"]),
    ("barcode",             ["BarcodeSupport"]),
    ("biometrics",          ["BiometricKit"]),
    ("bluetooth",           ["bluetooth"]),
    ("bridge",              ["Bridge"]),
    ("calendar",            ["calendar"]),
    ("carplay",             ["carkit"]),
    ("cloud",               ["CloudDocs", "cloudd", "CloudSubscription", "icloud", "iCloud"]),
    ("coredevice",          ["coredevice", "CoreDevice"]),
    ("debugserver",         ["debugserver", "debugproxy"]),
    ("developer_tools",     ["instruments", "dt.", "DVTSecure"]),
    ("diagnostics",         ["diagnostics", "iosdiagnostics"]),
    ("disk",                ["disk_usage", "AppleFSCompression"]),
    ("find_my",             ["findmydeviced", "findkit"]),
    ("gpu",                 ["AGX", "AGXG"]),
    ("icloud_pairing",      ["icloudpairing"]),
    ("internal",            ["internal.devicecompute", "internal.dt"]),
    ("itunes",              ["iTunes", "itunesstored"]),
    ("lockdown",            ["lockdown", "lockdownd"]),
    ("maps",                ["Maps"]),
    ("mdm",                 ["devicemanagementclient", "configurator"]),
    ("mobile_activation",   ["mobileactivationd"]),
    ("mobile_core",         ["mobile.backup", "mobile.debug", "mobile.diagnostics",
                              "mobile.heartbeat", "mobile.insecure", "mobile.internal",
                              "mobile.iTunes", "mobile.lockdown", "mobile.syslog"]),
    ("notification",        ["notification_proxy", "notificationproxy", "AOSNotification",
                              "accountnotifications", "ARQLNotifications"]),
    ("pairing",             ["dt.remotepairing", "remotepairingdeviced"]),
    ("tunnel",              ["tunnelservice", "tunneld", "usbmuxd", "usbmux"]),
    ("syslog",              ["syslog"]),
    ("springboard",         ["springboard"]),
    ("xpc",                 [".xpc"]),
    ("shim",                [".shim.remote"]),
]


def categorize(service: str) -> str:
    for category, keywords in CATEGORY_MAP:
        for kw in keywords:
            if kw in service:
                return category
    # Fall back to second segment
    parts = service.split(".")
    if len(parts) >= 3:
        return parts[2]
    return "other"


def build():
    with open(RAW_FILE, "r") as f:
        raw = [line.strip() for line in f if line.strip()]

    entries = []
    for svc in sorted(set(raw)):
        entries.append({
            "service": svc,
            "category": categorize(svc),
            "has_shim": svc.endswith(".shim.remote"),
            "is_xpc": svc.endswith(".xpc"),
        })

    output = {
        "meta": {
            "total": len(entries),
            "source": "live device enumeration + pymobiledevice3/libimobiledevice source analysis",
            "generated_by": "iosctl/scripts/build_services_json.py",
        },
        "services": entries,
    }

    os.makedirs(os.path.dirname(OUT_FILE), exist_ok=True)
    with open(OUT_FILE, "w") as f:
        json.dump(output, f, indent=2)

    print(f"[+] Written {len(entries)} services to {OUT_FILE}")

    # Print category summary
    from collections import Counter
    cats = Counter(e["category"] for e in entries)
    print("\nCategory breakdown:")
    for cat, count in sorted(cats.items(), key=lambda x: -x[1]):
        print(f"  {cat:<30} {count}")


if __name__ == "__main__":
    build()
