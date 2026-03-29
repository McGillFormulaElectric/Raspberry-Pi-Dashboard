from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer
import serial
import re

ser = None
pi_port = '/dev/serial0'
test_port = 'COM4'
uart5_port = '/dev/ttyAMA5'

# Accumulated receive buffer for partial packets
_rx_buf = ''

def setup_serial():
    global ser
    ser = serial.Serial(port=uart5_port,
                        baudrate=115200,
                        timeout=1
            )
    ser.reset_input_buffer()
    print("listening...")

# Matches id,value pairs in the no-delimiter stream "1,752,803,504,60".
# Non-greedy value digit match with lookahead for next id or end-of-string.
_PAIR_RE = re.compile(r'([1-4]),(\d+?)(?=[1-4],|$)')

def uart_input(window):
    global ser, _rx_buf
    if ser is None:
        return

    waiting = ser.in_waiting
    if waiting <= 0:
        return

    chunk = ser.read(waiting).decode('ascii', errors='ignore')
    _rx_buf += chunk
    print(f"[uart] raw: {repr(_rx_buf)}")

    matches = list(_PAIR_RE.finditer(_rx_buf))
    print(f"[uart] matches: {[(m.group(1), m.group(2)) for m in matches]}")
    if not matches:
        # Keep buffer bounded to avoid unbounded growth on garbage data
        if len(_rx_buf) > 64:
            _rx_buf = _rx_buf[-32:]
        return

    for m in matches:
        id_ = int(m.group(1))
        value = int(m.group(2))
        value = max(0, min(100, value))

        if id_ == 1:
            throttle_resize(window, value)
        elif id_ == 3:
            frontbrake_resize(window, value)

    # Discard everything up through the last matched character
    last_end = matches[-1].end()
    _rx_buf = _rx_buf[last_end:]

def _resize_bar(bar, pct, max_height=371):
    height = int(max_height * (pct / 100))
    height = min(max_height, height)
    bottom = bar.y() + bar.height()
    bar.setFixedHeight(height)
    bar.move(bar.x(), bottom - height)

def frontbrake_resize(window, pct):
    print("brake1:", pct)
    _resize_bar(window.frontbrakebar, pct)

def throttle_resize(window, pct):
    print("throttle1:", pct)
    _resize_bar(window.throttlebar, pct)


        


        
