from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt, QFile, QTimer
from PySide6.QtUiTools import QUiLoader

from widgets.frontbrake import setup_serial, uart_input
from widgets.page_2 import pulse_light


class Dashboard:

    def __init__(self):

        # Application
        self.app = QApplication()

        # Load UI
        loader = QUiLoader()
        ui_file = QFile("untitled/mainwindow.ui")
        ui_file.open(QFile.ReadOnly)

        self.window = loader.load(ui_file)
        ui_file.close()

        # Setup serial
        setup_serial()

        # Timer for UART
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_uart)
        self.timer.start(5)

        # Shortcuts
        self.setup_shortcuts()

        # Hide cursor
        self.app.setOverrideCursor(QCursor(Qt.BlankCursor))

        # Show window
        self.window.show()
        self.window.showFullScreen()
    def run(self):
        self.app.exec()

    def update_uart(self):
        uart_input(self.window)

    def toggle_fullscreen(self):
        if self.window.isFullScreen():
            self.window.showNormal()
        else:
            self.window.showFullScreen()

    def next_page(self):
        index = self.window.stackedWidget.currentIndex()
        count = self.window.stackedWidget.count()
        self.window.stackedWidget.setCurrentIndex((index + 1) % count)

    def prev_page(self):
        index = self.window.stackedWidget.currentIndex()
        count = self.window.stackedWidget.count()
        self.window.stackedWidget.setCurrentIndex((index - 1) % count)

    def setup_shortcuts(self):

        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+K"), self.window, activated=self.next_page)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+J"), self.window, activated=self.prev_page)

        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+M"), self.window, activated=self.window.showMinimized)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+F"), self.window, activated=self.toggle_fullscreen)
        QtGui.QShortcut(QtGui.QKeySequence("Ctrl+Q"), self.window, activated=QtWidgets.QApplication.quit)


if __name__ == "__main__":
    dashboard = Dashboard()
    dashboard.run()