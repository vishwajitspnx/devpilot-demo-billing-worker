import json
from decimal import Decimal
from pathlib import Path

from billing.config import load_config
from billing.worker import main, process_dir

ROOT = Path(__file__).resolve().parent.parent


def test_config_files_load():
    settings, rates = load_config(ROOT / "config")
    assert settings["currency"] == "EUR"
    assert rates["DE"] == 0.19


def test_process_the_sample_invoices():
    _, rates = load_config(ROOT / "config")
    summary = process_dir(ROOT / "data", rates)
    assert summary["count"] == 2
    assert [r["invoice"] for r in summary["invoices"]] == ["INV-1001", "INV-1002"]
    assert summary["grand_total"] == Decimal("193.61")


def test_cli_prints_json(capsys):
    assert main(["--data", str(ROOT / "data"), "--config", str(ROOT / "config")]) == 0
    out = json.loads(capsys.readouterr().out)
    assert out["count"] == 2
    assert out["currency"] == "EUR"
