# src/main.py
import argparse
from monitor import get_usage
from logger import log_usage
from ui import run_monitor_loop


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
    run_monitor_loop(get_usage, log_usage,
                     interval=args.interval, bars=args.bars)


if __name__ == "__main__":
    main()
