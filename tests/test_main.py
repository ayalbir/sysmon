import sys

from src import main as main_mod


def test_parse_args_defaults(monkeypatch):
    # simulate no CLI args
    monkeypatch.setattr(sys, "argv", ["main.py"])
    args = main_mod.parse_args()
    assert args.interval == 1.0
    assert args.bars == 30


def test_main_calls_run_monitor_loop(monkeypatch):
    called = {}

    def fake_run_monitor_loop(get_usage, log_usage, interval, bars):
        # record that it was called and check signature types
        called['get_usage'] = get_usage
        called['log_usage'] = log_usage
        called['interval'] = interval
        called['bars'] = bars

    # Replace run_monitor_loop with our fake
    monkeypatch.setattr(main_mod, 'run_monitor_loop', fake_run_monitor_loop)

    # Run main (it should call our fake run_monitor_loop)
    # ensure argparse in main() doesn't pick up pytest's CLI args
    monkeypatch.setattr(sys, 'argv', ['main.py'])
    main_mod.main()

    assert 'get_usage' in called and callable(called['get_usage'])
    assert 'log_usage' in called and callable(called['log_usage'])
    assert called['interval'] == 1.0
    assert called['bars'] == 30
