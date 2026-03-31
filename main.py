from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor, QCursor
from PySide6.QtCore import Qt, QFile, QTimer
from PySide6.QtUiTools import QUiLoader
from widgets.uart_logic import setup_serial, uart_input, bar_resize
import random
from widgets.page_2 import pulse_light
from dashboard.dashboard_class import Dashboard



if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()