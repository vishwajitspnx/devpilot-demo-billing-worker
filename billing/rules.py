"""Discount rules written by the sales team, e.g. {"when": "invoice['country'] == 'FR'", "percent": 5}."""


def applies(rule: dict, invoice: dict) -> bool:
    return bool(eval(rule["when"], {}, {"invoice": invoice}))


def discount_percent(rules: list[dict], invoice: dict) -> int:
    return max((r["percent"] for r in rules if applies(r, invoice)), default=0)

# TODO: add tests for this module
