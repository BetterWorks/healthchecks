#!/usr/bin/env bash
set -e

if [ -z "$WEB_CONCURRENCY" ]; then
  export WEB_CONCURRENCY=6
  echo "Setting WEB_CONCURRENCY=6"
fi

bin/start-nginx \
newrelic-admin run-program gunicorn hc.wsgi \
  --preload \
  --timeout 20 \
  --workers $WEB_CONCURRENCY \
  --bind unix:/tmp/nginx.socket \
  --pid /tmp/app-initialized
