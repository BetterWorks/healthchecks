#!/usr/bin/env bash
set -e

bin/start-nginx \
newrelic-admin run-program gunicorn hc.wsgi \
  --max-requests 1000 \
  --max-requests-jitter 50 \
  --preload \
  --timeout 20 \
  --workers 4 \
  --bind unix:/tmp/nginx.socket \
  --pid /tmp/app-initialized
