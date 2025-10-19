#!/bin/sh
service redis-server start
exec .venv/bin/python src/app.py --host "${APP_HOST:-0.0.0.0}" --port "${APP_PORT:-80}"
