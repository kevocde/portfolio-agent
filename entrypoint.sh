#!/bin/sh
exec .venv/bin/python src/app.py --host "${HOST:-0.0.0.0}" --port "${PORT:-80}"
