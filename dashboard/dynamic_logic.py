from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget, QLabel
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer


def bar_resize(window, object_name, height):
    '''Change size of generic bar'''
    # findChild(QWidget, object_name) searches window's descendant widgets for one matching the given type and name
    bar = window.findChild(QWidget, object_name)
    if bar is None:
        #print(f"[bar_resize] Widget not found: {object_name}")
        return

    track_name = object_name.replace("_bar", "_track")
    # findChild(QWidget, track_name) fetches the track widget that defines the full bar area
    track = window.findChild(QWidget, track_name)
    if track is None:
        print(f"[bar_resize] Track not found: {track_name}")
        return

    max_height = track.height()
    new_height = int(max_height * (height / 100))
    new_height = max(0, min(max_height, new_height))

    bottom = track.y() + track.height()
    # setFixedHeight(new_height) locks the bar widget to exactly this pixel height, ignoring any layout stretch
    bar.setFixedHeight(new_height)
    # move(x, y) sets the widget's top-left position; using bottom - new_height keeps the bar's bottom edge fixed to the track's bottom
    bar.move(bar.x(), bottom - new_height)

# Toggle an LED-style widget between on and off colors.
def led_blink(window, object_name, bool):
    '''change color of led from red to green, green to red'''
    # Leave the implementation empty for now.
    pass

# Update the text shown by a named label widget.
def update_text(window, object_name, value):
    '''Update a QLabel on the dashboard by objectName'''
    # Qt boilerplate: `findChild(QLabel, object_name)` finds the label widget with this object name.
    label = window.findChild(QLabel, object_name)
    # Only update the text when the label exists.
    if label is not None:
        # Qt boilerplate: `setText(str(value))` converts the value to text and updates what the label shows on screen.
        print(f"[update_text] label found: {object_name}")
        label.setText(str(value))
    else:
        print(f"[update_text] label not found: {object_name}")

# Update a value inside a dashboard table widget.
def update_table(window, object_name, row, column):
    '''update value of cell in table'''
    # Leave the implementation empty for now.
    pass
