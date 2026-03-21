"""
iosctl.commands.probe_all — probe every known service and log reachability
"""

import subprocess
import os
import sys
from datetime import datetime
from .logger import log, log_result

PMD3_CANDIDATES = [
    "/home/runitup/pymobiledevice3/venv/bin/pymobiledevice3",
    "/home/runitup/venv/bin/pymobiledevice3",
    "pymobiledevice3",
]

# Path to the known service list (one com.apple.* identifier per line)
SERVICE_FILE = os.path.expanduser("~/iosctl/data/services.txt")

# Per-service probe timeout in seconds
PROBE_TIMEOUT = 5


def _find_pmd3() -> str:
    import shutil
    for candidate in PMD3_CANDIDATES:
        if shutil.which(candidate) or (candidate.startswith("/") and __import__("os").path.isfile(candidate)):
            return candidate
    return "pymobiledevice3"


def _load_services() -> list[str]:
    """Load service list from data file."""
    if not os.path.exists(SERVICE_FILE):
        print(f"[!] Service list not found at {SERVICE_FILE}")
        print("    Run: cp ~/cli_map/ios_services.txt ~/iosctl/data/services.txt")
        return []

    with open(SERVICE_FILE, "r") as f:
        return [line.strip() for line in f if line.strip()]


def _probe(pmd3: str, service: str) -> tuple[str, str]:
    """
    Attempt to start a lockdown service.
    Returns (status, detail) where status is SUCCESS | FAIL | TIMEOUT | ERROR.
    """
    try:
        result = subprocess.run(
            [pmd3, "lockdown", "start-service", service],
            capture_output=True,
            text=True,
            timeout=PROBE_TIMEOUT,
        )
        if result.returncode == 0:
            return "SUCCESS", ""
        else:
            detail = (result.stderr or result.stdout).strip().splitlines()[0] if (result.stderr or result.stdout) else ""
            return "FAIL", detail

    except subprocess.TimeoutExpired:
        return "TIMEOUT", f">{PROBE_TIMEOUT}s"

    except Exception as e:
        return "ERROR", str(e)


def run():
    """Probe all known services and produce a reachability report."""
    pmd3 = _find_pmd3()
    services = _load_services()

    if not services:
        return

    total = len(services)
    print(f"[*] Probing {total} services (timeout: {PROBE_TIMEOUT}s each)...\n")
    log(f"probe-all: started — {total} services")

    results = {"SUCCESS": [], "FAIL": [], "TIMEOUT": [], "ERROR": []}
    start_time = datetime.now()

    for i, service in enumerate(services, 1):
        status, detail = _probe(pmd3, service)
        results[status].append(service)

        # Status indicator
        indicator = {"SUCCESS": "✓", "FAIL": "✗", "TIMEOUT": "⏱", "ERROR": "!"}.get(status, "?")
        detail_str = f"  ({detail})" if detail else ""
        print(f"  [{i:4d}/{total}] {indicator} {service}{detail_str}")
        log_result(service, f"{status} {detail}".strip())

    elapsed = (datetime.now() - start_time).total_seconds()

    # Summary
    print(f"\n{'─' * 60}")
    print(f"  Probe complete in {elapsed:.1f}s\n")
    print(f"  ✓ Reachable  : {len(results['SUCCESS'])}")
    print(f"  ✗ Unreachable: {len(results['FAIL'])}")
    print(f"  ⏱ Timeout    : {len(results['TIMEOUT'])}")
    print(f"  ! Error      : {len(results['ERROR'])}")
    print(f"{'─' * 60}\n")

    if results["SUCCESS"]:
        print("[+] Reachable services:")
        for s in results["SUCCESS"]:
            print(f"    {s}")

    log(f"probe-all: complete — {len(results['SUCCESS'])} reachable / {total} total")

    # Write structured report
    _write_report(results, elapsed)


def _write_report(results: dict, elapsed: float):
    """Write a timestamped probe report to logs/."""
    report_dir = os.path.expanduser("~/iosctl/logs")
    os.makedirs(report_dir, exist_ok=True)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    report_path = os.path.join(report_dir, f"probe_{timestamp}.txt")

    with open(report_path, "w") as f:
        f.write(f"iosctl probe-all report\n")
        f.write(f"Generated: {datetime.now().isoformat()}\n")
        f.write(f"Duration:  {elapsed:.1f}s\n\n")

        for status, services in results.items():
            f.write(f"[{status}] ({len(services)})\n")
            for s in services:
                f.write(f"  {s}\n")
            f.write("\n")

    print(f"[+] Report saved: {report_path}")
    log(f"probe-all: report saved to {report_path}")
