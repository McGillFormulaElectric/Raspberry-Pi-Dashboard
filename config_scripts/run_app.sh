#!/bin/bash

set -u

APP_DIR="/home/mcgillformulaelectric/Raspberry-Pi-Dashboard"
LOG_FILE="$APP_DIR/run_app.log"

{
    echo "===== $(date) starting dashboard ====="

    cd "$APP_DIR" || exit 1

    export DISPLAY="${DISPLAY:-:0}"
    export XAUTHORITY="${XAUTHORITY:-/home/mcgillformulaelectric/.Xauthority}"
    export XDG_RUNTIME_DIR="${XDG_RUNTIME_DIR:-/run/user/$(id -u)}"

    # Give the desktop session and hardware devices a moment to appear after boot.
    sleep 10

    source "$APP_DIR/venv/bin/activate"
    exec "$APP_DIR/venv/bin/python" "$APP_DIR/main.py"
} >> "$LOG_FILE" 2>&1