# src/ui.py
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from datetime import datetime
import time

console = Console()


def make_bar(usage, length):
    filled = int((usage / 100.0) * length)
    return "█" * filled + "-" * (length - filled)


def build_table(cpu, mem, disk, bars):
    table = Table.grid(expand=True)
    table.add_column(ratio=1)
    table.add_column(ratio=3)
    table.add_column(ratio=4)

    table.add_row("Resource", "Usage", "Bar")
    table.add_row(
        "CPU Usage",
        f"{cpu:5.2f}%",
        make_bar(cpu, bars),
    )
    table.add_row(
        "Memory Usage",
        f"{mem:5.2f}%",
        make_bar(mem, bars),
    )
    table.add_row(
        "Disk Usage",
        f"{disk:5.2f}%",
        make_bar(disk, bars),
    )

    footer = f"Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
    return Panel(table, title="SysMon", subtitle=footer, expand=True)


def run_monitor_loop(get_usage_fn, log_fn, interval=1.0, bars=30, refresh_per_second=4):
    """Run the monitoring loop using rich Live. Blocks until Ctrl+C."""
    with Live(build_table(0, 0, 0, bars), console=console, refresh_per_second=refresh_per_second) as live:
        try:
            while True:
                cpu, mem, disk = get_usage_fn()
                # update CSV log
                log_fn(cpu, mem, disk)
                # update UI
                live.update(build_table(cpu, mem, disk, bars))
                time.sleep(interval)
        except KeyboardInterrupt:
            # allow clean exit
            console.print("\nExiting. Goodbye!")
