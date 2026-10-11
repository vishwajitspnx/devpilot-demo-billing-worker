# syntax=docker/dockerfile:1.7
# Demo billing worker. Build from the repository root.
FROM python:3.13.7-slim AS base
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1 PIP_NO_CACHE_DIR=1 PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /srv
RUN useradd --create-home --uid 10001 billing

FROM base AS test
COPY requirements-dev.txt ./
RUN pip install -r requirements-dev.txt
COPY pytest.ini ./
COPY billing ./billing
COPY config ./config
COPY data ./data
COPY tests ./tests
USER billing
CMD ["pytest", "-q"]

FROM base AS app
COPY billing ./billing
COPY config ./config
COPY data ./data
USER billing
CMD ["python", "-m", "billing.worker"]
