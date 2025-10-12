import psutil
import time
import argparse
from rich import print


def display_usage(cpu_usage, memory_usage, bars=50):
    cpu_percent = cpu_usage / 100.0
    cpu_bars = '█' * int(cpu_percent * bars) + '-' * \
        (bars - int(cpu_percent * bars))

    memory_percent = memory_usage / 100.0
    memory_bars = '█' * int(memory_percent * bars) + \
        '-' * (bars - int(memory_percent * bars))

    print(f"\rCPU Usage: |{cpu_bars}| {cpu_usage:.2f}%  ", end='')
    print(f"Memory Usage: |{memory_bars}| {memory_usage:.2f}%", end='\r')


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
    args = parse_args()  # get command-line values

    while True:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        display_usage(cpu, mem, args.bars)
        time.sleep(args.interval)


if __name__ == "__main__":
    main()
