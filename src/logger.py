# src/logger.py
import csv
from datetime import datetime
from pathlib import Path

LOG_FILE = Path("logs/sysmon_log.csv")

def log_usage(cpu, mem, disk):
    LOG_FILE.parent.mkdir(exist_ok=True)  # ensure logs/ folder exists
    with LOG_FILE.open("a", newline="") as f:
        writer = csv.writer(f)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            str(cpu),
            str(mem),
            str(disk),
        ])
