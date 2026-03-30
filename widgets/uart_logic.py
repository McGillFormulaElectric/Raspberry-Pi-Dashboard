from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer
import serial
from dashboard.dynamic_logic import bar_resize

ser = None
pi_port = '/dev/serial0'
test_port = 'COM4'
uart5_port = '/dev/ttyAMA5'
def setup_serial():
    global ser
    ser = serial.Serial(port=test_port,
                        baudrate=115200,
                        timeout=1
            )
    ser.reset_input_buffer()
    print("listening...")

def uart_input(window):
    global ser
    if ser is None:
        return
    
    if ser.in_waiting > 0:
        raw = ser.read(1)
        if len(raw) == 1:
            value = raw[0]
            print(value)
            print("\r\n")
            bar_resize(window, value)
def uart_store(window):
    '''store incoming uart values in a dictionnary'''
    pass

        


        
