"""Discount codes on invoices. A discount is taken off the subtotal before tax."""

from decimal import Decimal


def _amount(value) -> Decimal:
    return Decimal(str(value))


def discount_for(subtotal: Decimal, code: str, codes: dict) -> Decimal:
    rule = codes.get(code)
    if rule is None:
        raise ValueError(f"Unknown discount code {code!r}")
    if subtotal < _amount(rule.get("min_subtotal", 0)):
        return Decimal("0.00")
    return min(subtotal, _amount(rule["amount"]))
