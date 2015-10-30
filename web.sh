#!/usr/bin/env bash
set -e

NEW_RELIC_APP_NAME="web" newrelic-admin run-program gunicorn hc.wsgi \
  --max-requests 1000 \
  --max-requests-jitter 50 \
  --preload \
  --threads 4 \
  --timeout 20 \
  --workers 4
