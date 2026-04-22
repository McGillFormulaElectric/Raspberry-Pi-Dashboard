# Raspberry Pi Dashboard

This is a guide for running the car's dashboard on the Raspberry Pi. It's written so anyone on the team can do it, even if you've never used a Pi or written any code. If I'm not around and something breaks, this should cover most of what you need.

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

## What's in the folders

You don't need to touch any of this, but if you're curious:

- `main.py` is the file you run. Always start here.
- `dashboard/` is the brain of the dashboard (screen logic and UART reading).
- `widgets/` has individual screen elements like blinking lights.
- `untitled/mainwindow.ui` is the visual design of the screen.
- `config_scripts/` has the Pi setup scripts (`pi_config.sh`, `run_app.sh`).
- `images/` holds logos and static pictures.
- `test/` is for me, safe to ignore.

## One thing to remember

Always start the program with `main.py`. Not any other file. If you only remember one thing from this, remember that.
