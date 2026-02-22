from PySide6.QtWidgets import QFrame, QApplication, QMainWindow, QWidget
from PySide6.QtGui import QPainter, QColor
from PySide6.QtCore import QTimer
import serial


def frontbrake_resize(window, height):
    height = min(400, height) #400 gotten from max possible y value in qt creator
    bar= window.frontbrakebar #custom object name given in creator
    
    bottom = bar.y() + bar.height() #find bottom of bar
    
    bar.setFixedHeight(height) #set to desired height
    
    bar.move(bar.x(), bottom - height) #move it down to bottom. needed because you can only control bottom of bar, not the top
                                        


    

    

        
        


        
