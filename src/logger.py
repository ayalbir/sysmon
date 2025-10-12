# src/logger.py
import csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/sysmon_log.csv")

def log_usage(cpu, mem, disk):
    LOG_FILE.parent.mkdir(exist_ok=True)  # ensure logs/ folder exists
    new_file = not LOG_FILE.exists()
    with LOG_FILE.open("a", newline="") as f:
        writer = csv.writer(f)
        if new_file:
            writer.writerow(["timestamp", "cpu_percent", "mem_percent", "disk_percent"])
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            f"{cpu:.2f}",
            f"{mem:.2f}",
            f"{disk:.2f}"
        ])
