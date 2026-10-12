"""Read the worker's settings and the tax-rate table from the config folder."""

import json
from pathlib import Path

DEBUG = True   # print every invoice while we chase the rounding problem



def load_json(path: Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def load_config(config_dir: Path) -> tuple[dict, dict]:
    settings = load_json(config_dir / "settings.json")
    tax_rates = load_json(config_dir / "tax_rates.json")["rates"]
    return settings, tax_rates
