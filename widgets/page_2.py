from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor, QCursor
from PySide6.QtCore import Qt, QFile, QTimer
from PySide6.QtUiTools import QUiLoader
def pulse_light(window):
    indicator_lights = {window.charging_status_light:'', window.balancing_status_light:''} #list of all lights used as indicators
    styles= [] #color, border-radius, etc...
    
    for light in indicator_lights:
        light.styleSheet()
    print(styles)
