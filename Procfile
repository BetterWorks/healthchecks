web: PYTHONIOENCODING="utf-8" ./bin/start-pgbouncer honcho -f Procfile start www sendalerts
sendalerts: NEW_RELIC_APP_NAME="sendalerts" ./manage.py sendalerts
www: NEW_RELIC_APP_NAME="web" ./web.sh
