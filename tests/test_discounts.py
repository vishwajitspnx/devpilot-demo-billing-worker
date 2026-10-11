from decimal import Decimal

import pytest

from billing.calc import invoice_totals
from billing.discounts import discount_for

CODES = {
    "LOYAL5": {"type": "fixed", "amount": 5.00},
    "BULK50": {"type": "fixed", "amount": 50.00, "min_subtotal": 500.00},
}


def test_fixed_discount():
    assert discount_for(Decimal("80.00"), "LOYAL5", CODES) == Decimal("5.00")


def test_minimum_subtotal():
    assert discount_for(Decimal("499.99"), "BULK50", CODES) == Decimal("0.00")


def test_discount_never_exceeds_subtotal():
    assert discount_for(Decimal("3.00"), "LOYAL5", CODES) == Decimal("3.00")


def test_unknown_code():
    with pytest.raises(ValueError):
        discount_for(Decimal("10.00"), "NOPE", CODES)


def test_invoice_with_discount_code():
    invoice = {"id": "T-3", "country": "DE", "discount_code": "LOYAL5",
               "items": [{"unit_price": 100.00, "quantity": 1}]}
    totals = invoice_totals(invoice, {"DE": 0.19}, CODES)
    assert totals["discount"] == Decimal("5.00")


def test_percent_discount():
    codes = {"AUTUMN10": {"type": "percent", "percent": 10}}
    assert discount_for(Decimal("80.00"), "AUTUMN10", codes) == Decimal("8.00")
