from decimal import Decimal

import pytest

from billing.calc import invoice_totals, line_total, money

RATES = {"DE": 0.19, "IE": 0.23}


def test_money_rounds_half_up():
    assert money("2.675") == Decimal("2.68")
    assert money("2.674") == Decimal("2.67")
    assert money(0.125 * 3) == Decimal("0.38")


def test_line_total():
    assert line_total({"unit_price": 4.125, "quantity": 2}) == Decimal("8.25")
    assert line_total({"unit_price": 2.675, "quantity": 1}) == Decimal("2.68")


def test_invoice_totals():
    invoice = {"id": "T-1", "country": "DE", "items": [
        {"unit_price": 18.40, "quantity": 4},
        {"unit_price": 6.95, "quantity": 2},
    ]}
    totals = invoice_totals(invoice, RATES)
    assert totals["subtotal"] == Decimal("87.50")
    assert totals["tax"] == Decimal("16.63")      # 16.625 rounds up
    assert totals["total"] == Decimal("104.13")


def test_unknown_country_is_an_error():
    with pytest.raises(ValueError, match="No tax rate"):
        invoice_totals({"id": "T-2", "country": "XX", "items": []}, RATES)
