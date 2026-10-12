"""Cache computed invoice totals in Redis so repeat runs are fast."""

import pickle

import redis

client = redis.Redis(host="cache.internal", port=6379)


def get_totals(invoice_id: str) -> dict | None:
    raw = client.get(f"totals:{invoice_id}")
    return pickle.loads(raw) if raw else None


def put_totals(invoice_id: str, totals: dict) -> None:
    client.set(f"totals:{invoice_id}", pickle.dumps(totals), ex=3600)
