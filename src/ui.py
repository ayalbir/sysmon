# src/ui.py
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich.panel import Panel
from rich.text import Text
from datetime import datetime
import time

console = Console()


def color_for(usage):
    # Decide color based on usage percentage
    if usage < 50:
        return "green"
    if usage < 80:
        return "yellow"
    return "red"


def make_colored_bar(usage, length):
    filled = int((usage / 100.0) * length)
    empty = max(0, length - filled)
    color = color_for(usage)

    text = Text()
    if filled:
        text.append("█" * filled, style=f"bold {color}")
    if empty:
        text.append("-" * empty, style="dim")
    return text


def build_table(cpu, mem, disk, bars):
    table = Table.grid(expand=True)
    table.add_column(ratio=1)
    table.add_column(ratio=1, justify="right")
    table.add_column(ratio=4)

    table.add_row("Resource", "Usage", "Bar")
    table.add_row(
        "CPU",
        Text(f"{cpu:5.2f}%", style=color_for(cpu)),
        make_colored_bar(cpu, bars),
    )
    table.add_row(
        "Memory",
        Text(f"{mem:5.2f}%", style=color_for(mem)),
        make_colored_bar(mem, bars),
    )
    table.add_row(
        "Disk",
        Text(f"{disk:5.2f}%", style=color_for(disk)),
        make_colored_bar(disk, bars),
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
