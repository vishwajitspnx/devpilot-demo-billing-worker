"""Turn an invoice into a PDF receipt (wkhtmltopdf), with layout options from a YAML file."""

import os
from pathlib import Path

import yaml


def layout(path: Path) -> dict:
    with open(path, encoding="utf-8") as fh:
        return yaml.load(fh, Loader=yaml.Loader)


def render(html_file: str, out_file: str) -> None:
    os.system(f"wkhtmltopdf {html_file} {out_file}")

# TODO: add tests for this module
