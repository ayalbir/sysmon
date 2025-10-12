# src/main.py
import time
import argparse
import sys
from monitor import get_usage
from logger import log_usage


def display_usage(cpu_usage, memory_usage, disk_usage, bars):

    def make_bar(usage, wanted_bars = bars):
        percent = usage / 100.0
        return '█' * int(percent * wanted_bars) + '-' * (wanted_bars - int(percent * wanted_bars))

    cpu_bars = make_bar(cpu_usage, bars)

    memory_bars = make_bar(memory_usage, bars)

    disk_bars = make_bar(disk_usage, bars)
    
    sys.stdout.write("\r\033[K")
    sys.stdout.write(
        f"rCPU Usage: |{cpu_bars}| {cpu_usage:.2f}%  "
        f"Memory Usage: |{memory_bars}| {memory_usage:.2f}%"
        f"Disk Usage: |{disk_bars}| {disk_usage:.2f}%"
    )
    sys.stdout.flush()

def parse_args():
    parser = argparse.ArgumentParser(
        description="SysMon – Simple system monitor"
    )
    parser.add_argument(
        "--interval",
        type=float,
        default=1.0,
        help="Refresh interval in seconds (default: 1.0)",
    )
    parser.add_argument(
        "--bars",
        type=int,
        default=30,
        help="Number of characters in each usage bar (default: 30)",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    try:
        while True:
            cpu, mem, disk = get_usage()
            display_usage(cpu, mem, disk, args.bars)
            log_usage(cpu, mem, disk)
            time.sleep(args.interval)
    except KeyboardInterrupt:
        print("\nExiting. Goodbye!")

if __name__ == "__main__":
    main()
