from PySide6.QtWidgets import QFrame, QApplication, QMainWindow
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import Qt
import sys
class FrontBrakeBar(QFrame):
    def __innit__(self, parent=None):
        super().__init__(parent)
        self.value=0
    
    def setValue(self,value):
        self.value=max(0, min(100, value))
        self.update()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        w = self.width()
        h = self.height()

        # ----- Bar ------
        fill_height = int(h*(self.value/100))
        fill_top = h- fill_height

        painter.setBrush(QColor(0,120,255))
        painter.setPen(Qt.NoPen)
        painter.drawRect(0,fill_top, w, fill_height)

        # ----- Moving Number ----
        text = str(self.value)
        painter.setPen(Qt.white)

        text_y = fill_top - 6
        text_y = max(12, text_y)

        painter.drawText(0, text_y, w, 20, Qt.AlignCenter, text)
        
