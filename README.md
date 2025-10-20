# sysmon

## About

SysMon is a small cross-platform command-line system monitor written in Python. It samples CPU, memory and disk usage at a configurable interval and appends metric records to a CSV log (default: `logs/sysmon_log.csv`). The project is intended as a lightweight utility and a learning example for building CLI tools that use `psutil`.

Key features in this repo:
- Periodic sampling of system metrics (CPU, memory, disk)
- CSV logging via `src/logger.py`
- A simple terminal UI component in `src/ui.py`
- Unit tests in `tests/` covering core behavior

## Installation

Recommended (PowerShell):

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install -r requirements.txt
```

If you don't have a requirements.txt, install the runtime dependency:

```powershell
pip install psutil
```

## Usage

Run the monitor from the repository root:

```powershell
python -m src.main
```

Default output is appended to logs/sysmon_log.csv. Configure paths or log settings in src/logger.py as needed.


## Tests

Run the project's pytest test suite. The tests require `psutil`.

Recommended (PowerShell):

```powershell
python -m venv .venv        # optional, creates a virtual environment
.\.venv\Scripts\Activate.ps1
python -m pip install -U pip
pip install pytest psutil
pytest -q
```

Run a single test file:

```powershell
pytest tests/test_monitor.py -q
```

The tests are isolated (the logger test uses a temporary file) and `tests/conftest.py` adds the repo root to `sys.path` so imports like `from src import main` work.