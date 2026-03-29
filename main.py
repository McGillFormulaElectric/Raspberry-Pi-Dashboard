from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor, QCursor
from PySide6.QtCore import Qt, QFile, QTimer
from PySide6.QtUiTools import QUiLoader
from widgets.frontbrake import setup_serial, uart_input
import random
from widgets.page_2 import pulse_light
from dashboard_class import Dashboard



if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()






'''
#from widgets.frontbrake import frontbrakebar


app = QApplication()
loader = QUiLoader()
ui_file = QFile("untitled/mainwindow.ui")
 
ui_file.open(QFile.ReadOnly)

window = loader.load(ui_file)
ui_file.close()
#event loop -----begin --------
print("hello")
setup_serial()
timer = QTimer()
timer.timeout.connect(lambda:uart_input(window))
pulse_light(window)
timer.start(5)
#event loop -----end --------

def toggle_fullscreen():
    if window.isFullScreen():
        window.showNormal()
    else:
        window.showFullScreen()

def next_page():
    index = window.stackedWidget.currentIndex()
    count = window.stackedWidget.count()
    window.stackedWidget.setCurrentIndex((index + 1) % count)

def prev_page():
    index = window.stackedWidget.currentIndex()
    count = window.stackedWidget.count()
    window.stackedWidget.setCurrentIndex((index - 1) % count)


QtGui.QShortcut(QtGui.QKeySequence("Ctrl+K"), window, activated=next_page) #flip through pages
QtGui.QShortcut(QtGui.QKeySequence("Ctrl+J"), window, activated=prev_page)
        
QtGui.QShortcut(QtGui.QKeySequence("Ctrl+M"), window, activated=window.showMinimized)
QtGui.QShortcut(QtGui.QKeySequence("Ctrl+F"), window, activated=toggle_fullscreen)
QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), window, activated=QtWidgets.QApplication.quit)

app.setOverrideCursor(QCursor(Qt.BlankCursor))

#fake_uart()
window.show()
window.showFullScreen()
app.exec()
        
'''

