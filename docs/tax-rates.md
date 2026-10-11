# Tax rates

`config/tax_rates.json` holds the standard VAT rate for each country we bill, as a fraction (`0.19` is 19%).
The worker refuses an invoice whose country has no rate.

## Where the numbers come from

<<<<<<< HEAD
Rates are copied by hand from the EU "VAT rates in Europe" page at the start of each quarter.
Finance checks the change before it is merged.
=======
Rates are copied from the national tax office of each country.
Any change needs a second reviewer from Finance and a note in the changelog.
>>>>>>> feature/tax-rate-review

## Adding a country

1. Add the two-letter country code and rate to `config/tax_rates.json`.
2. Set `"updated"` to today's date.
3. Add an invoice for that country to the tests.
