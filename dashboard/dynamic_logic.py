from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget, QLabel, QProgressBar
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer


def bar_resize(window, object_name, height):
    '''Change size of generic bar'''
    # findChild(QWidget, object_name) searches window's descendant widgets for one matching the given type and name
    bar = window.findChild(QWidget, object_name)
    if bar is None:
        #print(f"[bar_resize] Widget not found: {object_name}")
        return

    track_name = object_name.replace("bar", "Track")
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
def led_blink(window, object_name, state):
    '''change color of led from red to green, green to red, state is 0 for off/red and 1 for on/green'''
    label = window.findChild(QLabel, object_name)
    if label is not None:
        if state:
            label.setStyleSheet("color: rgb(14, 255, 54);")
        else:
            label.setStyleSheet("color: rgb(255, 5, 38);")
        return
    # Fallback: QWidget-based LED (uses background-color instead of color)
    widget = window.findChild(QWidget, object_name)
    if widget is not None:
        if state:
            widget.setStyleSheet(f"#{object_name} {{ background-color: rgb(14, 255, 54); border-radius: 15px; }}")
        else:
            widget.setStyleSheet(f"#{object_name} {{ background-color: rgb(255, 5, 38); border-radius: 15px; }}")





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

def update_progress_bar(window, object_name, value):
    if object_name == "maxCellBar" and value>60:
        value=60

    label = window.findChild(QProgressBar, object_name)
    if label is not None:
        print(f"Progress Bar {object_name} found")
        label.setValue(value)
    else:
        print(f"{object_name} Progress Bar Not Found")








_flash_timers = {}
_flash_states = {}

def toggle_badge(window, object_name, state):
    '''flash badge when state==1, hide when state==0'''
    badge = window.findChild(QFrame, object_name)
    if badge is None:
        return

    if not state:
        if object_name in _flash_timers:
            _flash_timers[object_name].stop()
        _flash_states[object_name] = False
        badge.setVisible(False)
        return

    if object_name in _flash_timers and _flash_timers[object_name].isActive():
        return

    _flash_states[object_name] = False

    def _tick():
        _flash_states[object_name] = not _flash_states[object_name]
        badge.setVisible(_flash_states[object_name])

    timer = QTimer()
    timer.timeout.connect(_tick)
    timer.start(250)
    _flash_timers[object_name] = timer