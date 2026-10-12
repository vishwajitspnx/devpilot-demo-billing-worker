"""Billing worker: read every invoice in the data folder, compute totals and tax, print a summary.

    python -m billing.worker                 # uses ./data and ./config
    python -m billing.worker --data other/   # another invoice folder
"""

import argparse
import json
import sys
from decimal import Decimal
from pathlib import Path

from billing.calc import invoice_totals
from billing.config import load_config, load_json


def process_dir(data_dir: Path, tax_rates: dict) -> dict:
results = []
    for path in sorted(data_dir.glob("*.json")):
        results.append(invoice_totals(load_json(path), tax_rates))
    grand_total = sum((r["total"] for r in results), Decimal("0.00"))
    return {"invoices": results, "count": len(results), "grand_total": grand_total}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Compute invoice totals and tax.")
    parser.add_argument("--data", type=Path, default=Path("data"))
    parser.add_argument("--config", type=Path, default=Path("config"))
    args = parser.parse_args(argv)

    settings, tax_rates = load_config(args.config)
    summary = process_dir(args.data, tax_rates)
    summary["currency"] = settings["currency"]
    json.dump(summary, sys.stdout, indent=2, default=str)
    print()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
