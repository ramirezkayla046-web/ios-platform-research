"""
iosctl.commands.logger — simple timestamped file logger
"""

import os
from datetime import datetime

LOG_PATH = os.path.expanduser("~/iosctl/logs/main.log")


def _ensure_log_dir():
    os.makedirs(os.path.dirname(LOG_PATH), exist_ok=True)


def log(msg: str):
    """Append a timestamped message to the main log file."""
    _ensure_log_dir()
    entry = f"{datetime.now().isoformat()} | {msg}\n"
    with open(LOG_PATH, "a") as f:
        f.write(entry)


def log_result(service: str, status: str):
    """Log a service probe result."""
    _ensure_log_dir()
    entry = f"{datetime.now().isoformat()} | {service} | {status}\n"
    with open(LOG_PATH, "a") as f:
        f.write(entry)
