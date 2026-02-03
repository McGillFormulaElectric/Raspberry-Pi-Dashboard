from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import sys
import serial
from widgets.frontbrake import FrontBrakeBar
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        loader = QUiLoader()
        loader.registerCustomWidget(FrontBrakeBar)

        ui_path = os.path.join(os.path.dirname(__file__), "mainwindow.ui")
        ui_file = QFile(ui_path)

        if not ui_file.open(QFile.ReadOnly):
            raise RuntimeError(f"Could not open UI file: {ui_path}")

        self.ui = loader.load(ui_file, self)
        ui_file.close()

        self.frontbrake = self.ui.findChild(FrontBrakeBar, "frontbrake")
        self.frontbrake.setValue(60)


app = QApplication(sys.argv)
window = MainWindow()
window.show()
sys.exit(app.exec())
