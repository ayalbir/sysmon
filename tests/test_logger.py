# tests/test_logger.py
import os
import csv
from src.logger import log_usage, LOG_FILE

def test_log_usage_creates_file(tmp_path):
    test_file = tmp_path / "test_log.csv"
    from src import logger
    logger.LOG_FILE = test_file  # temporarily redirect output

    log_usage(10.5, 20.0, 30.0)
    assert test_file.exists()

    with open(test_file) as f:
        rows = list(csv.reader(f))
        assert len(rows) == 1
        assert rows[0][1:] == ["10.5", "20.0", "30.0"]
