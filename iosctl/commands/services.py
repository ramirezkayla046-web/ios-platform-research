"""
iosctl.commands.services — enumerate accessible lockdown services on connected device
"""

import subprocess
import sys
from .logger import log

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
    """List all lockdown services accessible on the connected device."""
    pmd3 = _find_pmd3()

    print("[*] Enumerating lockdown services on connected device...\n")
    log("services: started")

    try:
        result = subprocess.run(
            [pmd3, "lockdown", "services"],
            capture_output=True,
            text=True,
            timeout=15,
        )

        if result.returncode != 0:
            stderr = result.stderr.strip()
            print(f"[!] Failed to list services.")
            if stderr:
                print(f"    {stderr}")
            log(f"services: failed — {stderr}")
            return

        lines = [l for l in result.stdout.splitlines() if l.strip()]

        if not lines:
            print("[!] No services returned. Is a device paired and connected?")
            log("services: empty result")
            return

        print(f"[+] {len(lines)} services found:\n")
        for line in sorted(lines):
            print(f"  {line}")

        log(f"services: found {len(lines)} services")

    except FileNotFoundError:
        print("[!] pymobiledevice3 not found. Check your venv path.")
        log("services: pymobiledevice3 not found")
        sys.exit(1)

    except subprocess.TimeoutExpired:
        print("[!] Service enumeration timed out.")
        log("services: timeout")
        sys.exit(1)

    except Exception as e:
        print(f"[!] Unexpected error: {e}")
        log(f"services: error — {e}")
        sys.exit(1)
