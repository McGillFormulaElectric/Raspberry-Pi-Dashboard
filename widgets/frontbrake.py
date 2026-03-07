from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer
import serial

ser = None

def setup_serial():
    global ser
    ser = serial.Serial(port='/dev/serial0',
                        baudrate=115200,
                        timeout=0
            )

def uart_input(window):
    global ser
    if ser is None:
        return
    
    if ser.in_waiting > 0:
        raw = ser.read(1)
        if len(raw) == 1:
            value = raw[0]
            print(value)
            print("\n")
            frontbrake_resize(window, value)

def transfer_function(raw_value):
    #mathhhhhhh
    real_value=0

    return real_value

def frontbrake_resize(window, height):
    print("The height here is:",height)
    height = int(3.71*height)
    height = min(371, height)
    bar= window.frontbrakebar
    bottom = bar.y() + bar.height()
    bar.setFixedHeight(height)
    bar.move(bar.x(), bottom - height)


        


        
