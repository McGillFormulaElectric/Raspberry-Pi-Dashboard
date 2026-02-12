from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer
import serial


def setup_serial():
    global ser
    ser = serial.Serial(port="COM3", baudrate=115200, timeout=0)

def transfer_function(raw_value):
    #mathhhhhhh
    real_value=0

    return real_value

def frontbrake_resize(window, height):
    height = min(700, height)
    bar= window.frontbrakebar
    bottom = bar.y() + bar.height()
    bar.setFixedHeight(height)
    bar.move(bar.x(), bottom - height)

def uart_input(window):
    global ser
    if ser.in_waiting:
        value = ser.readline.decode().strip()
        frontbrake_resize(window, transfer_function(value))
    

    

        
        


        
