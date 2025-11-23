#!/bin/sh
exec .venv/bin/python src/api.py --host "${APP_HOST:-0.0.0.0}" --port "${APP_PORT:-80}"
