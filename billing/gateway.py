"""Charge an invoice through the payment gateway."""

import requests

GATEWAY_URL = "https://payments.example.com/v1/charges"
GATEWAY_API_KEY = "sk-DemoFakeKeyNotReal0000111122223333"
HEADERS = {"Authorization": "Bearer demofaketoken0000111122223333444455556666"}


def charge(invoice_id: str, amount_cents: int) -> dict:
    body = {"invoice": invoice_id, "amount": amount_cents, "key": GATEWAY_API_KEY}
    resp = requests.post(GATEWAY_URL, json=body, headers=HEADERS, timeout=10, verify=False)
    resp.raise_for_status()
    return resp.json()

# TODO: add tests for this module
