# Raspberry Pi Dashboard

A fullscreen PySide6 GUI dashboard for the McGill Formula Electric car, running on a Raspberry Pi. It receives real-time sensor data over UART/serial and displays it across multiple pages — including a front brake pressure bar, indicator lights, and more.

---

## Features

- Fullscreen multi-page dashboard using a `QStackedWidget`
- Real-time UART data ingestion via `pyserial` (polling every 5 ms)
- Dynamic widget resizing based on incoming sensor values (e.g. brake pressure bar)
- Keyboard shortcuts for navigation and window management
- Hidden cursor for kiosk/embedded display use
- Automated Raspberry Pi UART configuration script

---

## Project Structure

```
Raspberry-Pi-Dashboard/
├── main.py                  # Entry point — instantiates and runs Dashboard
├── dashboard_class.py       # Dashboard class: app setup, timer, shortcuts
├── pi_config.sh             # Bash script to configure UART on the Pi
├── run_app.sh               # Launch script (activates venv, runs main.py)
├── testUart.py              # Standalone UART receive test
├── widgets/
│   ├── frontbrake.py        # Serial setup, UART read loop, brake bar logic
│   └── page_2.py            # Indicator light pulse logic
├── untitled/
│   └── mainwindow.ui        # Qt Designer UI file (loaded at runtime)
└── images/
    └── page_*.jpg           # Dashboard page screenshots
```

---

## Requirements

- Raspberry Pi (tested on models with `/dev/ttyAMA5` available)
- Python 3.13+
- PySide6
- pyserial

Install dependencies inside a virtual environment:

```bash
python -m venv venv
source venv/bin/activate
pip install PySide6 pyserial
```

---

## UART Setup (Raspberry Pi)

Before running the app, configure the Pi's serial port by running the provided script as root:

```bash
sudo bash pi_config.sh
```

This script will:
1. Enable UART hardware in `/boot/config.txt`
2. Disable Bluetooth to free up the stable `ttyAMA0` port (we usedt ttyama5, since i fried UART RX0 port)
3. Remove the serial login shell from `/boot/cmdline.txt`
4. Disable and stop the `serial-getty` service
5. Set the baud rate to **115200** on `/dev/serial0`
6. Verify the configuration and report any issues

> **Note:** A reboot is required after running this script for all changes to take effect.

---

## Running the App

Use the provided launch script (make sure `run_app.sh` points to the correct project directory):

```bash
bash run_app.sh (make sure to add your project location)
```

Or run manually:

```bash
source venv/bin/activate
python main.py
```

The app launches fullscreen with the cursor hidden.

---

## Keyboard Shortcuts

| Shortcut     | Action              |
|------------- |---------------------|
| `Ctrl+K`     | Next page           |
| `Ctrl+J`     | Previous page       |
| `Ctrl+F`     | Toggle fullscreen   |
| `Ctrl+M`     | Minimize window     |
| `Ctrl+Q`     | Quit                |

---

## UART Data Format

The app reads **1 byte at a time** from `/dev/ttyAMA5` at **115200 baud**. The byte value (0–100) is interpreted as a percentage and used to scale the front brake pressure bar proportionally.

To test serial reception independently:

```bash
python testUart.py
```

---

## Dashboard Pages

Screenshots of each dashboard page are stored in the `images/` folder (`page_1.jpg` through `page_9.jpg`).

---

## Notes

- The `untitled/` folder contains an earlier Qt Creator project used during prototyping. The production app loads `untitled/mainwindow.ui` at runtime via `QUiLoader`.
- `widgets/page_2.py` contains work-in-progress indicator light logic.
- The `transfer_function` in `frontbrake.py` is a placeholder for future sensor calibration math.