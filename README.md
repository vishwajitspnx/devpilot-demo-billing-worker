# Demo Billing Worker (DevPilot test project)

A tiny background worker (Python): it reads invoices from `data/*.json`, works out subtotal, tax and total for each,
and prints a summary. Settings are in `config/settings.json`, tax rates per country in `config/tax_rates.json`.
It exists to **try out DevPilot**. Some branches contain **bugs on purpose**.

> Do not deploy this anywhere real. The bugs and the fake passwords in it are deliberate.

## Run it

Docker is all you need. The worker has no web page: it runs once and prints JSON.

```bash
docker build --target app -t billing-worker . && docker run --rm billing-worker     # run the worker
docker build --target test -t billing-worker-test . && docker run --rm billing-worker-test   # unit tests
```

Money is rounded half-up to whole cents (`2.675` becomes `2.68`).

## Branches (stages)

| Branch | Stage | Deploy workflow |
|---|---|---|
| `develop` | development | none (local copy) |
| `staging` | staging | `deploy-staging.yml` |
| `main` | production | `deploy-production.yml` |

Other branches: `feature/discount-codes` and `feature/eu-tax-rates` (new features, start from `develop`),
and `wip/email-receipts` (a developer's work in progress, no pull request).

The deploy workflows only print what they would do: there is no real server.

## Planted problems (what DevPilot should notice)

| Where | Problem | DevPilot today |
|---|---|---|
| `main` (and every branch) | Hard-coded database password in `config/settings.json` (`"db_password": ...`) | Should be a finding (high). Check: the password pattern may miss a quoted JSON key |
| `develop` | Money is rounded down instead of half-up, unit tests fail, so CI fails | CI failure finding on the development stage |
| PR `feature/discount-codes` → `develop` | Python syntax error (unclosed bracket) in `billing/discounts.py` | Finding (high) |
| same PR | With a discount code, tax is charged twice (tax on a price that already has tax) | **Not found yet**: needs AI review (Phase 1b) |
| `feature/eu-tax-rates` (no PR) | `config/tax_rates.json` is not valid JSON (trailing comma) | Finding (medium) |
| same branch | Leftover merge-conflict markers in `docs/tax-rates.md` | Finding (high) |
| `wip/email-receipts` (no PR) | Hard-coded SMTP password in `billing/mailer.py` | Finding (high), if developer branches are watched |

`staging` is the same as `main`.
