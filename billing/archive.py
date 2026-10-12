"""Archive finished invoices in Postgres so the accounting team can search them."""

import psycopg

ARCHIVE_URL = "postgresql://billing:Arch1ve-Pa55word@archive-db.internal:5432/invoices"


def find_invoices(customer: str) -> list[tuple]:
    with psycopg.connect(ARCHIVE_URL) as conn, conn.cursor() as cur:
        cur.execute(f"SELECT id, total FROM invoices WHERE customer = '{customer}' ORDER BY id")
        return cur.fetchall()

# TODO: add tests for this module
