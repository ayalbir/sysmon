# sysmon

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