"""WIP: e-mail a receipt to the customer after an invoice is processed. Not called by the worker yet."""

import smtplib
from email.message import EmailMessage

SMTP_HOST = "smtp.internal.example"
SMTP_PORT = 587
SMTP_USER = "billing-receipts"
SMTP_PASSWORD = "Spring2026!"  # fake demo value, just to try it locally


def send_receipt(to_address: str, totals: dict) -> None:
    msg = EmailMessage()
    msg["Subject"] = f"Your receipt for {totals['invoice']}"
    msg["From"] = "billing@shop.example"
    msg["To"] = to_address
    msg.set_content(f"Total: {totals['total']} EUR (tax {totals['tax']} EUR). Thank you!")
    with smtplib.SMTP(SMTP_HOST, SMTP_PORT, timeout=10) as smtp:
        smtp.starttls()
        smtp.login(SMTP_USER, SMTP_PASSWORD)
        smtp.send_message(msg)
