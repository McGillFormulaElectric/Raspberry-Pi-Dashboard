from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer

def bar_resize(window, class_name,height):
    '''change size of generic bar'''
    print("The height here is:",height)
    height = int(371*(height/100))
    height = min(371, height)
    bar= window.class_name
    bottom = bar.y() + bar.height()
    bar.setFixedHeight(height)
    bar.move(bar.x(), bottom - height)

def led_blink(window, class_name, bool):
    '''change color of led from red to green, green to red'''
    pass

def update_text(window, class_name, value):
    '''update text on the dashbaord itself'''
    pass

def update_table(window, class_name, row, column):
    '''update value of cell in table'''
    pass