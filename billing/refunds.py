"""Refund part of an invoice (work in progress)."""

from decimal import Decimal


def refund(invoice: dict, amount: Decimal) -> dict
    if amount > invoice["total"]:
        raise ValueError("refund is larger than the invoice")
    return {**invoice, "refunded": amount, "total": invoice["total"] - amount}
