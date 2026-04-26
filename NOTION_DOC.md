# Raspberry Pi Dashboard — Full Project Documentation

This document is the complete reference for the McGill Formula Electric driver dashboard running on the Raspberry Pi. It's split into two halves: the first half is meant for non-technical people who just need to run or update the dashboard, and the second half is a deeper walkthrough of how the project is built so anyone taking it over can pick it up.

---

# Part 1 — User Guide

## What it does

The dashboard is what shows up on the car's screen. It displays:

- Speed, throttle, and brake pressure
- Battery voltage, current, and temperature
- Tire temperatures and tire pressure
- Pit mode, charging, and balancing status

The Pi reads live data coming in from the car's electronics over a wire (UART) and updates the screen roughly a thousand times a second. It's a Python program built with a library called PySide6.

## Running it the normal way

The Pi is configured to start the dashboard automatically when it boots. Most of the time this is all you have to do:

1. Plug the Pi into power.
2. Wait about 30 seconds.
3. The dashboard should come up fullscreen.

If numbers are moving on the screen, you're good.

## Running it manually

If the dashboard didn't come up on its own, you'll need to start it yourself.

### 1. Open a terminal

If the dashboard is frozen or stuck on a black screen, press `Ctrl + Q` to close it first. Then click the terminal icon at the top of the screen (the one that looks like `>_`). If you're already looking at a text screen, you're in a terminal, just keep going.

### 2. Go to the project folder

```bash
cd /home/mcgillformulaelectric/Raspberry-Pi-Dashboard
```

### 3. Activate the virtual environment

```bash
source venv/bin/activate
```

You should see `(venv)` appear at the start of the line. That means it worked.

### 4. Run the dashboard

Important: the dashboard has to be started with `main.py`. Don't try to run any other Python file in this project, it won't work.

```bash
python main.py
```

The screen should come up fullscreen within a few seconds.

### The shortcut

All three steps above are bundled into a script. If you just want the thing to run:

```bash
bash /home/mcgillformulaelectric/Raspberry-Pi-Dashboard/config_scripts/run_app.sh
```

## Updating the code on the Pi

When I push new code to GitHub, you'll need to pull it down onto the Pi. For whatever reason, the Pi almost always complains about merge conflicts or local changes when you try to pull normally. Don't worry about it. Just throw away whatever is on the Pi and take what's on GitHub.

### 1. Open a terminal

Same as before. Close the dashboard with `Ctrl + Q` if it's running.

### 2. Run these commands, one at a time

Copy each line, paste it in, hit Enter. Just trust it.

```bash
cd /home/mcgillformulaelectric/Raspberry-Pi-Dashboard
```

```bash
git fetch origin
```

```bash
git reset --hard origin/main
```

```bash
git clean -fd
```

What those do, in plain English:

- `cd` goes to the project folder.
- `git fetch origin` grabs the latest code from GitHub but doesn't change anything yet.
- `git reset --hard origin/main` wipes out any local changes on the Pi and overwrites everything with the GitHub version. This is the "accept all incoming changes" button.
- `git clean -fd` deletes any extra files lying around that aren't supposed to be there.

### 3. Restart the dashboard

Either run it again:

```bash
bash /home/mcgillformulaelectric/Raspberry-Pi-Dashboard/config_scripts/run_app.sh
```

Or just reboot and let it auto-start:

```bash
sudo reboot
```

### If git asks for a username or password

Use the credentials I gave you. If you don't have any, call me, I'll need to log you in once and then it'll remember.

### If it still complains

Here's the same four commands chained into one line. Paste it and it'll reset everything no matter what state the Pi is in:

```bash
cd /home/mcgillformulaelectric/Raspberry-Pi-Dashboard && git fetch origin && git reset --hard origin/main && git clean -fd
```

## Keyboard shortcuts

These work while the dashboard is running:

| Keys | What it does |
|------|--------------|
| `Ctrl + K` | Next page |
| `Ctrl + J` | Previous page |
| `Ctrl + F` | Toggle fullscreen |
| `Ctrl + M` | Minimize window |
| `Ctrl + Q` | Quit the dashboard |

The mouse cursor is hidden on purpose, that's not a bug.

## When something goes wrong

### The screen is black or nothing is showing

- Give it 30 to 60 seconds, it sometimes takes a moment.
- Check that the Pi is actually on (red light on the Pi board).
- Make sure the screen cable is seated properly at both ends.
- Unplug the Pi, wait 10 seconds, plug it back in.

### "No module named PySide6" or similar

The virtual environment isn't active. Go back to step 3 in the manual run section:

```bash
cd /home/mcgillformulaelectric/Raspberry-Pi-Dashboard
source venv/bin/activate
python main.py
```

### The dashboard opens but everything stays at zero

The dashboard is running fine, it's just not getting any data from the car. Usually one of:

- The car's electronics aren't powered on.
- The UART wire between the Pi and the car popped off.
- The yellow and orange wires going into the Pi's GPIO pins aren't seated properly.
- The car's main power switch is off.

If the wires all look fine and the car is on, try the UART setup step below.

### "Could not open port" or "/dev/serial0 not found"

The Pi's serial port needs to be set up. Run this once:

```bash
sudo bash /home/mcgillformulaelectric/Raspberry-Pi-Dashboard/config_scripts/pi_config.sh
```

Then reboot:

```bash
sudo reboot
```

After it comes back up the dashboard should start on its own. If not, run it manually.

### Dashboard crashes or freezes

- Press `Ctrl + Q` to quit. If it doesn't respond, unplug the Pi, wait 10 seconds, plug it back in.
- Once you're back at a terminal, run it manually.
- If it keeps crashing in the same spot, take a photo of the error on screen and send it to me.

### "Permission denied"

Put `sudo` in front of the command:

```bash
sudo python main.py
```

### One number is stuck but the others are moving

Probably a loose wire or unplugged sensor on the car side. The dashboard itself is fine, go check the car.

## Last resort

If nothing above worked, try these in order:

1. Reboot the Pi. Unplug, wait 10 seconds, plug back in.
2. Run `main.py` manually using the steps above.
3. Re-run the setup script and reboot:
   ```bash
   sudo bash /home/mcgillformulaelectric/Raspberry-Pi-Dashboard/config_scripts/pi_config.sh
   sudo reboot
   ```
4. Call me. Take a photo of any error text on the screen before calling, it saves a lot of time.

## One thing to remember

Always start the program with `main.py`. Not any other file. If you only remember one thing from this, remember that.

---

# Part 2 — Developer Guide

This section is for whoever is taking over the dashboard. It covers how the pieces fit together, the UART protocol, what each file does, and how to extend things when you add new signals or pages.

## High-level architecture

There are two sides to this system:

1. **The car side (Nucleo microcontroller).** This is an STM32 running C code. It reads sensor data over CAN, packages it into small UART frames, and sends them out over a wire to the Pi. The code that does this lives in `test/nucleo_test_uart.c` as a reference (the actual flight firmware is in a different repo).

2. **The Pi side (this project).** A Python program reads those UART frames, stores the values in a dictionary, and a Qt-based UI displays them on screen.

Data flow:

```
Car sensors
   v
Nucleo (CAN -> UART frame)
   v
Serial cable
   v
Pi GPIO pins 14/15 (ttyAMA0 / serial0)
   v
uart_store() -> dictionary { object_name: value }
   v
QTimer fires uart_update() every 1 ms
   v
Look up the widgets on the current page
   v
Call the right UI function: bar_resize, update_text, update_progress_bar, toggle_badge
   v
Screen updates
```

## UART protocol

Communication is one-way: Nucleo sends, Pi listens. No handshaking, no reply.

### Frame format

Each frame is exactly **3 bytes**:

| Byte | Name | Meaning |
|------|------|---------|
| 0 | Start byte | Always `0xFF` (255). Used as a sync marker. |
| 1 | ID | A number from 1 to 34 identifying which signal this is. |
| 2 | Value | A single unsigned byte, 0–255. Interpretation depends on the signal. |

### Serial parameters

- Port (Pi): `/dev/serial0` in production. `COM9` is used for local testing on Windows. `/dev/ttyAMA5` is sometimes used as an alternate.
- Baud rate: **115200**
- 8 data bits, no parity, 1 stop bit
- Timeout: 1 second

### Parsing logic (uart_store)

The parser loops while at least 3 bytes are available. It reads 1 byte at a time looking for `0xFF`, and once it finds one, reads the next 2 bytes as the ID + value. Any non-`0xFF` byte where the start byte should be is discarded (framing error, resync).

The value is then written into the shared `uart_data` dictionary keyed by the object name looked up from the `id` dictionary:

```python
self.uart_data[self.id[msg_id]] = value
```

### Signal ID table

IDs are defined in [dashboard/signals_and_pages.py](dashboard/signals_and_pages.py). Current mapping:

| ID | Object name | Page | Widget type |
|----|-------------|------|-------------|
| 1  | frontbrakebar    | page_1 | bar |
| 2  | rearbrakebar     | page_1 | bar |
| 3  | speedbar         | page_1 | bar |
| 4  | throttlebar      | page_1 | bar |
| 5  | front_brake_text | page_1 | text |
| 6  | rear_brake_text  | page_1 | text |
| 7  | speed_text       | page_1 | text |
| 8  | throttle_text    | page_1 | text |
| 9  | valCurrent       | page_2 | text |
| 10 | valVoltage       | page_2 | text |
| 11 | valMinTemp       | page_2 | text |
| 12 | valMaxTemp       | page_2 | text |
| 13 | valMinVolt       | page_2 | text |
| 14 | valMaxVolt       | page_2 | text |
| 15 | badgeCharging    | page_2 | badge |
| 16 | badgeBalancing   | page_2 | badge |
| 17 | dotCharging      | page_2 | led |
| 18 | dotBalancing     | page_2 | led |
| 19 | tireFLValue      | page_10 | text |
| 20 | tireFRValue      | page_10 | text |
| 21 | tireRLValue      | page_10 | text |
| 22 | tireRRValue      | page_10 | text |
| 23 | maxCellValue     | page_10 | text |
| 24 | maxCellBar       | page_10 | progress_bar |
| 25 | speedValue       | page_10 | text |
| 26 | psiFLValue       | page_10 | text |
| 27 | psiFRValue       | page_10 | text |
| 28 | psiRLValue       | page_10 | text |
| 29 | psiRRValue       | page_10 | text |
| 30 | socValue         | page_10 | text |
| 31 | socBar           | page_10 | progress_bar |
| 32 | brakeBar         | page_10 | progress_bar |
| 33 | throttleBar      | page_10 | progress_bar |
| 34 | cardPitMode      | page_10 | badge |

## Project layout

```
Raspberry-Pi-Dashboard/
    main.py                 <- Entry point. Always run this file.
    README.md               <- User-facing quick guide.
    NOTION_DOC.md           <- This document.
    dashboard/
        dashboard_class.py  <- Main Dashboard class, UART loop, window setup.
        dynamic_logic.py    <- Widget update functions (bar, text, progress, badge, led).
        signals_and_pages.py<- Signal ID map, object-name-to-value dict, page-to-widget map.
        object_id.xlsx      <- Human-readable spreadsheet of the ID mapping.
    widgets/
        page_2.py           <- Page-specific helpers, e.g. BMS status badges.
        uart_logic.py       <- Older/experimental UART helper (not used in main flow).
    images/
        image_loader.py     <- Helpers for loading images into QLabels.
        logo.png, logo.jpg  <- Team logo assets.
    untitled/
        mainwindow.ui       <- Qt Designer file. This is the actual screen layout.
        mainwindow_ui.py    <- Auto-generated Python code from the .ui file.
        requirements.txt    <- Python dependencies (PySide6).
        ... other Qt Creator scaffolding ...
    config_scripts/
        pi_config.sh        <- One-time Pi setup: enables UART, disables Bluetooth, kills getty.
        run_app.sh          <- cd + activate venv + python main.py, bundled into one.
        read_port.sh        <- Raw serial byte reader for debugging UART.
    test/
        testUart.py         <- Minimal pyserial listener for poking at UART.
        nucleo_test_uart.c  <- Reference Nucleo firmware that emits test frames.
    main/
        mainwindow_ui.py    <- Older/duplicate of the Qt-generated UI file.
        ui_mainwindow.py    <- Older/duplicate as above.
```

## File-by-file walkthrough

### [main.py](main.py)

The entry point. Three lines of real code:

```python
from dashboard.dashboard_class import Dashboard

if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()
```

Keep it this simple. All logic lives in the `Dashboard` class.

### [dashboard/dashboard_class.py](dashboard/dashboard_class.py)

The core class. Responsibilities:

- Creates the `QApplication` and loads `untitled/mainwindow.ui` via `QUiLoader`.
- Opens the serial port (`pyserial.Serial`).
- Starts a `QTimer` that fires every 1 ms and calls `uart_update()`.
- Sets up keyboard shortcuts for page switching, fullscreen, minimize, quit.
- Hides the mouse cursor with `QCursor(Qt.BlankCursor)`.
- Shows the window fullscreen.

Key methods:

- `__init__` — wires everything up.
- `run()` — enters the Qt event loop.
- `setup_serial()` — opens the port, flushes the input buffer, prints a listening message. If the port fails to open, sets `self.ser = None` and continues so the UI still runs.
- `uart_store()` — reads available bytes, re-syncs on `0xFF`, writes `(id, value)` pairs into `self.uart_data`.
- `uart_update()` — called by the timer. Pulls `uart_store` to drain fresh bytes, looks up the current stacked widget page, iterates the widgets defined for that page in `self.pages`, and dispatches to the right update function by widget type.
- `setup_shortcuts()` — registers `Ctrl+K/J/F/M/Q`.
- `next_page` / `prev_page` / `toggle_fullscreen` — simple wrappers.

Port-selection note: `self.pi_port`, `self.test_port`, and `self.uart5_port` are all defined, but only one is passed to `serial.Serial(...)`. Currently it's hardcoded to `self.test_port` (`COM9`). On the Pi, this needs to be changed to `self.pi_port` (`/dev/serial0`) before deployment. This is a known manual step.

Timer note: the timer fires every 1 ms (`self.timer.start(1)`), not 20 ms as described in the original design doc. This is aggressive but fine on the Pi 4. If you ever see high CPU usage or the UI hitching, ease this back to 5 or 10 ms.

### [dashboard/dynamic_logic.py](dashboard/dynamic_logic.py)

A grab bag of widget-update helpers. Each takes `(window, object_name, value)` and finds the widget by its `objectName` (set in Qt Designer) and updates it.

- `bar_resize(window, object_name, height)` — Resizes a custom bar widget. Looks for a matching "track" widget (same name with `bar` swapped for `Track`) that defines the full extent of the bar. Height is interpreted as a percentage (0–100). The bar grows upward from the bottom of the track by setting `setFixedHeight` and repositioning with `move()`.
- `led_blink(window, object_name, state)` — Toggles a QLabel between red and green via stylesheet. (Note: only the green-state stylesheet is currently a valid CSS string; the off state has a minor bug that needs `color: rgb(...)` wrapping. Low priority since LEDs aren't in active use yet.)
- `update_text(window, object_name, value)` — Stringifies the value and calls `label.setText(...)`.
- `update_table(...)` — Placeholder, not implemented yet.
- `update_progress_bar(window, object_name, value)` — Sets a `QProgressBar` value. Special case: `maxCellBar` is clamped to 60°C max (safety display).
- `toggle_badge(window, object_name, state)` — Flashes a badge on/off at 4 Hz (every 250 ms) via a per-badge `QTimer`. When `state=0`, the timer stops and the badge is hidden.

The `_flash_timers` and `_flash_states` dicts keyed on object name are module-level state. That's fine for this use case since badges are singletons.

### [dashboard/signals_and_pages.py](dashboard/signals_and_pages.py)

Pure data. Three dictionaries:

- `uart_data` — maps `object_name -> value`. This is the live value cache populated by `uart_store`.
- `id` — maps `uart_id (int) -> object_name`. Used to look up where to put a value when a frame arrives.
- `pages` — maps `page_object_name -> { object_name -> widget_type }`. Defines what widgets live on each page and how they should be updated.

Adding a new signal means adding an entry to all three dicts (plus placing the widget in Qt Designer with a matching `objectName`).

### [widgets/page_2.py](widgets/page_2.py)

Currently just has `_set_badge_state` and `pulse_light`, which style the BMS charging/balancing badges with color and text. This is older code that predates the generic `toggle_badge` in `dynamic_logic.py` and could probably be consolidated.

### [widgets/uart_logic.py](widgets/uart_logic.py)

An earlier prototype of the UART handling. Not called from the main flow anymore. Left in the tree for reference. Safe to remove if we do a cleanup pass.

### [images/image_loader.py](images/image_loader.py)

Utility functions for loading image files into QLabels. Three functions:

- `load_image_to_label(label, image_name, keep_aspect_ratio, smooth)` — loads a single image.
- `load_image_map(window, {label_name: image_name})` — batch load, returns per-label success dict.
- `load_page_image(window, page_number, label_name, image_name)` — loads an image onto a QLabel that lives on a specific page of the `stackedWidget`.

Currently only the logo is loaded, and that code path is commented out in `dashboard_class.py`.

### [untitled/mainwindow.ui](untitled/mainwindow.ui)

This is a Qt Designer XML file. Open it in **Qt Designer** (comes with PySide6) to edit the layout visually. Object names set here are what the Python code looks up with `findChild`. Changing an `objectName` silently breaks the signal mapping, so if you rename anything, update `signals_and_pages.py` too.

The main window uses a `QStackedWidget` to flip between pages. Current pages:

- `page_1` — Driver HUD with speed/brake/throttle bars.
- `page_2` — BMS battery status.
- `page_10` — All-in-one overview with tires, SoC, pit mode, and cell temps.

There are other page indices scattered through the file but those three are the ones wired into `pages` in `signals_and_pages.py`.

### [config_scripts/pi_config.sh](config_scripts/pi_config.sh)

One-time Pi setup. Must be run as root: `sudo bash pi_config.sh`. It does:

1. Adds `enable_uart=1` to `/boot/config.txt` (enables the hardware UART).
2. Adds `dtoverlay=disable-bt` (disables Bluetooth so the stable `ttyAMA0` UART is wired to pins 14/15 instead of being used by Bluetooth).
3. Strips `console=serial0,...` out of `/boot/cmdline.txt` (disables the serial login shell that would otherwise hog the port).
4. Stops and disables `serial-getty@ttyAMA0.service` and `serial-getty@serial0.service`.
5. Sets baud rate to 115200 on `/dev/serial0`.
6. Does a 2-second read test on `/dev/serial0`.
7. Verifies all the steps worked and reports pass/fail.

A reboot is required after running this.

### [config_scripts/run_app.sh](config_scripts/run_app.sh)

Three lines: `cd` into the project, activate the venv, run `main.py`. This is what the systemd auto-start service invokes.

### [config_scripts/read_port.sh](config_scripts/read_port.sh)

A raw debug tool. Reads `/dev/serial0` and prints every received byte as a decimal number to the terminal. Useful when you want to verify the Nucleo is actually sending something before worrying about whether the dashboard is parsing it right.

### [test/testUart.py](test/testUart.py)

Minimal pyserial script. Opens `/dev/ttyAMA5` at 115200 and prints 3-byte chunks. For ad-hoc testing when you don't want to spin up the full Qt application.

### [test/nucleo_test_uart.c](test/nucleo_test_uart.c)

Reference firmware for the Nucleo. In the main loop, it cycles through IDs 19–34, sending `[0xFF, id, val]` every 10 ms, bumping `val` by 10 each full pass. This is what you flash onto a Nucleo to simulate the car when the real car isn't around.

## Qt concepts cheat sheet

A few Qt/PySide6 terms that come up constantly:

- **Object name** — a string identifier set in Qt Designer on every widget. The Python code finds widgets by name using `window.findChild(QWidget, "someName")`. If there's a mismatch, `findChild` returns `None`.
- **Stacked widget** — Qt's way of having multiple "pages" in one window. You switch between them with `stackedWidget.setCurrentIndex(n)`.
- **QTimer** — Qt's main-thread-safe timer. It doesn't spawn threads, it just posts events. Perfect for periodic UI refresh.
- **Stylesheet** — CSS-like string that styles widgets. Set with `widget.setStyleSheet("...")`.
- **Ui file** — XML produced by Qt Designer, loaded at runtime with `QUiLoader.load(...)`. We use this instead of compiling the UI to Python, so you can edit the design visually without running `pyside6-uic`.

## Adding a new signal (full checklist)

Say you want to add a new gauge for, I don't know, coolant temperature. Here's everything you need to touch.

### 1. Add the widget in Qt Designer

Open `untitled/mainwindow.ui` in Qt Designer. Drop a widget on the appropriate page. Set a clear `objectName`, e.g. `coolantTempValue`. If it's a bar, also add a matching "track" widget named the same but with `bar` replaced by `Track`.

### 2. Pick the next free UART ID

In `dashboard/signals_and_pages.py`, current IDs go up to 34. Use 35 for the new signal.

### 3. Register the signal

In the same file, add entries to all three dicts:

```python
uart_data = {
    ...,
    "coolantTempValue": 0,
}

id = {
    ...,
    35: "coolantTempValue",
}

pages = {
    "page_2": {
        ...,
        "coolantTempValue": "text",
    },
}
```

### 4. Update the Nucleo firmware

Whoever owns the Nucleo firmware needs to start emitting ID 35 with the right value. The frame is always `[0xFF, 35, value]`.

### 5. Test

With the Nucleo sending, either run `sudo bash config_scripts/read_port.sh` to see raw bytes, or just run `main.py` and flip to the right page. The value should update live.

## Adding a new widget type

If you need something that isn't a bar, progress bar, text label, badge, or LED (say, a 2D meter or a numeric dial):

1. Add a function to `dashboard/dynamic_logic.py` with the signature `your_update_fn(window, object_name, value)`.
2. Add a dispatch branch in `uart_update()` in `dashboard_class.py`:
   ```python
   if widget_type == "your_type":
       your_update_fn(self.window, object_name, value)
   ```
3. Use `"your_type"` in the `pages` dict in `signals_and_pages.py`.

## Auto-start on boot

The Pi is set up to run the dashboard at boot via a systemd service. The actual unit file isn't in this repo — it lives on the Pi itself at `/etc/systemd/system/dashboard.service` and calls `config_scripts/run_app.sh`. If auto-start ever breaks, check:

```bash
sudo systemctl status dashboard.service
```

If it's not enabled:

```bash
sudo systemctl enable dashboard.service
sudo systemctl start dashboard.service
```

## Known quirks and gotchas

- **Port has to be changed manually between dev and prod.** `dashboard_class.py` hardcodes `self.test_port` (`COM9` on Windows). On the Pi, that line needs to be changed to `self.pi_port` (`/dev/serial0`) before deployment. TODO: pick the port automatically based on `os.name` or env var.
- **1 ms timer is very aggressive.** The comment in the code says "every 5ms" but it actually runs at 1 ms. Haven't seen issues but worth knowing.
- **`maxCellBar` is clamped to 60°C.** This is intentional — the progress bar should max out at that temp for safety signalling. Don't remove the clamp.
- **`led_blink` off-state stylesheet is malformed.** Minor cosmetic bug, the off color string isn't wrapped as a CSS property. Worth fixing if you ever start using LED widgets seriously.
- **Bluetooth is disabled on the Pi.** Needed to free `ttyAMA0` for the dashboard's UART. If someone ever wants Bluetooth back, they'd also need to remap the UART to `ttyS0` (the mini-UART, less stable).
- **Serial login shell must stay disabled.** `serial-getty` has a habit of re-enabling itself after updates. If UART stops working, that's the first place to check. `pi_config.sh` handles this, so re-running it fixes it.
- **Git on the Pi almost always fails to pull cleanly.** The standard fix is the hard-reset sequence documented above. Don't try to be clever about merging, just overwrite.

## Tools and dependencies

- Python 3.x (whatever the Pi ships with; tested on 3.11+)
- PySide6 (the only hard dependency; see `untitled/requirements.txt`)
- pyserial (for UART)
- Qt Designer (for editing the `.ui` file visually — installed alongside PySide6)

Install in the venv:

```bash
pip install PySide6 pyserial
```

## Contact

If you're stuck, get in touch with the current dashboard lead. Keep this doc updated as the project changes — future-you will thank present-you.
