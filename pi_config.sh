#!/bin/bash

# Serial UART Setup Script for Raspberry Pi
# Configures GPIO 14/15 (serial0) for USB-to-TTL communication
# Run with: sudo bash pi_config.sh

set -e
chmod +x pi_config.sh

echo "=== Raspberry Pi Serial UART Setup ==="
echo ""

# Check if running as root
# just ensures if u have authority to do sudo commands, i.e. u are the owner
if [ "$EUID" -ne 0 ]; then
  echo "Please run as root: sudo bash $0"
  exit 1
fi

# Step 1: Enable UART in /boot/config.txt
CONFIG="/boot/config.txt"
echo "[1/4] Configuring $CONFIG..."

# Enable UART
# equivalent to: Would you like the serial port hardware to be enabled? -> YES
if ! grep -q "^enable_uart=1" "$CONFIG"; then
  echo "enable_uart=1" >> "$CONFIG"
  echo "  Added enable_uart=1"
else
  echo "  enable_uart=1 already present"
fi

# Disable Bluetooth (frees up the full UART for serial0)
# switching from ttys0 port (unstable) to ttyAMA0 (more stable) 
if ! grep -q "^dtoverlay=disable-bt" "$CONFIG"; then
  echo "dtoverlay=disable-bt" >> "$CONFIG"
  echo "  Added dtoverlay=disable-bt"
else
  echo "  dtoverlay=disable-bt already present"
fi

# Step 2: Configure cmdline.txt — remove serial login shell, keep hardware enabled
# equivalent to doing sudo raspi-config
CMDLINE="/boot/cmdline.txt"
echo "[2/4] Configuring $CMDLINE..."

# Remove console=serial0,... if present (disables login shell on serial)
#equivalent to: Would you like a login shell accessible over serial? -> NO
if grep -q "console=serial0" "$CMDLINE"; then
  sed -i 's/console=serial0,[0-9]* //g' "$CMDLINE"
  echo "  Removed serial0 console (login shell disabled)"
else
  echo "  No serial0 console entry found, skipping"
fi

# Step 3: Disable serial getty service (the agetty process that was locking the port)
# serial-getty is a Linux service that creates a login terminal over a serial port.
#usually we keep disabling it whenever we run the pi, but its response is inconsistent
# idea was that when we do it manually it only temporarily stops it and and resets to default later

echo "[3/4] Disabling serial getty service..."
systemctl stop serial-getty@ttyAMA0.service 2>/dev/null || true #Kill the login process using UART
systemctl disable serial-getty@ttyAMA0.service 2>/dev/null || true #prevents the service from starting automatically at boot
systemctl stop serial-getty@serial0.service 2>/dev/null || true #same thing as above just does it again for serial0, ttyAMA0 -> serial0
systemctl disable serial-getty@serial0.service 2>/dev/null || true
echo "  serial-getty disabled"

# Step 4: Set correct baud rate on serial0
echo "[4/4] Setting baud rate to 115200 on /dev/serial0..."
if [ -e /dev/serial0 ]; then
  stty -F /dev/serial0 115200 cs8 -cstopb -parenb raw
  echo "  Done"
else
  echo "  /dev/serial0 not found yet — will be available after reboot"
fi

# Step 5: send data to serial0 and read from port
# only do when u do feedback loop test
# if u just do echo > /dev/serial0, this is just sending on tx line
if [ -e /dev/serial0 ]; then
    if timeout 2 cat /dev/serial0 | grep -q .; then
        echo "UART working"
    else
        echo "UART FAILED: no data received"
    fi
else
    echo "Skipping UART test: /dev/serial0 not present yet"
fi


# Step 6: Verify UART configuration
echo "[5/5] Verifying UART configuration..."

ok=true

# Check enable_uart
if grep -q "^enable_uart=1" /boot/config.txt; then
  echo "  ✔ UART hardware enabled"
else
  echo "  ✘ enable_uart=1 missing in /boot/config.txt"
  ok=false
fi

# Check serial console removal
if grep -q "console=serial0" /boot/cmdline.txt; then
  echo "  ✘ Serial login console still present in cmdline.txt"
  ok=false
else
  echo "  ✔ Serial login console disabled"
fi

# Check serial-getty service
if systemctl is-enabled serial-getty@serial0.service >/dev/null 2>&1; then
  echo "  ✘ serial-getty service still enabled"
  ok=false
else
  echo "  ✔ serial-getty disabled"
fi

#returns baud rate, could it 115200 or 9600
if [ -e /dev/serial0 ]; then
  echo -n "  Baud rate: "
  stty -F /dev/serial0 | grep -o 'speed [0-9]*' | awk '{print $2}'
else
  echo "  Baud rate: serial0 not available yet"
fi

# Final result
if [ "$ok" = true ]; then
  echo ""
  echo "UART configuration looks correct."
else
  echo ""
  echo "WARNING: Some UART configuration checks failed."
  echo "try doing sudo reboot"
fi

