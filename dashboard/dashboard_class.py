from PySide6 import QtCore, QtGui, QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QCursor
from PySide6.QtCore import Qt, QFile, QTimer
from PySide6.QtUiTools import QUiLoader
from dashboard.dynamic_logic import bar_resize, update_text, find_track_widget
from widgets.page_2 import pulse_light
from images.image_loader import load_page_image
import serial
from dashboard.signals_and_pages import uart_data, pages, id


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

        #UART
        #self.ser = None
        self.pi_port = '/dev/serial0'
        self.test_port = 'COM4'
        self.uart5_port = '/dev/ttyAMA5'
        self.ser = serial.Serial(
                port=self.uart5_port,
                baudrate=115200,
                timeout=1,
            )


        self.uart_data = uart_data #{class_names: value}
        self.id = id #{id: class_name}
        self.pages = pages #page_object_name: {object_name: widget_type}
        self.validate_page_mappings()

        # Timer for UART
        self.setup_serial() #opens uart port
        self.timer = QTimer()
        self.timer.timeout.connect(self.uart_update) #main UART Loop
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
    def setup_serial(self):
        try:
            self.ser.reset_input_buffer()
            print(f"listening on {self.uart5_port}...")
        except (serial.SerialException, OSError) as exc:
            self.ser = None
            print(f"[setup_serial] Failed to open {self.test_port}: {exc}")

    def uart_store(self):
        '''stores values from uart into the dictionnary'''
        if self.ser is None:
            return

        try:
            while self.ser.in_waiting >= 3:
                # look for start byte
                start = self.ser.read(1)
                if start[0] != 0xFF:
                    print(f"[uart_store] Framing error, discarding byte: {start[0]}")
                    continue  # discard and re-sync

                raw = self.ser.read(2)
                if len(raw) == 2:
                    msg_id, value = raw[0], raw[1]
                    if msg_id in self.id:
                        object_name = self.id[msg_id]
                        self.uart_data[object_name] = value
                    else:
                        print(f"[uart_store] Unknown ID: {msg_id}")
        except (serial.SerialException, OSError) as exc:
            print(f"[uart_store] Serial read failed: {exc}")
            try:
                self.ser.close()
            except (serial.SerialException, OSError):
                pass
            self.ser = None

    
    def uart_update(self):
        '''Update the values on the given page by looping through the dicts'''
        self.uart_store()
        current_page = self.window.stackedWidget.currentWidget()
        if current_page is None:
            return

        current_page_name = current_page.objectName()

        if current_page_name not in self.pages:
            return

        for object_name, widget_type in self.pages[current_page_name].items():
            if object_name in self.uart_data:
                value = self.uart_data.get(object_name, 0)
            else:
                continue

            if widget_type == "bar":
                bar_resize(self.window, object_name, value)
            if widget_type == "text":
                update_text(self.window, object_name, value)
                bar_resize(current_page, object_name, value)
            elif widget_type == "text":
                update_text(current_page, object_name, value)

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

    def validate_page_mappings(self):
        '''Log missing page/widget mappings so UI drift is visible at startup.'''
        for page_name, widgets in self.pages.items():
            page = self.window.findChild(QtWidgets.QWidget, page_name)
            if page is None:
                print(f"[validate_page_mappings] Page not found: {page_name}")
                continue

            for object_name, widget_type in widgets.items():
                if widget_type == "text":
                    widget = page.findChild(QtWidgets.QLabel, object_name)
                else:
                    widget = page.findChild(QtWidgets.QWidget, object_name)

                if widget is None:
                    print(
                        f"[validate_page_mappings] {widget_type} widget not found on "
                        f"{page_name}: {object_name}"
                    )
                    continue

                if widget_type == "bar":
                    track, track_name = find_track_widget(page, object_name)
                    if track is None:
                        print(
                            f"[validate_page_mappings] Track not found on {page_name} "
                            f"for {object_name}"
                        )
                    elif track.parent() is not page:
                        print(
                            f"[validate_page_mappings] Track {track_name} for {object_name} "
                            f"is nested unexpectedly on {page_name}"
                        )

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

