from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt, QFile, QTimer
from PySide6.QtUiTools import QUiLoader

from widgets.uart_logic import setup_serial, uart_input
from widgets.page_2 import pulse_light
from images.image_loader import load_page_image


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

        # Load static page images (if matching QLabel names exist in the .ui).
        #self.load_startup_images()

        # Current page
        self.current_page = self.window.stackedWidget.currentIndex()

        # Setup serial
        setup_serial()

        #UART
        self.uart_data = {} #{class_names: value}
        self.id = {} #{id: class_name}
        self.pages = {} #page_num: [bars,led,...]

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

        #dictionnary
    def run(self):
        self.app.exec()

    def update_uart(self):
        uart_input(self.window)
    
    def uart_update(self):
        '''update the values on the given page by looping through the list'''
        pass

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

    def load_startup_images(self):
        """
        Auto-load one image into one specific page only.

        Default behavior:
        - loads images/page_1.jpg
        - into QLabel named 'pageImageLabel' on page_1
        """
        target_page = 1
        # Put your image file inside the images/ folder, then set its name below.
        # Example: image_file = "team_logo.png"
        image_file = "logo.png"
        # Safe no-op when the page/label/image doesn't exist yet.
        load_page_image(self.window, target_page, "label_13", image_file)

