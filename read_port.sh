#!/bin/bash

# read_port.sh
# Reads from /dev/serial0 and prints each byte as a decimal number
# Run with: sudo bash read_serial_dec.sh

DEVICE="/dev/serial0"
BAUD=115200

if [ "$EUID" -ne 0 ]; then
  echo "Please run as root: sudo bash $0"
  exit 1
fi

if [ ! -e "$DEVICE" ]; then
  echo "Error: $DEVICE not found"
  exit 1
fi

# Set port to raw mode so bytes come through unmodified
stty -F "$DEVICE" "$BAUD" cs8 -cstopb -parenb raw -echo

echo "Reading from $DEVICE at $BAUD baud. Ctrl+C to stop."
echo "---"

# Read one byte at a time and print as decimal
while IFS= read -r -d '' -n 1 char; do
  printf '%d ' "$(printf '%d' "'$char")"
done < "$DEVICE"