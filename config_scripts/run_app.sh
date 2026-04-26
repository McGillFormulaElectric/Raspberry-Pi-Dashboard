#!/bin/bash
chmod +x /home/mcgillformulaelectric/Raspberry-Pi-Dashboard/config_scripts/run_app.sh
cd /home/mcgillformulaelectric/Raspberry-Pi-Dashboard || exit

source venv/bin/activate 

python main.py

