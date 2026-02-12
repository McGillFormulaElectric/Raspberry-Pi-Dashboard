from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt, QFile, QTimer
from PySide6.QtUiTools import QUiLoader
from widgets.frontbrake import frontbrake_resize, uart_input, transfer_function, setup_serial
import random


#from widgets.frontbrake import frontbrakebar


app = QApplication()
loader = QUiLoader()
ui_file = QFile("untitled/mainwindow.ui")
 
ui_file.open(QFile.ReadOnly)

window = loader.load(ui_file)
#event loop -----begin --------

setup_serial()
timer = QTimer()
timer.timeout.connect(lambda:uart_input(window))
timer.start(5)
#event loop -----begin --------
'''
# testing uart
current_value = 0
direction = 1

def fake_uart():
    global current_value, direction

    current_value += 10 * direction

    if current_value >= 700:
        direction = -1
    if current_value <= 0:
        direction = 1

    frontbrake_resize(window, current_value)

timer = QTimer()
timer.timeout.connect(fake_uart)
timer.start(30)
ui_file.close()
#end test 
'''

window.show()
#window.showFullScreen()
app.exec()
        