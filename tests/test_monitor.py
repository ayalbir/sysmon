# tests/test_monitor.py
from src.monitor import get_usage

def test_get_usage_returns_three_numbers():
    cpu, mem, disk = get_usage()
    assert isinstance(cpu, (int, float))
    assert isinstance(mem, (int, float))
    assert isinstance(disk, (int, float))

def test_get_usage_values_in_range():
    cpu, mem, disk = get_usage()
    for val in (cpu, mem, disk):
        assert 0 <= val <= 100
