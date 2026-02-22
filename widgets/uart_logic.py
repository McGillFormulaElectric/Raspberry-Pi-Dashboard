import serial
from widgets.frontbrake import frontbrake_resize


def setup_serial():
    global ser
    ser = serial.Serial(port="/dev/serial0", baudrate=115200, timeout=1) #port = "/dev/serial0"

def uart_input(window):
    global ser
    if ser.in_waiting:
        value = ser.readline.decode().strip()
        frontbrake_resize(window, value) #transfer_function(value)

def transfer_function(raw_value):
    #mathhhhhhh

    return raw_value