from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer


def bar_resize(window, object_name, height):
    '''Change size of generic bar'''
    bar = window.findChild(QWidget, object_name)
    if bar is None:
        print(f"[bar_resize] Widget not found: {object_name}")
        return

    track_name = object_name.replace("_bar", "_track")
    track = window.findChild(QWidget, track_name)
    if track is None:
        print(f"[bar_resize] Track not found: {track_name}")
        return

    max_height = track.height()
    new_height = int(max_height * (height / 100))
    new_height = max(0, min(max_height, new_height))

    bottom = track.y() + track.height()
    bar.setFixedHeight(new_height)
    bar.move(bar.x(), bottom - new_height)

def led_blink(window, object_name, bool):
    '''change color of led from red to green, green to red'''
    pass

def update_text(window, object_name, value):
    '''Update a QLabel on the dashboard by objectName'''
    label = window.findChild(QLabel, object_name)
    if label is not None:
        label.setText(str(value))

def update_table(window, object_name, row, column):
    '''update value of cell in table'''
    pass
