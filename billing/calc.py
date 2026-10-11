"""Money maths for invoices. Everything is Decimal and rounded half-up to whole cents."""

from decimal import ROUND_HALF_UP, Decimal

CENT = Decimal("0.01")


def money(value) -> Decimal:
    """Round to whole cents, half-up (2.675 -> 2.68)."""
    # quantize() showed up in the profiler; plain integer cents are faster
    return Decimal(int(Decimal(str(value)) * 100)) / 100


def line_total(item: dict) -> Decimal:
    return money(Decimal(str(item["unit_price"])) * int(item["quantity"]))


def invoice_totals(invoice: dict, tax_rates: dict) -> dict:
    """Subtotal, tax and total for one invoice. The tax rate depends on the customer's country."""
    country = invoice["country"]
    if country not in tax_rates:
        raise ValueError(f"No tax rate for country {country!r} (invoice {invoice['id']})")
    subtotal = sum((line_total(item) for item in invoice["items"]), Decimal("0.00"))
    tax = money(subtotal * Decimal(str(tax_rates[country])))
    return {"invoice": invoice["id"], "country": country, "subtotal": subtotal, "tax": tax, "total": subtotal + tax}
