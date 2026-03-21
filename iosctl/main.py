#!/usr/bin/env python3
"""
iosctl — iOS device recon and service enumeration CLI
Built on top of pymobiledevice3.
"""

import sys
import os

# Ensure commands directory is importable
sys.path.insert(0, os.path.dirname(__file__))

from commands import scan, services, probe_all
from commands.logger import log

VERSION = "0.1.0"

USAGE = """
iosctl v{version} — iOS device recon CLI

Usage:
  iosctl <command> [options]

Commands:
  scan          Detect connected iOS devices and show device info
  services      List all accessible lockdown services on connected device
  probe-all     Probe every known service and log reachability results
  version       Show version

Options:
  -h, --help    Show this help message

Examples:
  iosctl scan
  iosctl services
  iosctl probe-all
""".format(version=VERSION)


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help"):
        print(USAGE)
        return

    cmd = sys.argv[1]

    if cmd == "scan":
        log(f"Command: scan")
        scan.run()

    elif cmd == "services":
        log(f"Command: services")
        services.run()

    elif cmd == "probe-all":
        log(f"Command: probe-all")
        probe_all.run()

    elif cmd == "version":
        print(f"iosctl v{VERSION}")

    else:
        print(f"[!] Unknown command: {cmd}")
        print(USAGE)
        sys.exit(1)


if __name__ == "__main__":
    main()
