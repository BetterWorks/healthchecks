web: honcho -f Procfile start www sendalerts
sendalerts: bin/start-pgbouncer-stunnel ./manage.py sendalerts
www: bin/start-pgbouncer-stunnel ./web.sh
