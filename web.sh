#!/usr/bin/env bash
set -e

newrelic-admin run-program gunicorn hc.wsgi \
  --max-requests 1000 \
  --max-requests-jitter 50 \
  --preload \
  --timeout 20 \
  --workers 4
