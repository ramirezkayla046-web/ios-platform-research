"""
iosctl.commands.scan — detect and display connected iOS devices
"""

import subprocess
import sys
from .logger import log

# Prefer the venv pymobiledevice3 if available, fall back to system PATH
PMD3_CANDIDATES = [
    "/home/runitup/pymobiledevice3/venv/bin/pymobiledevice3",
    "/home/runitup/venv/bin/pymobiledevice3",
    "pymobiledevice3",
]


def _find_pmd3() -> str:
    import shutil
    for candidate in PMD3_CANDIDATES:
        if shutil.which(candidate) or (candidate.startswith("/") and __import__("os").path.isfile(candidate)):
            return candidate
    return "pymobiledevice3"


def run():
    """Scan for connected iOS devices and print basic device info."""
    pmd3 = _find_pmd3()

    print("[*] Scanning for connected iOS devices...\n")
    log("scan: started")

    # List connected devices
    try:
        result = subprocess.run(
            [pmd3, "usbmux", "list"],
            capture_output=True,
            text=True,
            timeout=10,
        )

        if result.returncode != 0 or not result.stdout.strip():
            print("[!] No devices found. Check USB connection and trust prompt.")
            log("scan: no devices found")
            return

        print("[+] Connected devices:\n")
        print(result.stdout)
        log(f"scan: success\n{result.stdout.strip()}")

    except FileNotFoundError:
        print(f"[!] pymobiledevice3 not found. Check your venv path.")
        log("scan: pymobiledevice3 not found")
        sys.exit(1)

    except subprocess.TimeoutExpired:
        print("[!] Scan timed out.")
        log("scan: timeout")
        sys.exit(1)

    except Exception as e:
        print(f"[!] Unexpected error during scan: {e}")
        log(f"scan: error — {e}")
        sys.exit(1)
