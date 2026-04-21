# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QProgressBar, QSizePolicy,
    QStackedWidget, QStatusBar, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setWindowOpacity(1.000000000000000)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.actionsettings = QAction(MainWindow)
        self.actionsettings.setObjectName(u"actionsettings")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 20, 771, 441))
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.accentStripe = QWidget(self.page_1)
        self.accentStripe.setObjectName(u"accentStripe")
        self.accentStripe.setGeometry(QRect(0, 0, 4, 22))
        self.accentStripe.setStyleSheet(u"background-color: rgb(232, 0, 45);")
        self.titleLabel = QLabel(self.page_1)
        self.titleLabel.setObjectName(u"titleLabel")
        self.titleLabel.setGeometry(QRect(12, 0, 300, 22))
        self.titleLabel.setStyleSheet(u"color: rgb(255, 255, 255); font-family: \"Courier New\"; font-size: 9px; background-color: transparent;")
        self.headerLine = QFrame(self.page_1)
        self.headerLine.setObjectName(u"headerLine")
        self.headerLine.setGeometry(QRect(0, 26, 771, 1))
        self.headerLine.setStyleSheet(u"background-color: rgb(26, 26, 26);")
        self.headerLine.setFrameShape(QFrame.Shape.HLine)
        self.frontbrakeTrack = QWidget(self.page_1)
        self.frontbrakeTrack.setObjectName(u"frontbrakeTrack")
        self.frontbrakeTrack.setGeometry(QRect(0, 68, 145, 310))
        self.frontbrakeTrack.setStyleSheet(u"background-color: rgb(10, 10, 10); border: 1px solid rgb(28, 28, 28);")
        self.frontbrakebar = QWidget(self.page_1)
        self.frontbrakebar.setObjectName(u"frontbrakebar")
        self.frontbrakebar.setEnabled(True)
        self.frontbrakebar.setGeometry(QRect(1, 223, 143, 155))
        self.frontbrakebar.setStyleSheet(u"background-color: rgb(86, 138, 219);")
        self.frontBrakeValueTop = QLabel(self.page_1)
        self.frontBrakeValueTop.setObjectName(u"frontBrakeValueTop")
        self.frontBrakeValueTop.setGeometry(QRect(33, 38, 80, 26))
        self.frontBrakeValueTop.setStyleSheet(u"color: rgb(86, 138, 219); font-family: \"Courier New\"; font-size: 18px; font-weight: bold; background-color: transparent;")
        self.frontBrakeValueTop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label = QLabel(self.page_1)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(12, 390, 120, 28))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255); font-family: \"Courier New\"; font-size: 13px; font-weight: bold; background-color: transparent;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rearbrakeTrack = QWidget(self.page_1)
        self.rearbrakeTrack.setObjectName(u"rearbrakeTrack")
        self.rearbrakeTrack.setGeometry(QRect(151, 68, 145, 310))
        self.rearbrakeTrack.setStyleSheet(u"background-color: rgb(10, 10, 10); border: 1px solid rgb(28, 28, 28);")
        self.rearbrakebar = QWidget(self.page_1)
        self.rearbrakebar.setObjectName(u"rearbrakebar")
        self.rearbrakebar.setEnabled(True)
        self.rearbrakebar.setGeometry(QRect(152, 274, 143, 104))
        self.rearbrakebar.setStyleSheet(u"background-color: rgb(58, 101, 176);")
        self.rearBrakeValueTop = QLabel(self.page_1)
        self.rearBrakeValueTop.setObjectName(u"rearBrakeValueTop")
        self.rearBrakeValueTop.setGeometry(QRect(184, 38, 80, 26))
        self.rearBrakeValueTop.setStyleSheet(u"color: rgb(58, 101, 176); font-family: \"Courier New\"; font-size: 18px; font-weight: bold; background-color: transparent;")
        self.rearBrakeValueTop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(self.page_1)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(164, 390, 120, 28))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255); font-family: \"Courier New\"; font-size: 13px; font-weight: bold; background-color: transparent;")
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.speedTrack = QWidget(self.page_1)
        self.speedTrack.setObjectName(u"speedTrack")
        self.speedTrack.setGeometry(QRect(302, 68, 145, 310))
        self.speedTrack.setStyleSheet(u"background-color: rgb(10, 10, 10); border: 1px solid rgb(28, 28, 28);")
        self.speedbar = QWidget(self.page_1)
        self.speedbar.setObjectName(u"speedbar")
        self.speedbar.setEnabled(True)
        self.speedbar.setGeometry(QRect(303, 172, 143, 206))
        self.speedbar.setStyleSheet(u"background-color: rgb(232, 0, 45);")
        self.speedValueTop = QLabel(self.page_1)
        self.speedValueTop.setObjectName(u"speedValueTop")
        self.speedValueTop.setGeometry(QRect(335, 38, 80, 26))
        self.speedValueTop.setStyleSheet(u"color: rgb(232, 0, 45); font-family: \"Courier New\"; font-size: 18px; font-weight: bold; background-color: transparent;")
        self.speedValueTop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_3 = QLabel(self.page_1)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(315, 390, 120, 28))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255); font-family: \"Courier New\"; font-size: 13px; font-weight: bold; background-color: transparent;")
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.throttleTrack = QWidget(self.page_1)
        self.throttleTrack.setObjectName(u"throttleTrack")
        self.throttleTrack.setGeometry(QRect(459, 68, 145, 310))
        self.throttleTrack.setStyleSheet(u"background-color: rgb(10, 10, 10); border: 1px solid rgb(28, 28, 28);")
        self.throttlebar = QWidget(self.page_1)
        self.throttlebar.setObjectName(u"throttlebar")
        self.throttlebar.setEnabled(True)
        self.throttlebar.setGeometry(QRect(460, 138, 143, 240))
        self.throttlebar.setStyleSheet(u"background-color: rgb(111, 154, 33);")
        self.throttleValueTop = QLabel(self.page_1)
        self.throttleValueTop.setObjectName(u"throttleValueTop")
        self.throttleValueTop.setGeometry(QRect(492, 38, 80, 26))
        self.throttleValueTop.setStyleSheet(u"color: rgb(111, 154, 33); font-family: \"Courier New\"; font-size: 18px; font-weight: bold; background-color: transparent;")
        self.throttleValueTop.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_4 = QLabel(self.page_1)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(466, 390, 120, 28))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255); font-family: \"Courier New\"; font-size: 13px; font-weight: bold; background-color: transparent;")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.statsPanel = QWidget(self.page_1)
        self.statsPanel.setObjectName(u"statsPanel")
        self.statsPanel.setGeometry(QRect(612, 128, 148, 250))
        self.statsPanel.setStyleSheet(u"background-color: rgb(13, 13, 13); border: 1px solid rgb(26, 26, 26); border-radius: 2px;")
        self.front_brake_text_2 = QLabel(self.statsPanel)
        self.front_brake_text_2.setObjectName(u"front_brake_text_2")
        self.front_brake_text_2.setGeometry(QRect(30, 30, 21, 32))
        self.front_brake_text_2.setStyleSheet(u"color: rgb(86, 138, 219); font-family: \"Courier New\"; font-size: 22px; font-weight: bold; background-color: transparent;")
        self.speed_text_2 = QLabel(self.statsPanel)
        self.speed_text_2.setObjectName(u"speed_text_2")
        self.speed_text_2.setGeometry(QRect(40, 180, 61, 24))
        self.speed_text_2.setStyleSheet(u"color: rgb(232, 0, 45); font-family: \"Courier New\"; font-size: 18px; font-weight: bold; background-color: transparent;")
        self.throttle_text_2 = QLabel(self.statsPanel)
        self.throttle_text_2.setObjectName(u"throttle_text_2")
        self.throttle_text_2.setGeometry(QRect(40, 220, 21, 24))
        self.throttle_text_2.setStyleSheet(u"color: rgb(111, 154, 33); font-family: \"Courier New\"; font-size: 18px; font-weight: bold; background-color: transparent;")
        self.statFBLabel = QLabel(self.page_1)
        self.statFBLabel.setObjectName(u"statFBLabel")
        self.statFBLabel.setGeometry(QRect(612, 140, 136, 18))
        self.statFBLabel.setStyleSheet(u"color: rgb(255, 255, 255); font-family: \"Courier New\"; font-size: 12px; font-weight: bold; background-color: transparent;")
        self.front_brake_text = QLabel(self.page_1)
        self.front_brake_text.setObjectName(u"front_brake_text")
        self.front_brake_text.setGeometry(QRect(612, 162, 21, 32))
        self.front_brake_text.setStyleSheet(u"color: rgb(86, 138, 219); font-family: \"Courier New\"; font-size: 22px; font-weight: bold; background-color: transparent;")
        self.statLine1 = QFrame(self.page_1)
        self.statLine1.setObjectName(u"statLine1")
        self.statLine1.setGeometry(QRect(612, 200, 136, 1))
        self.statLine1.setStyleSheet(u"background-color: rgb(26, 26, 26);")
        self.statLine1.setFrameShape(QFrame.Shape.HLine)
        self.statRBLabel = QLabel(self.page_1)
        self.statRBLabel.setObjectName(u"statRBLabel")
        self.statRBLabel.setGeometry(QRect(612, 212, 136, 18))
        self.statRBLabel.setStyleSheet(u"color: rgb(255, 255, 255); font-family: \"Courier New\"; font-size: 12px; font-weight: bold; background-color: transparent;")
        self.rear_brake_text = QLabel(self.page_1)
        self.rear_brake_text.setObjectName(u"rear_brake_text")
        self.rear_brake_text.setGeometry(QRect(612, 234, 31, 32))
        self.rear_brake_text.setStyleSheet(u"color: rgb(58, 101, 176); font-family: \"Courier New\"; font-size: 22px; font-weight: bold; background-color: transparent;")
        self.statLine2 = QFrame(self.page_1)
        self.statLine2.setObjectName(u"statLine2")
        self.statLine2.setGeometry(QRect(612, 274, 136, 1))
        self.statLine2.setStyleSheet(u"background-color: rgb(26, 26, 26);")
        self.statLine2.setFrameShape(QFrame.Shape.HLine)
        self.statSPLabel = QLabel(self.page_1)
        self.statSPLabel.setObjectName(u"statSPLabel")
        self.statSPLabel.setGeometry(QRect(612, 286, 80, 18))
        self.statSPLabel.setStyleSheet(u"color: rgb(255, 255, 255); font-family: \"Courier New\"; font-size: 12px; font-weight: bold; background-color: transparent;")
        self.speed_text = QLabel(self.page_1)
        self.speed_text.setObjectName(u"speed_text")
        self.speed_text.setGeometry(QRect(612, 308, 21, 24))
        self.speed_text.setStyleSheet(u"color: rgb(232, 0, 45); font-family: \"Courier New\"; font-size: 18px; font-weight: bold; background-color: transparent;")
        self.statTHLabel = QLabel(self.page_1)
        self.statTHLabel.setObjectName(u"statTHLabel")
        self.statTHLabel.setGeometry(QRect(612, 332, 80, 18))
        self.statTHLabel.setStyleSheet(u"color: rgb(255, 255, 255); font-family: \"Courier New\"; font-size: 12px; font-weight: bold; background-color: transparent;")
        self.throttle_text = QLabel(self.page_1)
        self.throttle_text.setObjectName(u"throttle_text")
        self.throttle_text.setGeometry(QRect(612, 352, 21, 24))
        self.throttle_text.setStyleSheet(u"color: rgb(111, 154, 33); font-family: \"Courier New\"; font-size: 18px; font-weight: bold; background-color: transparent;")
        self.label_13 = QLabel(self.page_1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(610, 20, 151, 101))
        self.label_13.setStyleSheet(u"background-image: url(:/logo.png);")
        self.label_13.setPixmap(QPixmap(u"untitled/logo.png"))
        self.label_13.setScaledContents(True)
        self.front_brake_text_3 = QLabel(self.page_1)
        self.front_brake_text_3.setObjectName(u"front_brake_text_3")
        self.front_brake_text_3.setGeometry(QRect(650, 230, 21, 32))
        self.front_brake_text_3.setStyleSheet(u"color: rgb(86, 138, 219); font-family: \"Courier New\"; font-size: 22px; font-weight: bold; background-color: transparent;")
        self.stackedWidget.addWidget(self.page_1)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"\n"
"    QWidget#page_3 {\n"
"      background-color: #000000;\n"
"    }\n"
"    QWidget#batteryMonitorPage {\n"
"      background-color: #000000;\n"
"    }\n"
"    QFrame#packCard, QFrame#cellCard {\n"
"      background-color: #111111;\n"
"      border: 1px solid rgba(255,255,255,0.12);\n"
"      border-radius: 12px;\n"
"    }\n"
"    QLabel#headerTitle {\n"
"      color: #ffffff;\n"
"      font-family: Courier New;\n"
"      font-size: 11px;\n"
"      letter-spacing: 3px;\n"
"    }\n"
"    QLabel#packLabel, QLabel#cellLabel {\n"
"      color: #ffffff;\n"
"      font-family: Courier New;\n"
"      font-size: 11px;\n"
"      letter-spacing: 2px;\n"
"    }\n"
"    QLabel#packValue, QLabel#cellValue {\n"
"      color: #1D9E75;\n"
"      font-family: Courier New;\n"
"      font-size: 64px;\n"
"      font-weight: 500;\n"
"    }\n"
"    QLabel#packUnit, QLabel#cellUnit {\n"
"      color: rgba(255,255,255,0.5);\n"
"      font-family: Courier New;\n"
"      font-size: 20px;\n"
"    }\n"
"    QLabel#packBadge, QLabel#"
                        "cellBadge {\n"
"      color: #1D9E75;\n"
"      background-color: rgba(29,158,117,0.15);\n"
"      font-family: Courier New;\n"
"      font-size: 10px;\n"
"      letter-spacing: 2px;\n"
"      border-radius: 4px;\n"
"      padding: 3px 8px;\n"
"    }\n"
"    QLabel#packMin, QLabel#packMax, QLabel#cellMin, QLabel#cellMax {\n"
"      color: #ffffff;\n"
"      font-family: Courier New;\n"
"      font-size: 11px;\n"
"    }\n"
"    QProgressBar#packBar, QProgressBar#cellBar {\n"
"      background-color: rgba(255,255,255,0.1);\n"
"      border: none;\n"
"      border-radius: 3px;\n"
"      height: 5px;\n"
"      text-align: center;\n"
"    }\n"
"    QProgressBar#packBar::chunk, QProgressBar#cellBar::chunk {\n"
"      background-color: #1D9E75;\n"
"      border-radius: 3px;\n"
"    }\n"
"    QLabel#footer {\n"
"      color: #ffffff;\n"
"      font-family: Courier New;\n"
"      font-size: 10px;\n"
"      letter-spacing: 3px;\n"
"    }\n"
"    QFrame#headerLine {\n"
"      color: rgba(255,255,255,0.15);\n"
"    }\n"
""
                        "      ")
        self.batteryMonitorPage = QWidget(self.page_3)
        self.batteryMonitorPage.setObjectName(u"batteryMonitorPage")
        self.batteryMonitorPage.setGeometry(QRect(125, 0, 520, 441))
        self.statusDot = QLabel(self.batteryMonitorPage)
        self.statusDot.setObjectName(u"statusDot")
        self.statusDot.setGeometry(QRect(32, 18, 9, 9))
        self.statusDot.setStyleSheet(u"background-color: #1D9E75; border-radius: 4px;")
        self.headerLineLeft = QFrame(self.batteryMonitorPage)
        self.headerLineLeft.setObjectName(u"headerLineLeft")
        self.headerLineLeft.setGeometry(QRect(48, 21, 145, 1))
        self.headerLineLeft.setStyleSheet(u"color: rgba(255,255,255,0.15);")
        self.headerLineLeft.setFrameShape(QFrame.Shape.HLine)
        self.headerTitle = QLabel(self.batteryMonitorPage)
        self.headerTitle.setObjectName(u"headerTitle")
        self.headerTitle.setGeometry(QRect(175, 10, 170, 24))
        self.headerTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.headerLineRight = QFrame(self.batteryMonitorPage)
        self.headerLineRight.setObjectName(u"headerLineRight")
        self.headerLineRight.setGeometry(QRect(337, 21, 151, 1))
        self.headerLineRight.setStyleSheet(u"color: rgba(255,255,255,0.15);")
        self.headerLineRight.setFrameShape(QFrame.Shape.HLine)
        self.packCard = QFrame(self.batteryMonitorPage)
        self.packCard.setObjectName(u"packCard")
        self.packCard.setGeometry(QRect(32, 60, 456, 160))
        self.packLabel = QLabel(self.packCard)
        self.packLabel.setObjectName(u"packLabel")
        self.packLabel.setGeometry(QRect(20, 20, 120, 18))
        self.packBadge = QLabel(self.packCard)
        self.packBadge.setObjectName(u"packBadge")
        self.packBadge.setGeometry(QRect(338, 18, 88, 20))
        self.packBadge.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.packValue = QLabel(self.packCard)
        self.packValue.setObjectName(u"packValue")
        self.packValue.setGeometry(QRect(35, 55, 150, 60))
        self.packValue.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.packUnit = QLabel(self.packCard)
        self.packUnit.setObjectName(u"packUnit")
        self.packUnit.setGeometry(QRect(190, 86, 20, 30))
        self.packBar = QProgressBar(self.packCard)
        self.packBar.setObjectName(u"packBar")
        self.packBar.setGeometry(QRect(37, 118, 382, 5))
        self.packBar.setValue(68)
        self.packBar.setTextVisible(False)
        self.packMin = QLabel(self.packCard)
        self.packMin.setObjectName(u"packMin")
        self.packMin.setGeometry(QRect(34, 132, 100, 18))
        self.packMax = QLabel(self.packCard)
        self.packMax.setObjectName(u"packMax")
        self.packMax.setGeometry(QRect(321, 132, 100, 18))
        self.cellCard = QFrame(self.batteryMonitorPage)
        self.cellCard.setObjectName(u"cellCard")
        self.cellCard.setGeometry(QRect(32, 246, 456, 160))
        self.cellLabel = QLabel(self.cellCard)
        self.cellLabel.setObjectName(u"cellLabel")
        self.cellLabel.setGeometry(QRect(20, 20, 140, 18))
        self.cellBadge = QLabel(self.cellCard)
        self.cellBadge.setObjectName(u"cellBadge")
        self.cellBadge.setGeometry(QRect(324, 18, 102, 20))
        self.cellBadge.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cellValue = QLabel(self.cellCard)
        self.cellValue.setObjectName(u"cellValue")
        self.cellValue.setGeometry(QRect(35, 55, 150, 60))
        self.cellValue.setAlignment(Qt.AlignmentFlag.AlignBottom|Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft)
        self.cellUnit = QLabel(self.cellCard)
        self.cellUnit.setObjectName(u"cellUnit")
        self.cellUnit.setGeometry(QRect(190, 86, 20, 30))
        self.cellBar = QProgressBar(self.cellCard)
        self.cellBar.setObjectName(u"cellBar")
        self.cellBar.setGeometry(QRect(37, 118, 382, 5))
        self.cellBar.setValue(68)
        self.cellBar.setTextVisible(False)
        self.cellMin = QLabel(self.cellCard)
        self.cellMin.setObjectName(u"cellMin")
        self.cellMin.setGeometry(QRect(34, 132, 90, 18))
        self.cellMax = QLabel(self.cellCard)
        self.cellMax.setObjectName(u"cellMax")
        self.cellMax.setGeometry(QRect(327, 132, 93, 18))
        self.footer = QLabel(self.batteryMonitorPage)
        self.footer.setObjectName(u"footer")
        self.footer.setGeometry(QRect(130, 414, 260, 18))
        self.footer.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"\n"
"QWidget#page_4 {\n"
"    background-color: #0a0c10;\n"
"}\n"
"QFrame#frameTopLeft, QFrame#frameTopRight,\n"
"QFrame#frameBottomLeft, QFrame#frameBottomRight {\n"
"    background-color: #0d1117;\n"
"    border: 1px solid #1e2530;\n"
"}\n"
"QLabel#label_8, QLabel#label_10,\n"
"QLabel#label_11, QLabel#label_12 {\n"
"    color: #ffffff;\n"
"    font-family: \"Rajdhani\";\n"
"    font-size: 15px;\n"
"    font-weight: 600;\n"
"    letter-spacing: 2px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#running_perc, QLabel#gated_percent,\n"
"QLabel#running_temp, QLabel#cur_max_temp {\n"
"    color: #ffffff;\n"
"    font-family: \"Share Tech Mono\";\n"
"    font-size: 56px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelUnit1, QLabel#labelUnit2,\n"
"QLabel#labelUnit3, QLabel#labelUnit4 {\n"
"    color: #ffffff;\n"
"    font-family: \"Rajdhani\";\n"
"    font-size: 18px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelCorner1, QLabel#l"
                        "abelCorner2,\n"
"QLabel#labelCorner3, QLabel#labelCorner4 {\n"
"    color: #ffffff;\n"
"    font-family: \"Share Tech Mono\";\n"
"    font-size: 12px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelDot1, QLabel#labelDot2 {\n"
"    color: #ff6b35;\n"
"    font-size: 16px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#labelDot3, QLabel#labelDot4 {\n"
"    color: #55d86a;\n"
"    font-size: 16px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"      ")
        self.frameTopLeft = QFrame(self.page_4)
        self.frameTopLeft.setObjectName(u"frameTopLeft")
        self.frameTopLeft.setGeometry(QRect(0, 0, 386, 221))
        self.frameTopLeft.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelDot1 = QLabel(self.frameTopLeft)
        self.labelDot1.setObjectName(u"labelDot1")
        self.labelDot1.setGeometry(QRect(18, 16, 14, 18))
        self.label_8 = QLabel(self.frameTopLeft)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(38, 15, 160, 22))
        self.labelCorner1 = QLabel(self.frameTopLeft)
        self.labelCorner1.setObjectName(u"labelCorner1")
        self.labelCorner1.setGeometry(QRect(332, 14, 34, 20))
        self.labelCorner1.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.running_perc = QLabel(self.frameTopLeft)
        self.running_perc.setObjectName(u"running_perc")
        self.running_perc.setGeometry(QRect(0, 68, 386, 66))
        self.running_perc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelUnit1 = QLabel(self.frameTopLeft)
        self.labelUnit1.setObjectName(u"labelUnit1")
        self.labelUnit1.setGeometry(QRect(0, 132, 386, 28))
        self.labelUnit1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frameTopRight = QFrame(self.page_4)
        self.frameTopRight.setObjectName(u"frameTopRight")
        self.frameTopRight.setGeometry(QRect(385, 0, 386, 221))
        self.frameTopRight.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelDot2 = QLabel(self.frameTopRight)
        self.labelDot2.setObjectName(u"labelDot2")
        self.labelDot2.setGeometry(QRect(18, 16, 14, 18))
        self.label_10 = QLabel(self.frameTopRight)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(38, 15, 160, 22))
        self.labelCorner2 = QLabel(self.frameTopRight)
        self.labelCorner2.setObjectName(u"labelCorner2")
        self.labelCorner2.setGeometry(QRect(332, 14, 34, 20))
        self.labelCorner2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.gated_percent = QLabel(self.frameTopRight)
        self.gated_percent.setObjectName(u"gated_percent")
        self.gated_percent.setGeometry(QRect(0, 68, 386, 66))
        self.gated_percent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelUnit2 = QLabel(self.frameTopRight)
        self.labelUnit2.setObjectName(u"labelUnit2")
        self.labelUnit2.setGeometry(QRect(0, 132, 386, 28))
        self.labelUnit2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frameBottomLeft = QFrame(self.page_4)
        self.frameBottomLeft.setObjectName(u"frameBottomLeft")
        self.frameBottomLeft.setGeometry(QRect(0, 220, 386, 221))
        self.frameBottomLeft.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelDot3 = QLabel(self.frameBottomLeft)
        self.labelDot3.setObjectName(u"labelDot3")
        self.labelDot3.setGeometry(QRect(18, 16, 14, 18))
        self.label_11 = QLabel(self.frameBottomLeft)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(38, 15, 160, 22))
        self.labelCorner3 = QLabel(self.frameBottomLeft)
        self.labelCorner3.setObjectName(u"labelCorner3")
        self.labelCorner3.setGeometry(QRect(338, 14, 28, 20))
        self.labelCorner3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.running_temp = QLabel(self.frameBottomLeft)
        self.running_temp.setObjectName(u"running_temp")
        self.running_temp.setGeometry(QRect(0, 68, 386, 66))
        self.running_temp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelUnit3 = QLabel(self.frameBottomLeft)
        self.labelUnit3.setObjectName(u"labelUnit3")
        self.labelUnit3.setGeometry(QRect(0, 132, 386, 28))
        self.labelUnit3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frameBottomRight = QFrame(self.page_4)
        self.frameBottomRight.setObjectName(u"frameBottomRight")
        self.frameBottomRight.setGeometry(QRect(385, 220, 386, 221))
        self.frameBottomRight.setFrameShape(QFrame.Shape.StyledPanel)
        self.labelDot4 = QLabel(self.frameBottomRight)
        self.labelDot4.setObjectName(u"labelDot4")
        self.labelDot4.setGeometry(QRect(18, 16, 14, 18))
        self.label_12 = QLabel(self.frameBottomRight)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(38, 15, 170, 22))
        self.labelCorner4 = QLabel(self.frameBottomRight)
        self.labelCorner4.setObjectName(u"labelCorner4")
        self.labelCorner4.setGeometry(QRect(338, 14, 28, 20))
        self.labelCorner4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.cur_max_temp = QLabel(self.frameBottomRight)
        self.cur_max_temp.setObjectName(u"cur_max_temp")
        self.cur_max_temp.setGeometry(QRect(0, 68, 386, 66))
        self.cur_max_temp.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.labelUnit4 = QLabel(self.frameBottomRight)
        self.labelUnit4.setObjectName(u"labelUnit4")
        self.labelUnit4.setGeometry(QRect(0, 132, 386, 28))
        self.labelUnit4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.page_4)
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.page_5.setStyleSheet(u"QWidget#page_5 {\n"
"    background-color: #05070a;\n"
"}\n"
"QFrame#thermalTopCard, QFrame#motorLoopCard, QFrame#inverterLoopCard {\n"
"    background-color: #0d1117;\n"
"    border: 1px solid #1f2937;\n"
"    border-radius: 14px;\n"
"}\n"
"QLabel#thermalSectionTitle {\n"
"    color: #d1d5db;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 18px;\n"
"    font-weight: 700;\n"
"    letter-spacing: 1px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#thermalSectionDot {\n"
"    color: #22c55e;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 18px;\n"
"    font-weight: 700;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#componentHeader, QLabel#motorLabel, QLabel#igbtLabel, QLabel#coldPlateLabel {\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 15px;\n"
"    font-weight: 600;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#flHeader, QLabel#frHeader, QLabel#rlHeader, QLabel#rrHeader {\n"
"    color: #60a"
                        "5fa;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 15px;\n"
"    font-weight: 700;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#motorFLValue, QLabel#motorFRValue, QLabel#motorRLValue, QLabel#motorRRValue,\n"
"QLabel#igbtFLValue, QLabel#igbtFRValue, QLabel#igbtRLValue, QLabel#igbtRRValue,\n"
"QLabel#coldPlateFLValue, QLabel#coldPlateFRValue, QLabel#coldPlateRLValue, QLabel#coldPlateRRValue {\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 15px;\n"
"    font-weight: 700;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#motorLoopTitle, QLabel#inverterLoopTitle {\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 16px;\n"
"    font-weight: 700;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#motorLoopStartLabel, QLabel#motorLoopEndLabel,\n"
"QLabel#inverterLoopStartLabel, QLabel#inverterLoopEndLabel {\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size:"
                        " 14px;\n"
"    font-weight: 600;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QLabel#motorLoopStartValue, QLabel#motorLoopEndValue,\n"
"QLabel#inverterLoopStartValue, QLabel#inverterLoopEndValue {\n"
"    color: #ffffff;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 22px;\n"
"    font-weight: 700;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"QFrame#thermalDivider1, QFrame#thermalDivider2, QFrame#thermalDivider3 {\n"
"    background-color: #1f2937;\n"
"    min-height: 1px;\n"
"    max-height: 1px;\n"
"    border: none;\n"
"}")
        self.thermalSectionDot = QLabel(self.page_5)
        self.thermalSectionDot.setObjectName(u"thermalSectionDot")
        self.thermalSectionDot.setGeometry(QRect(18, 16, 16, 24))
        self.thermalSectionTitle = QLabel(self.page_5)
        self.thermalSectionTitle.setObjectName(u"thermalSectionTitle")
        self.thermalSectionTitle.setGeometry(QRect(0, 16, 771, 24))
        self.thermalSectionTitle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thermalTopCard = QFrame(self.page_5)
        self.thermalTopCard.setObjectName(u"thermalTopCard")
        self.thermalTopCard.setGeometry(QRect(18, 54, 735, 208))
        self.thermalTopCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.componentHeader = QLabel(self.thermalTopCard)
        self.componentHeader.setObjectName(u"componentHeader")
        self.componentHeader.setGeometry(QRect(18, 18, 170, 22))
        self.flHeader = QLabel(self.thermalTopCard)
        self.flHeader.setObjectName(u"flHeader")
        self.flHeader.setGeometry(QRect(230, 18, 72, 22))
        self.flHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.frHeader = QLabel(self.thermalTopCard)
        self.frHeader.setObjectName(u"frHeader")
        self.frHeader.setGeometry(QRect(344, 18, 72, 22))
        self.frHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rlHeader = QLabel(self.thermalTopCard)
        self.rlHeader.setObjectName(u"rlHeader")
        self.rlHeader.setGeometry(QRect(458, 18, 72, 22))
        self.rlHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.rrHeader = QLabel(self.thermalTopCard)
        self.rrHeader.setObjectName(u"rrHeader")
        self.rrHeader.setGeometry(QRect(572, 18, 72, 22))
        self.rrHeader.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thermalDivider1 = QFrame(self.thermalTopCard)
        self.thermalDivider1.setObjectName(u"thermalDivider1")
        self.thermalDivider1.setGeometry(QRect(18, 46, 699, 1))
        self.thermalDivider1.setFrameShape(QFrame.Shape.NoFrame)
        self.motorLabel = QLabel(self.thermalTopCard)
        self.motorLabel.setObjectName(u"motorLabel")
        self.motorLabel.setGeometry(QRect(18, 58, 170, 24))
        self.motorFLValue = QLabel(self.thermalTopCard)
        self.motorFLValue.setObjectName(u"motorFLValue")
        self.motorFLValue.setGeometry(QRect(230, 58, 72, 24))
        self.motorFLValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.motorFRValue = QLabel(self.thermalTopCard)
        self.motorFRValue.setObjectName(u"motorFRValue")
        self.motorFRValue.setGeometry(QRect(344, 58, 72, 24))
        self.motorFRValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.motorRLValue = QLabel(self.thermalTopCard)
        self.motorRLValue.setObjectName(u"motorRLValue")
        self.motorRLValue.setGeometry(QRect(458, 58, 72, 24))
        self.motorRLValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.motorRRValue = QLabel(self.thermalTopCard)
        self.motorRRValue.setObjectName(u"motorRRValue")
        self.motorRRValue.setGeometry(QRect(572, 58, 72, 24))
        self.motorRRValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thermalDivider2 = QFrame(self.thermalTopCard)
        self.thermalDivider2.setObjectName(u"thermalDivider2")
        self.thermalDivider2.setGeometry(QRect(18, 94, 699, 1))
        self.thermalDivider2.setFrameShape(QFrame.Shape.NoFrame)
        self.igbtLabel = QLabel(self.thermalTopCard)
        self.igbtLabel.setObjectName(u"igbtLabel")
        self.igbtLabel.setGeometry(QRect(18, 106, 170, 24))
        self.igbtFLValue = QLabel(self.thermalTopCard)
        self.igbtFLValue.setObjectName(u"igbtFLValue")
        self.igbtFLValue.setGeometry(QRect(230, 106, 72, 24))
        self.igbtFLValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.igbtFRValue = QLabel(self.thermalTopCard)
        self.igbtFRValue.setObjectName(u"igbtFRValue")
        self.igbtFRValue.setGeometry(QRect(344, 106, 72, 24))
        self.igbtFRValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.igbtRLValue = QLabel(self.thermalTopCard)
        self.igbtRLValue.setObjectName(u"igbtRLValue")
        self.igbtRLValue.setGeometry(QRect(458, 106, 72, 24))
        self.igbtRLValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.igbtRRValue = QLabel(self.thermalTopCard)
        self.igbtRRValue.setObjectName(u"igbtRRValue")
        self.igbtRRValue.setGeometry(QRect(572, 106, 72, 24))
        self.igbtRRValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.thermalDivider3 = QFrame(self.thermalTopCard)
        self.thermalDivider3.setObjectName(u"thermalDivider3")
        self.thermalDivider3.setGeometry(QRect(18, 142, 699, 1))
        self.thermalDivider3.setFrameShape(QFrame.Shape.NoFrame)
        self.coldPlateLabel = QLabel(self.thermalTopCard)
        self.coldPlateLabel.setObjectName(u"coldPlateLabel")
        self.coldPlateLabel.setGeometry(QRect(18, 154, 170, 24))
        self.coldPlateFLValue = QLabel(self.thermalTopCard)
        self.coldPlateFLValue.setObjectName(u"coldPlateFLValue")
        self.coldPlateFLValue.setGeometry(QRect(230, 154, 72, 24))
        self.coldPlateFLValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coldPlateFRValue = QLabel(self.thermalTopCard)
        self.coldPlateFRValue.setObjectName(u"coldPlateFRValue")
        self.coldPlateFRValue.setGeometry(QRect(344, 154, 72, 24))
        self.coldPlateFRValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coldPlateRLValue = QLabel(self.thermalTopCard)
        self.coldPlateRLValue.setObjectName(u"coldPlateRLValue")
        self.coldPlateRLValue.setGeometry(QRect(458, 154, 72, 24))
        self.coldPlateRLValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.coldPlateRRValue = QLabel(self.thermalTopCard)
        self.coldPlateRRValue.setObjectName(u"coldPlateRRValue")
        self.coldPlateRRValue.setGeometry(QRect(572, 154, 72, 24))
        self.coldPlateRRValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.motorLoopCard = QFrame(self.page_5)
        self.motorLoopCard.setObjectName(u"motorLoopCard")
        self.motorLoopCard.setGeometry(QRect(18, 279, 360, 128))
        self.motorLoopCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.motorLoopTitle = QLabel(self.motorLoopCard)
        self.motorLoopTitle.setObjectName(u"motorLoopTitle")
        self.motorLoopTitle.setGeometry(QRect(16, 16, 150, 24))
        self.motorLoopStartLabel = QLabel(self.motorLoopCard)
        self.motorLoopStartLabel.setObjectName(u"motorLoopStartLabel")
        self.motorLoopStartLabel.setGeometry(QRect(16, 44, 100, 20))
        self.motorLoopEndLabel = QLabel(self.motorLoopCard)
        self.motorLoopEndLabel.setObjectName(u"motorLoopEndLabel")
        self.motorLoopEndLabel.setGeometry(QRect(168, 44, 100, 20))
        self.motorLoopStartValue = QLabel(self.motorLoopCard)
        self.motorLoopStartValue.setObjectName(u"motorLoopStartValue")
        self.motorLoopStartValue.setGeometry(QRect(16, 66, 100, 28))
        self.motorLoopEndValue = QLabel(self.motorLoopCard)
        self.motorLoopEndValue.setObjectName(u"motorLoopEndValue")
        self.motorLoopEndValue.setGeometry(QRect(168, 66, 100, 28))
        self.inverterLoopCard = QFrame(self.page_5)
        self.inverterLoopCard.setObjectName(u"inverterLoopCard")
        self.inverterLoopCard.setGeometry(QRect(393, 279, 360, 128))
        self.inverterLoopCard.setFrameShape(QFrame.Shape.StyledPanel)
        self.inverterLoopTitle = QLabel(self.inverterLoopCard)
        self.inverterLoopTitle.setObjectName(u"inverterLoopTitle")
        self.inverterLoopTitle.setGeometry(QRect(16, 16, 170, 24))
        self.inverterLoopStartLabel = QLabel(self.inverterLoopCard)
        self.inverterLoopStartLabel.setObjectName(u"inverterLoopStartLabel")
        self.inverterLoopStartLabel.setGeometry(QRect(16, 44, 100, 20))
        self.inverterLoopEndLabel = QLabel(self.inverterLoopCard)
        self.inverterLoopEndLabel.setObjectName(u"inverterLoopEndLabel")
        self.inverterLoopEndLabel.setGeometry(QRect(168, 44, 100, 20))
        self.inverterLoopStartValue = QLabel(self.inverterLoopCard)
        self.inverterLoopStartValue.setObjectName(u"inverterLoopStartValue")
        self.inverterLoopStartValue.setGeometry(QRect(16, 66, 100, 28))
        self.inverterLoopEndValue = QLabel(self.inverterLoopCard)
        self.inverterLoopEndValue.setObjectName(u"inverterLoopEndValue")
        self.inverterLoopEndValue.setGeometry(QRect(168, 66, 100, 28))
        self.stackedWidget.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.page_6.setStyleSheet(u"\n"
"QWidget#page_6 {\n"
"    background-color: #090909;\n"
"}\n"
"QLabel#page6Title {\n"
"    color: #a2a2a6;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    letter-spacing: 2px;\n"
"    background-color: transparent;\n"
"}\n"
"QWidget#can1_util_bar_1, QWidget#can1_util_bar_2, QWidget#can1_util_bar_3, QWidget#can1_util_bar_4 {\n"
"    background-color: #10d96f;\n"
"    border: 2px solid #29363d;\n"
"    border-radius: 14px;\n"
"}\n"
"QLabel#barPercentStyle {\n"
"    color: #09170f;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12px;\n"
"    font-weight: 600;\n"
"    background-color: transparent;\n"
"}\n"
"QLabel#canLabelStyle {\n"
"    color: #dedee1;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 11px;\n"
"    font-weight: 600;\n"
"    background-color: transparent;\n"
"}\n"
"QWidget#linkErrorsCard, QFrame#inverte_code_table {\n"
"    background-color: #151515;\n"
"    border: 1px solid #2b2d31;\n"
"    border-radius: 14px;\n"
"}\n"
"QLabel#linkEr"
                        "rorsTitle {\n"
"    color: #9d9da1;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: 500;\n"
"    letter-spacing: 1px;\n"
"    background-color: transparent;\n"
"}\n"
"QWidget#l1_light, QWidget#l2_light, QWidget#l3_light, QWidget#l4_light {\n"
"    background-color: #eb2e25;\n"
"    border-radius: 15px;\n"
"}\n"
"QLabel#linkErrorText {\n"
"    color: #dfdfe2;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 11px;\n"
"    font-weight: 500;\n"
"    background-color: transparent;\n"
"}\n"
"QLabel#tableHeaderLabel {\n"
"    color: #4e9eff;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"    background-color: transparent;\n"
"}\n"
"QLabel#tableRowLabel {\n"
"    color: #ebebed;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 14px;\n"
"    font-weight: 600;\n"
"    background-color: transparent;\n"
"}\n"
"QLabel#tableRowValue {\n"
"    color: #ebebed;\n"
"    font-family: \"Segoe UI\";\n"
"    font-size: 12px;\n"
"    font-weight: 6"
                        "00;\n"
"    background-color: transparent;\n"
"}\n"
"QFrame#tableLine1, QFrame#tableLine2, QFrame#tableLine3 {\n"
"    background-color: #24272d;\n"
"    border: none;\n"
"}\n"
"      ")
        self.page6Dot = QLabel(self.page_6)
        self.page6Dot.setObjectName(u"page6Dot")
        self.page6Dot.setGeometry(QRect(18, 16, 16, 22))
        self.page6Dot.setStyleSheet(u"color: #22d67a; font-size: 22px; font-weight: 700; background-color: transparent;")
        self.page6Dot.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.page6Title = QLabel(self.page_6)
        self.page6Title.setObjectName(u"page6Title")
        self.page6Title.setGeometry(QRect(44, 14, 230, 24))
        self.can1_util_bar_1 = QWidget(self.page_6)
        self.can1_util_bar_1.setObjectName(u"can1_util_bar_1")
        self.can1_util_bar_1.setGeometry(QRect(18, 74, 80, 220))
        self.barPercentStyle = QLabel(self.can1_util_bar_1)
        self.barPercentStyle.setObjectName(u"barPercentStyle")
        self.barPercentStyle.setGeometry(QRect(0, 178, 80, 24))
        self.barPercentStyle.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.can1_util_bar_2 = QWidget(self.page_6)
        self.can1_util_bar_2.setObjectName(u"can1_util_bar_2")
        self.can1_util_bar_2.setGeometry(QRect(112, 74, 80, 220))
        self.barPercentStyle2 = QLabel(self.can1_util_bar_2)
        self.barPercentStyle2.setObjectName(u"barPercentStyle2")
        self.barPercentStyle2.setGeometry(QRect(0, 178, 80, 24))
        self.barPercentStyle2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.can1_util_bar_3 = QWidget(self.page_6)
        self.can1_util_bar_3.setObjectName(u"can1_util_bar_3")
        self.can1_util_bar_3.setGeometry(QRect(206, 74, 80, 220))
        self.barPercentStyle3 = QLabel(self.can1_util_bar_3)
        self.barPercentStyle3.setObjectName(u"barPercentStyle3")
        self.barPercentStyle3.setGeometry(QRect(0, 178, 80, 24))
        self.barPercentStyle3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.can1_util_bar_4 = QWidget(self.page_6)
        self.can1_util_bar_4.setObjectName(u"can1_util_bar_4")
        self.can1_util_bar_4.setGeometry(QRect(300, 74, 80, 220))
        self.barPercentStyle4 = QLabel(self.can1_util_bar_4)
        self.barPercentStyle4.setObjectName(u"barPercentStyle4")
        self.barPercentStyle4.setGeometry(QRect(0, 178, 80, 24))
        self.barPercentStyle4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.canLabelStyle = QLabel(self.page_6)
        self.canLabelStyle.setObjectName(u"canLabelStyle")
        self.canLabelStyle.setGeometry(QRect(31, 300, 54, 34))
        self.canLabelStyle.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.canLabelStyle2 = QLabel(self.page_6)
        self.canLabelStyle2.setObjectName(u"canLabelStyle2")
        self.canLabelStyle2.setGeometry(QRect(125, 300, 54, 34))
        self.canLabelStyle2.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.canLabelStyle3 = QLabel(self.page_6)
        self.canLabelStyle3.setObjectName(u"canLabelStyle3")
        self.canLabelStyle3.setGeometry(QRect(219, 300, 54, 34))
        self.canLabelStyle3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.canLabelStyle4 = QLabel(self.page_6)
        self.canLabelStyle4.setObjectName(u"canLabelStyle4")
        self.canLabelStyle4.setGeometry(QRect(313, 300, 54, 34))
        self.canLabelStyle4.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.linkErrorsCard = QWidget(self.page_6)
        self.linkErrorsCard.setObjectName(u"linkErrorsCard")
        self.linkErrorsCard.setGeometry(QRect(18, 332, 734, 96))
        self.linkErrorsTitle = QLabel(self.linkErrorsCard)
        self.linkErrorsTitle.setObjectName(u"linkErrorsTitle")
        self.linkErrorsTitle.setGeometry(QRect(16, 10, 150, 20))
        self.l1_light = QWidget(self.linkErrorsCard)
        self.l1_light.setObjectName(u"l1_light")
        self.l1_light.setGeometry(QRect(65, 36, 30, 30))
        self.l2_light = QWidget(self.linkErrorsCard)
        self.l2_light.setObjectName(u"l2_light")
        self.l2_light.setGeometry(QRect(256, 36, 30, 30))
        self.l3_light = QWidget(self.linkErrorsCard)
        self.l3_light.setObjectName(u"l3_light")
        self.l3_light.setGeometry(QRect(447, 36, 30, 30))
        self.l4_light = QWidget(self.linkErrorsCard)
        self.l4_light.setObjectName(u"l4_light")
        self.l4_light.setGeometry(QRect(638, 36, 30, 30))
        self.linkErrorText = QLabel(self.linkErrorsCard)
        self.linkErrorText.setObjectName(u"linkErrorText")
        self.linkErrorText.setGeometry(QRect(59, 70, 42, 18))
        self.linkErrorText.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkErrorText2 = QLabel(self.linkErrorsCard)
        self.linkErrorText2.setObjectName(u"linkErrorText2")
        self.linkErrorText2.setGeometry(QRect(250, 70, 42, 18))
        self.linkErrorText2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkErrorText3 = QLabel(self.linkErrorsCard)
        self.linkErrorText3.setObjectName(u"linkErrorText3")
        self.linkErrorText3.setGeometry(QRect(441, 70, 42, 18))
        self.linkErrorText3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.linkErrorText4 = QLabel(self.linkErrorsCard)
        self.linkErrorText4.setObjectName(u"linkErrorText4")
        self.linkErrorText4.setGeometry(QRect(632, 70, 42, 18))
        self.linkErrorText4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.inverte_code_table = QFrame(self.page_6)
        self.inverte_code_table.setObjectName(u"inverte_code_table")
        self.inverte_code_table.setGeometry(QRect(402, 74, 350, 220))
        self.inverte_code_table.setFrameShape(QFrame.Shape.StyledPanel)
        self.tableHeaderLabel = QLabel(self.inverte_code_table)
        self.tableHeaderLabel.setObjectName(u"tableHeaderLabel")
        self.tableHeaderLabel.setGeometry(QRect(20, 14, 100, 22))
        self.tableHeaderLabel2 = QLabel(self.inverte_code_table)
        self.tableHeaderLabel2.setObjectName(u"tableHeaderLabel2")
        self.tableHeaderLabel2.setGeometry(QRect(265, 14, 65, 22))
        self.tableHeaderLabel2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.tableLine1 = QFrame(self.inverte_code_table)
        self.tableLine1.setObjectName(u"tableLine1")
        self.tableLine1.setGeometry(QRect(20, 44, 310, 1))
        self.tableLine1.setFrameShape(QFrame.Shape.HLine)
        self.tableRowLabel = QLabel(self.inverte_code_table)
        self.tableRowLabel.setObjectName(u"tableRowLabel")
        self.tableRowLabel.setGeometry(QRect(20, 58, 120, 20))
        self.tableRowValue = QLabel(self.inverte_code_table)
        self.tableRowValue.setObjectName(u"tableRowValue")
        self.tableRowValue.setGeometry(QRect(282, 58, 48, 20))
        self.tableRowValue.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.tableLine2 = QFrame(self.inverte_code_table)
        self.tableLine2.setObjectName(u"tableLine2")
        self.tableLine2.setGeometry(QRect(20, 90, 310, 1))
        self.tableLine2.setFrameShape(QFrame.Shape.HLine)
        self.tableRowLabel2 = QLabel(self.inverte_code_table)
        self.tableRowLabel2.setObjectName(u"tableRowLabel2")
        self.tableRowLabel2.setGeometry(QRect(20, 104, 120, 20))
        self.tableRowValue2 = QLabel(self.inverte_code_table)
        self.tableRowValue2.setObjectName(u"tableRowValue2")
        self.tableRowValue2.setGeometry(QRect(282, 104, 48, 20))
        self.tableRowValue2.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.tableLine3 = QFrame(self.inverte_code_table)
        self.tableLine3.setObjectName(u"tableLine3")
        self.tableLine3.setGeometry(QRect(20, 136, 310, 1))
        self.tableLine3.setFrameShape(QFrame.Shape.HLine)
        self.tableRowLabel3 = QLabel(self.inverte_code_table)
        self.tableRowLabel3.setObjectName(u"tableRowLabel3")
        self.tableRowLabel3.setGeometry(QRect(20, 150, 120, 20))
        self.tableRowValue3 = QLabel(self.inverte_code_table)
        self.tableRowValue3.setObjectName(u"tableRowValue3")
        self.tableRowValue3.setGeometry(QRect(282, 150, 48, 20))
        self.tableRowValue3.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.tableRowLabel4 = QLabel(self.inverte_code_table)
        self.tableRowLabel4.setObjectName(u"tableRowLabel4")
        self.tableRowLabel4.setGeometry(QRect(20, 186, 120, 20))
        self.tableRowValue4 = QLabel(self.inverte_code_table)
        self.tableRowValue4.setObjectName(u"tableRowValue4")
        self.tableRowValue4.setGeometry(QRect(282, 186, 48, 20))
        self.tableRowValue4.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.stackedWidget.addWidget(self.page_6)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"\n"
"QWidget#page_2 {\n"
"    background-color: #0a0a0a;\n"
"}\n"
"QLabel#bms_title {\n"
"    color: #f0f0f0;\n"
"    font-family: \"Courier New\";\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    background-color: transparent;\n"
"}\n"
"QLabel#bms_subtitle {\n"
"    color: #555555;\n"
"    font-family: \"Courier New\";\n"
"    font-size: 16px;\n"
"    background-color: transparent;\n"
"}\n"
"QLabel#dotCharging, QLabel#dotBalancing {\n"
"    color: #E24B4A;\n"
"    font-size: 16px;\n"
"    background-color: transparent;\n"
"}\n"
"QLabel#statusChargingLabel, QLabel#statusBalancingLabel {\n"
"    color: #aaaaaa;\n"
"    font-family: \"Courier New\";\n"
"    font-size: 16px;\n"
"    background-color: transparent;\n"
"}\n"
"QLabel#badgeCharging, QLabel#badgeBalancing {\n"
"    background-color: rgba(226, 75, 74, 40);\n"
"    color: #E24B4A;\n"
"    font-family: \"Courier New\";\n"
"    font-size: 16px;\n"
"    font-weight: bold;\n"
"    border-radius: 8px;\n"
"    border: 1px solid rgba(226, 75, 74, 80)"
                        ";\n"
"}\n"
"QFrame#bms_divider {\n"
"    background-color: rgba(255, 255, 255, 25);\n"
"}\n"
"QFrame#bmsCard1, QFrame#bmsCard2,\n"
"QFrame#bmsCard3, QFrame#bmsCard4,\n"
"QFrame#bmsCard5, QFrame#bmsCard6 {\n"
"    background-color: #161616;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"    border-radius: 8px;\n"
"}\n"
"QLabel#lblCurrent, QLabel#lblVoltage,\n"
"QLabel#lblMinTemp, QLabel#lblMaxTemp,\n"
"QLabel#lblMinVolt, QLabel#lblMaxVolt {\n"
"    color: #555555;\n"
"    font-family: \"Courier New\";\n"
"    font-size: 12px;\n"
"    background-color: transparent;\n"
"}\n"
"QLabel#valCurrent, QLabel#valVoltage,\n"
"QLabel#valMinTemp, QLabel#valMaxTemp,\n"
"QLabel#valMinVolt, QLabel#valMaxVolt {\n"
"    color: #f0f0f0;\n"
"    font-family: \"Courier New\";\n"
"    font-size: 26px;\n"
"    font-weight: bold;\n"
"    background-color: transparent;\n"
"}\n"
"      ")
        self.bms_title = QLabel(self.page_2)
        self.bms_title.setObjectName(u"bms_title")
        self.bms_title.setGeometry(QRect(190, 16, 280, 28))
        self.bms_subtitle = QLabel(self.page_2)
        self.bms_subtitle.setObjectName(u"bms_subtitle")
        self.bms_subtitle.setGeometry(QRect(478, 16, 140, 28))
        self.bms_title_line = QFrame(self.page_2)
        self.bms_title_line.setObjectName(u"bms_title_line")
        self.bms_title_line.setGeometry(QRect(190, 48, 390, 1))
        self.bms_title_line.setStyleSheet(u"background-color: rgb(26, 26, 26);")
        self.bms_title_line.setFrameShape(QFrame.Shape.HLine)
        self.dotCharging = QLabel(self.page_2)
        self.dotCharging.setObjectName(u"dotCharging")
        self.dotCharging.setGeometry(QRect(190, 62, 18, 22))
        self.statusChargingLabel = QLabel(self.page_2)
        self.statusChargingLabel.setObjectName(u"statusChargingLabel")
        self.statusChargingLabel.setGeometry(QRect(216, 62, 150, 22))
        self.badgeCharging = QLabel(self.page_2)
        self.badgeCharging.setObjectName(u"badgeCharging")
        self.badgeCharging.setGeometry(QRect(382, 62, 54, 22))
        self.badgeCharging.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.dotBalancing = QLabel(self.page_2)
        self.dotBalancing.setObjectName(u"dotBalancing")
        self.dotBalancing.setGeometry(QRect(190, 92, 18, 22))
        self.statusBalancingLabel = QLabel(self.page_2)
        self.statusBalancingLabel.setObjectName(u"statusBalancingLabel")
        self.statusBalancingLabel.setGeometry(QRect(216, 92, 150, 22))
        self.badgeBalancing = QLabel(self.page_2)
        self.badgeBalancing.setObjectName(u"badgeBalancing")
        self.badgeBalancing.setGeometry(QRect(382, 92, 54, 22))
        self.badgeBalancing.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.bms_divider = QFrame(self.page_2)
        self.bms_divider.setObjectName(u"bms_divider")
        self.bms_divider.setGeometry(QRect(110, 124, 550, 1))
        self.bms_divider.setFrameShape(QFrame.Shape.HLine)
        self.bms_divider.setFrameShadow(QFrame.Shadow.Plain)
        self.bmsCard1 = QFrame(self.page_2)
        self.bmsCard1.setObjectName(u"bmsCard1")
        self.bmsCard1.setGeometry(QRect(110, 160, 170, 110))
        self.lblCurrent = QLabel(self.bmsCard1)
        self.lblCurrent.setObjectName(u"lblCurrent")
        self.lblCurrent.setGeometry(QRect(12, 14, 146, 16))
        self.valCurrent = QLabel(self.bmsCard1)
        self.valCurrent.setObjectName(u"valCurrent")
        self.valCurrent.setGeometry(QRect(12, 42, 146, 38))
        self.bmsCard2 = QFrame(self.page_2)
        self.bmsCard2.setObjectName(u"bmsCard2")
        self.bmsCard2.setGeometry(QRect(300, 160, 170, 110))
        self.lblVoltage = QLabel(self.bmsCard2)
        self.lblVoltage.setObjectName(u"lblVoltage")
        self.lblVoltage.setGeometry(QRect(12, 14, 146, 16))
        self.valVoltage = QLabel(self.bmsCard2)
        self.valVoltage.setObjectName(u"valVoltage")
        self.valVoltage.setGeometry(QRect(12, 42, 146, 38))
        self.bmsCard3 = QFrame(self.page_2)
        self.bmsCard3.setObjectName(u"bmsCard3")
        self.bmsCard3.setGeometry(QRect(490, 160, 170, 110))
        self.lblMinTemp = QLabel(self.bmsCard3)
        self.lblMinTemp.setObjectName(u"lblMinTemp")
        self.lblMinTemp.setGeometry(QRect(12, 14, 146, 16))
        self.valMinTemp = QLabel(self.bmsCard3)
        self.valMinTemp.setObjectName(u"valMinTemp")
        self.valMinTemp.setGeometry(QRect(12, 42, 146, 38))
        self.bmsCard4 = QFrame(self.page_2)
        self.bmsCard4.setObjectName(u"bmsCard4")
        self.bmsCard4.setGeometry(QRect(110, 290, 170, 110))
        self.lblMaxTemp = QLabel(self.bmsCard4)
        self.lblMaxTemp.setObjectName(u"lblMaxTemp")
        self.lblMaxTemp.setGeometry(QRect(12, 14, 146, 16))
        self.valMaxTemp = QLabel(self.bmsCard4)
        self.valMaxTemp.setObjectName(u"valMaxTemp")
        self.valMaxTemp.setGeometry(QRect(12, 42, 146, 38))
        self.bmsCard5 = QFrame(self.page_2)
        self.bmsCard5.setObjectName(u"bmsCard5")
        self.bmsCard5.setGeometry(QRect(300, 290, 170, 110))
        self.lblMinVolt = QLabel(self.bmsCard5)
        self.lblMinVolt.setObjectName(u"lblMinVolt")
        self.lblMinVolt.setGeometry(QRect(12, 14, 146, 16))
        self.valMinVolt = QLabel(self.bmsCard5)
        self.valMinVolt.setObjectName(u"valMinVolt")
        self.valMinVolt.setGeometry(QRect(12, 42, 146, 38))
        self.bmsCard6 = QFrame(self.page_2)
        self.bmsCard6.setObjectName(u"bmsCard6")
        self.bmsCard6.setGeometry(QRect(490, 290, 170, 110))
        self.lblMaxVolt = QLabel(self.bmsCard6)
        self.lblMaxVolt.setObjectName(u"lblMaxVolt")
        self.lblMaxVolt.setGeometry(QRect(12, 14, 146, 16))
        self.valMaxVolt = QLabel(self.bmsCard6)
        self.valMaxVolt.setObjectName(u"valMaxVolt")
        self.valMaxVolt.setGeometry(QRect(12, 42, 146, 38))
        self.stackedWidget.addWidget(self.page_2)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.label_throttle_title = QLabel(self.page_7)
        self.label_throttle_title.setObjectName(u"label_throttle_title")
        self.label_throttle_title.setGeometry(QRect(0, 5, 771, 20))
        self.label_throttle_title.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.label_throttle_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.throttle_bar_bg = QWidget(self.page_7)
        self.throttle_bar_bg.setObjectName(u"throttle_bar_bg")
        self.throttle_bar_bg.setGeometry(QRect(10, 28, 581, 22))
        self.throttle_bar_bg.setStyleSheet(u"background-color: rgb(8, 255, 8)")
        self.throttle_bar_fill = QWidget(self.page_7)
        self.throttle_bar_fill.setObjectName(u"throttle_bar_fill")
        self.throttle_bar_fill.setGeometry(QRect(10, 28, 0, 22))
        self.throttle_bar_fill.setStyleSheet(u"background-color: rgb(0, 255, 0);")
        self.label_vx = QLabel(self.page_7)
        self.label_vx.setObjectName(u"label_vx")
        self.label_vx.setGeometry(QRect(8, 58, 257, 20))
        self.label_vx.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.vx_value = QLabel(self.page_7)
        self.vx_value.setObjectName(u"vx_value")
        self.vx_value.setGeometry(QRect(8, 78, 257, 50))
        font = QFont()
        font.setPointSize(30)
        font.setBold(True)
        self.vx_value.setFont(font)
        self.vx_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_front_brake = QLabel(self.page_7)
        self.label_front_brake.setObjectName(u"label_front_brake")
        self.label_front_brake.setGeometry(QRect(265, 58, 257, 20))
        self.label_front_brake.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.front_brake_value = QLabel(self.page_7)
        self.front_brake_value.setObjectName(u"front_brake_value")
        self.front_brake_value.setGeometry(QRect(265, 78, 257, 50))
        self.front_brake_value.setFont(font)
        self.front_brake_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_rear_brake = QLabel(self.page_7)
        self.label_rear_brake.setObjectName(u"label_rear_brake")
        self.label_rear_brake.setGeometry(QRect(522, 58, 249, 20))
        self.label_rear_brake.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.rear_brake_value = QLabel(self.page_7)
        self.rear_brake_value.setObjectName(u"rear_brake_value")
        self.rear_brake_value.setGeometry(QRect(522, 78, 249, 50))
        self.rear_brake_value.setFont(font)
        self.rear_brake_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_imd_res = QLabel(self.page_7)
        self.label_imd_res.setObjectName(u"label_imd_res")
        self.label_imd_res.setGeometry(QRect(8, 138, 257, 20))
        self.label_imd_res.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.imd_res_value = QLabel(self.page_7)
        self.imd_res_value.setObjectName(u"imd_res_value")
        self.imd_res_value.setGeometry(QRect(8, 158, 257, 50))
        self.imd_res_value.setFont(font)
        self.imd_res_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_total_volt = QLabel(self.page_7)
        self.label_total_volt.setObjectName(u"label_total_volt")
        self.label_total_volt.setGeometry(QRect(265, 138, 257, 20))
        self.label_total_volt.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.total_volt_value = QLabel(self.page_7)
        self.total_volt_value.setObjectName(u"total_volt_value")
        self.total_volt_value.setGeometry(QRect(265, 158, 257, 50))
        self.total_volt_value.setFont(font)
        self.total_volt_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_fl_voltage = QLabel(self.page_7)
        self.label_fl_voltage.setObjectName(u"label_fl_voltage")
        self.label_fl_voltage.setGeometry(QRect(522, 138, 249, 20))
        self.label_fl_voltage.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.fl_voltage_value = QLabel(self.page_7)
        self.fl_voltage_value.setObjectName(u"fl_voltage_value")
        self.fl_voltage_value.setGeometry(QRect(522, 158, 249, 50))
        self.fl_voltage_value.setFont(font)
        self.fl_voltage_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_fl_error = QLabel(self.page_7)
        self.label_fl_error.setObjectName(u"label_fl_error")
        self.label_fl_error.setGeometry(QRect(8, 218, 257, 20))
        self.label_fl_error.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.fl_error_value = QLabel(self.page_7)
        self.fl_error_value.setObjectName(u"fl_error_value")
        self.fl_error_value.setGeometry(QRect(8, 238, 257, 50))
        self.fl_error_value.setFont(font)
        self.fl_error_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_rl_temp_inv = QLabel(self.page_7)
        self.label_rl_temp_inv.setObjectName(u"label_rl_temp_inv")
        self.label_rl_temp_inv.setGeometry(QRect(265, 218, 257, 20))
        self.label_rl_temp_inv.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.rl_temp_inv_value = QLabel(self.page_7)
        self.rl_temp_inv_value.setObjectName(u"rl_temp_inv_value")
        self.rl_temp_inv_value.setGeometry(QRect(265, 238, 257, 50))
        self.rl_temp_inv_value.setFont(font)
        self.rl_temp_inv_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_rl_temp_motor = QLabel(self.page_7)
        self.label_rl_temp_motor.setObjectName(u"label_rl_temp_motor")
        self.label_rl_temp_motor.setGeometry(QRect(522, 218, 249, 20))
        self.label_rl_temp_motor.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.rl_temp_motor_value = QLabel(self.page_7)
        self.rl_temp_motor_value.setObjectName(u"rl_temp_motor_value")
        self.rl_temp_motor_value.setGeometry(QRect(522, 238, 249, 50))
        self.rl_temp_motor_value.setFont(font)
        self.rl_temp_motor_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_rr_error = QLabel(self.page_7)
        self.label_rr_error.setObjectName(u"label_rr_error")
        self.label_rr_error.setGeometry(QRect(8, 298, 257, 20))
        self.label_rr_error.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.rr_error_value = QLabel(self.page_7)
        self.rr_error_value.setObjectName(u"rr_error_value")
        self.rr_error_value.setGeometry(QRect(8, 318, 257, 50))
        self.rr_error_value.setFont(font)
        self.rr_error_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_rl_temp_igbt = QLabel(self.page_7)
        self.label_rl_temp_igbt.setObjectName(u"label_rl_temp_igbt")
        self.label_rl_temp_igbt.setGeometry(QRect(265, 298, 257, 20))
        self.label_rl_temp_igbt.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.rl_temp_igbt_value = QLabel(self.page_7)
        self.rl_temp_igbt_value.setObjectName(u"rl_temp_igbt_value")
        self.rl_temp_igbt_value.setGeometry(QRect(265, 318, 257, 50))
        self.rl_temp_igbt_value.setFont(font)
        self.rl_temp_igbt_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_min_volt = QLabel(self.page_7)
        self.label_min_volt.setObjectName(u"label_min_volt")
        self.label_min_volt.setGeometry(QRect(522, 298, 249, 20))
        self.label_min_volt.setStyleSheet(u"color: rgb(255, 255, 255); font-weight: bold;")
        self.min_volt_value = QLabel(self.page_7)
        self.min_volt_value.setObjectName(u"min_volt_value")
        self.min_volt_value.setGeometry(QRect(522, 318, 249, 50))
        self.min_volt_value.setFont(font)
        self.min_volt_value.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.stackedWidget.addWidget(self.page_7)
        self.page_8 = QWidget()
        self.page_8.setObjectName(u"page_8")
        self.fl_table = QTableWidget(self.page_8)
        if (self.fl_table.columnCount() < 2):
            self.fl_table.setColumnCount(2)
        if (self.fl_table.rowCount() < 4):
            self.fl_table.setRowCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.fl_table.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.fl_table.setItem(0, 1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.fl_table.setItem(1, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.fl_table.setItem(1, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.fl_table.setItem(2, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.fl_table.setItem(2, 1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.fl_table.setItem(3, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.fl_table.setItem(3, 1, __qtablewidgetitem7)
        self.fl_table.setObjectName(u"fl_table")
        self.fl_table.setGeometry(QRect(10, 10, 220, 121))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setItalic(True)
        self.fl_table.setFont(font1)
        self.fl_table.setStyleSheet(u"color: rgb(255, 255, 255); border: 1px solid rgba(255,255,255,150);")
        self.fl_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fl_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fl_table.setRowCount(4)
        self.fl_table.setColumnCount(2)
        self.fl_table.horizontalHeader().setVisible(False)
        self.fl_table.horizontalHeader().setDefaultSectionSize(130)
        self.fl_table.horizontalHeader().setStretchLastSection(True)
        self.fl_table.verticalHeader().setVisible(False)
        self.fl_table.verticalHeader().setDefaultSectionSize(30)
        self.fr_table = QTableWidget(self.page_8)
        if (self.fr_table.columnCount() < 2):
            self.fr_table.setColumnCount(2)
        if (self.fr_table.rowCount() < 4):
            self.fr_table.setRowCount(4)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.fr_table.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.fr_table.setItem(0, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.fr_table.setItem(1, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.fr_table.setItem(1, 1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.fr_table.setItem(2, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.fr_table.setItem(2, 1, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.fr_table.setItem(3, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.fr_table.setItem(3, 1, __qtablewidgetitem15)
        self.fr_table.setObjectName(u"fr_table")
        self.fr_table.setGeometry(QRect(541, 10, 220, 131))
        self.fr_table.setFont(font1)
        self.fr_table.setStyleSheet(u"color: rgb(255, 255, 255); border: 1px solid rgba(255,255,255,150);")
        self.fr_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fr_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.fr_table.setRowCount(4)
        self.fr_table.setColumnCount(2)
        self.fr_table.horizontalHeader().setVisible(False)
        self.fr_table.horizontalHeader().setDefaultSectionSize(130)
        self.fr_table.horizontalHeader().setStretchLastSection(True)
        self.fr_table.verticalHeader().setVisible(False)
        self.fr_table.verticalHeader().setDefaultSectionSize(30)
        self.rl_table = QTableWidget(self.page_8)
        if (self.rl_table.columnCount() < 2):
            self.rl_table.setColumnCount(2)
        if (self.rl_table.rowCount() < 4):
            self.rl_table.setRowCount(4)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.rl_table.setItem(0, 0, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.rl_table.setItem(0, 1, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.rl_table.setItem(1, 0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.rl_table.setItem(1, 1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.rl_table.setItem(2, 0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.rl_table.setItem(2, 1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.rl_table.setItem(3, 0, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.rl_table.setItem(3, 1, __qtablewidgetitem23)
        self.rl_table.setObjectName(u"rl_table")
        self.rl_table.setGeometry(QRect(10, 310, 220, 121))
        self.rl_table.setFont(font1)
        self.rl_table.setStyleSheet(u"color: rgb(255, 255, 255); border: 1px solid rgba(255,255,255,150);")
        self.rl_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.rl_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.rl_table.setRowCount(4)
        self.rl_table.setColumnCount(2)
        self.rl_table.horizontalHeader().setVisible(False)
        self.rl_table.horizontalHeader().setDefaultSectionSize(130)
        self.rl_table.horizontalHeader().setStretchLastSection(True)
        self.rl_table.verticalHeader().setVisible(False)
        self.rl_table.verticalHeader().setDefaultSectionSize(30)
        self.rr_table = QTableWidget(self.page_8)
        if (self.rr_table.columnCount() < 2):
            self.rr_table.setColumnCount(2)
        if (self.rr_table.rowCount() < 4):
            self.rr_table.setRowCount(4)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.rr_table.setItem(0, 0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.rr_table.setItem(0, 1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.rr_table.setItem(1, 0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.rr_table.setItem(1, 1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.rr_table.setItem(2, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.rr_table.setItem(2, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.rr_table.setItem(3, 0, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.rr_table.setItem(3, 1, __qtablewidgetitem31)
        self.rr_table.setObjectName(u"rr_table")
        self.rr_table.setGeometry(QRect(540, 310, 220, 121))
        self.rr_table.setFont(font1)
        self.rr_table.setStyleSheet(u"color: rgb(255, 255, 255); border: 1px solid rgba(255,255,255,150);")
        self.rr_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.rr_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.rr_table.setRowCount(4)
        self.rr_table.setColumnCount(2)
        self.rr_table.horizontalHeader().setVisible(False)
        self.rr_table.horizontalHeader().setDefaultSectionSize(130)
        self.rr_table.horizontalHeader().setStretchLastSection(True)
        self.rr_table.verticalHeader().setVisible(False)
        self.rr_table.verticalHeader().setDefaultSectionSize(30)
        self.label_5 = QLabel(self.page_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 60, 171, 311))
        self.label_5.setStyleSheet(u"background-image: url(:/Downloads/f1_birds_eye.png);")
        self.label_5.setScaledContents(True)
        self.stackedWidget.addWidget(self.page_8)
        self.page_9 = QWidget()
        self.page_9.setObjectName(u"page_9")
        self.page_9.setStyleSheet(u"\n"
"        QWidget#page_9 {\n"
"            background-color: rgb(15, 15, 15);\n"
"        }\n"
"        QLabel {\n"
"            color: rgb(255, 255, 255);\n"
"            font-family: Arial, sans-serif;\n"
"        }\n"
"      ")
        self.led_cell_volt = QWidget(self.page_9)
        self.led_cell_volt.setObjectName(u"led_cell_volt")
        self.led_cell_volt.setGeometry(QRect(10, 10, 24, 24))
        self.led_cell_volt.setStyleSheet(u"background-color: rgb(255, 0, 0); \n"
"border-radius: 12px; ")
        self.lbl_cell_volt_alarm = QLabel(self.page_9)
        self.lbl_cell_volt_alarm.setObjectName(u"lbl_cell_volt_alarm")
        self.lbl_cell_volt_alarm.setGeometry(QRect(45, 15, 200, 24))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        font2.setPointSize(14)
        self.lbl_cell_volt_alarm.setFont(font2)
        self.lbl_coolant_temp_alarm = QLabel(self.page_9)
        self.lbl_coolant_temp_alarm.setObjectName(u"lbl_coolant_temp_alarm")
        self.lbl_coolant_temp_alarm.setGeometry(QRect(45, 45, 311, 24))
        self.lbl_coolant_temp_alarm.setFont(font2)
        self.lbl_coolant_flow_alarm = QLabel(self.page_9)
        self.lbl_coolant_flow_alarm.setObjectName(u"lbl_coolant_flow_alarm")
        self.lbl_coolant_flow_alarm.setGeometry(QRect(45, 75, 200, 24))
        self.lbl_coolant_flow_alarm.setFont(font2)
        self.lbl_cell_temp_alarm = QLabel(self.page_9)
        self.lbl_cell_temp_alarm.setObjectName(u"lbl_cell_temp_alarm")
        self.lbl_cell_temp_alarm.setGeometry(QRect(520, 15, 200, 24))
        self.lbl_cell_temp_alarm.setFont(font2)
        self.lbl_cell_temp_alarm.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.led_cell_temp = QWidget(self.page_9)
        self.led_cell_temp.setObjectName(u"led_cell_temp")
        self.led_cell_temp.setGeometry(QRect(730, 15, 24, 24))
        self.led_cell_temp.setStyleSheet(u"background-color: rgb(255, 0, 0); \n"
"border-radius: 12px; ")
        self.lbl_hv_batt_ok = QLabel(self.page_9)
        self.lbl_hv_batt_ok.setObjectName(u"lbl_hv_batt_ok")
        self.lbl_hv_batt_ok.setGeometry(QRect(520, 45, 200, 24))
        self.lbl_hv_batt_ok.setFont(font2)
        self.lbl_hv_batt_ok.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.led_hv_batt_ok = QWidget(self.page_9)
        self.led_hv_batt_ok.setObjectName(u"led_hv_batt_ok")
        self.led_hv_batt_ok.setGeometry(QRect(730, 45, 24, 24))
        self.led_hv_batt_ok.setStyleSheet(u"background-color: rgb(255, 0, 0); \n"
"border-radius: 12px; ")
        self.lbl_can_ok = QLabel(self.page_9)
        self.lbl_can_ok.setObjectName(u"lbl_can_ok")
        self.lbl_can_ok.setGeometry(QRect(520, 75, 200, 24))
        self.lbl_can_ok.setFont(font2)
        self.lbl_can_ok.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.led_can_ok = QWidget(self.page_9)
        self.led_can_ok.setObjectName(u"led_can_ok")
        self.led_can_ok.setGeometry(QRect(730, 75, 24, 24))
        self.led_can_ok.setStyleSheet(u"background-color: rgb(255, 0, 0); \n"
"border-radius: 12px; ")
        self.val_speed = QLabel(self.page_9)
        self.val_speed.setObjectName(u"val_speed")
        self.val_speed.setGeometry(QRect(229, 80, 221, 150))
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(120)
        font3.setBold(True)
        self.val_speed.setFont(font3)
        self.val_speed.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.lbl_kmh = QLabel(self.page_9)
        self.lbl_kmh.setObjectName(u"lbl_kmh")
        self.lbl_kmh.setGeometry(QRect(460, 140, 201, 70))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(45)
        font4.setBold(True)
        self.lbl_kmh.setFont(font4)
        self.val_soc = QLabel(self.page_9)
        self.val_soc.setObjectName(u"val_soc")
        self.val_soc.setGeometry(QRect(169, 240, 181, 50))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setPointSize(40)
        self.val_soc.setFont(font5)
        self.val_soc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_soc = QLabel(self.page_9)
        self.lbl_soc.setObjectName(u"lbl_soc")
        self.lbl_soc.setGeometry(QRect(190, 295, 160, 20))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(14)
        font6.setItalic(True)
        self.lbl_soc.setFont(font6)
        self.lbl_soc.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.val_inv_volt = QLabel(self.page_9)
        self.val_inv_volt.setObjectName(u"val_inv_volt")
        self.val_inv_volt.setGeometry(QRect(390, 240, 181, 50))
        self.val_inv_volt.setFont(font5)
        self.val_inv_volt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_inv_volt = QLabel(self.page_9)
        self.lbl_inv_volt.setObjectName(u"lbl_inv_volt")
        self.lbl_inv_volt.setGeometry(QRect(390, 295, 160, 20))
        self.lbl_inv_volt.setFont(font6)
        self.lbl_inv_volt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_min_cell = QLabel(self.page_9)
        self.lbl_min_cell.setObjectName(u"lbl_min_cell")
        self.lbl_min_cell.setGeometry(QRect(10, 329, 180, 51))
        self.lbl_min_cell.setFont(font6)
        self.lbl_min_cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.val_min_cell = QLabel(self.page_9)
        self.val_min_cell.setObjectName(u"val_min_cell")
        self.val_min_cell.setGeometry(QRect(10, 385, 180, 45))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(35)
        self.val_min_cell.setFont(font7)
        self.val_min_cell.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_max_igbt = QLabel(self.page_9)
        self.lbl_max_igbt.setObjectName(u"lbl_max_igbt")
        self.lbl_max_igbt.setGeometry(QRect(200, 329, 180, 51))
        self.lbl_max_igbt.setFont(font6)
        self.lbl_max_igbt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.val_max_igbt = QLabel(self.page_9)
        self.val_max_igbt.setObjectName(u"val_max_igbt")
        self.val_max_igbt.setGeometry(QRect(200, 385, 180, 45))
        self.val_max_igbt.setFont(font7)
        self.val_max_igbt.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_max_inv = QLabel(self.page_9)
        self.lbl_max_inv.setObjectName(u"lbl_max_inv")
        self.lbl_max_inv.setGeometry(QRect(390, 329, 180, 51))
        self.lbl_max_inv.setFont(font6)
        self.lbl_max_inv.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.val_max_inv = QLabel(self.page_9)
        self.val_max_inv.setObjectName(u"val_max_inv")
        self.val_max_inv.setGeometry(QRect(390, 385, 180, 45))
        self.val_max_inv.setFont(font7)
        self.val_max_inv.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_max_motor = QLabel(self.page_9)
        self.lbl_max_motor.setObjectName(u"lbl_max_motor")
        self.lbl_max_motor.setGeometry(QRect(580, 329, 180, 51))
        self.lbl_max_motor.setFont(font6)
        self.lbl_max_motor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.val_max_motor = QLabel(self.page_9)
        self.val_max_motor.setObjectName(u"val_max_motor")
        self.val_max_motor.setGeometry(QRect(580, 385, 180, 45))
        self.val_max_motor.setFont(font7)
        self.val_max_motor.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.led_cell_volt_2 = QWidget(self.page_9)
        self.led_cell_volt_2.setObjectName(u"led_cell_volt_2")
        self.led_cell_volt_2.setGeometry(QRect(10, 40, 24, 24))
        self.led_cell_volt_2.setStyleSheet(u"background-color: rgb(255, 0, 0); \n"
"border-radius: 12px; ")
        self.led_cell_volt_3 = QWidget(self.page_9)
        self.led_cell_volt_3.setObjectName(u"led_cell_volt_3")
        self.led_cell_volt_3.setGeometry(QRect(10, 70, 24, 24))
        self.led_cell_volt_3.setStyleSheet(u"background-color: rgb(255, 0, 0);\n"
"border-radius: 12px; ")
        self.stackedWidget.addWidget(self.page_9)
        self.page_10 = QWidget()
        self.page_10.setObjectName(u"page_10")
        self.page_10.setStyleSheet(u"/* ===== Root ===== */\n"
"QWidget#page_10 {\n"
"    background-color: #000000;\n"
"}\n"
"\n"
"/* ===== Card panels ===== */\n"
"QFrame#cardSpeed,\n"
"QFrame#cardTirePSI,\n"
"QFrame#cardBrake,\n"
"QFrame#cardThrottle {\n"
"    background-color: #000000;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QFrame#cardTireTemp {\n"
"    background-color: #000000;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QFrame#cardPitMode {\n"
"    background-color: #FF1F1F;\n"
"    border: none;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"/* ===== Section headers ===== */\n"
"QLabel#tireTempHeader,\n"
"QLabel#tirePSIHeader,\n"
"QLabel#maxCellHeader,\n"
"QLabel#socHeader {\n"
"    color: rgba(255, 255, 255, 140);\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    font-size: 13px;\n"
"    font-weight: 500;\n"
"    letter-spacing: 3px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#tireFLLabel,\n"
"QLabel#tireFRLabel,\n"
"QLabel#tireRLLabel,\n"
"QLabel#tireRRLabel,"
                        "\n"
"QLabel#psiFLLabel,\n"
"QLabel#psiFRLabel,\n"
"QLabel#psiRLLabel,\n"
"QLabel#psiRRLabel {\n"
"    color: rgba(255, 255, 255, 89);\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    font-size: 11px;\n"
"    letter-spacing: 1px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* ===== Tire temp / PSI numbers ===== */\n"
"QLabel#tireFLValue,\n"
"QLabel#tireFRValue {\n"
"    color: #EF9F27;\n"
"    font-family: \"Roboto Mono\", \"Courier New\", monospace;\n"
"    font-size: 34px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#tireRLValue,\n"
"QLabel#tireRRValue {\n"
"    color: #E24B4A;\n"
"    font-family: \"Roboto Mono\", \"Courier New\", monospace;\n"
"    font-size: 34px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#psiFLValue,\n"
"QLabel#psiFRValue,\n"
"QLabel#psiRLValue,\n"
"QLabel#psiRRValue {\n"
"    color: #FFFFFF;\n"
"    font-family: \"Roboto Mono\", \"Courier New"
                        "\", monospace;\n"
"    font-size: 36px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* ===== Speed ===== */\n"
"QLabel#speedValue {\n"
"    color: #FFFFFF;\n"
"    font-family: \"Roboto Mono\", \"Courier New\", monospace;\n"
"    font-size: 200px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#speedUnit {\n"
"    color: rgba(255, 255, 255, 128);\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    font-size: 15px;\n"
"    letter-spacing: 4px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* ===== Max Cell / SoC ===== */\n"
"QLabel#maxCellValue {\n"
"    color: #1D9E75;\n"
"    font-family: \"Roboto Mono\", \"Courier New\", monospace;\n"
"    font-size: 32px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#socValue {\n"
"    color: #1D9E75;\n"
"    font-family: \"Roboto Mono\", \"Courier New\", monospace;\n"
"    font-size: 30p"
                        "x;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* ===== Scale labels ===== */\n"
"QLabel#scaleLabel0,\n"
"QLabel#scaleLabel15,\n"
"QLabel#scaleLabel30 {\n"
"    color: rgba(255, 255, 255, 102);\n"
"    font-family: \"Roboto Mono\", \"Courier New\", monospace;\n"
"    font-size: 16px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#scaleLabel45 {\n"
"    color: rgba(239, 159, 39, 230);\n"
"    font-family: \"Roboto Mono\", \"Courier New\", monospace;\n"
"    font-size: 16px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"QLabel#scaleLabel60,\n"
"QLabel#scaleLabelDQ {\n"
"    color: #E24B4A;\n"
"    font-family: \"Roboto Mono\", \"Courier New\", monospace;\n"
"    font-size: 16px;\n"
"    font-weight: 500;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* ===== Pit mode ===== */\n"
"QLabel#pitModeLabel {\n"
"    color: #000000;\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    font-si"
                        "ze: 36px;\n"
"    font-weight: 500;\n"
"    letter-spacing: 9px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* ===== Pedal labels ===== */\n"
"QLabel#brakeLabel,\n"
"QLabel#throttleLabel {\n"
"    color: rgba(255, 255, 255, 153);\n"
"    font-family: \"Roboto\", sans-serif;\n"
"    font-size: 12px;\n"
"    font-weight: 500;\n"
"    letter-spacing: 3px;\n"
"    background: transparent;\n"
"    border: none;\n"
"}\n"
"\n"
"/* ===== Separators ===== */\n"
"QFrame#tireTempSep,\n"
"QFrame#psiSep {\n"
"    background-color: rgba(255, 255, 255, 31);\n"
"    border: none;\n"
"    max-height: 1px;\n"
"    min-height: 1px;\n"
"}\n"
"\n"
"/* ===== Progress bars ===== */\n"
"QProgressBar#maxCellBar {\n"
"    background-color: #000000;\n"
"    border: 1px solid #EF9F27;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    color: transparent;\n"
"}\n"
"QProgressBar#maxCellBar::chunk {\n"
"    background-color: #1D9E75;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QProgressBar#socBar {\n"
""
                        "    background-color: #000000;\n"
"    border: 1px solid #EF9F27;\n"
"    border-radius: 3px;\n"
"    text-align: center;\n"
"    color: transparent;\n"
"}\n"
"QProgressBar#socBar::chunk {\n"
"    background-color: #1D9E75;\n"
"    border-radius: 2px;\n"
"}\n"
"\n"
"QProgressBar#brakeBar {\n"
"    background-color: #000000;\n"
"    border: 1px solid #EF9F27;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    color: transparent;\n"
"}\n"
"QProgressBar#brakeBar::chunk {\n"
"    background-color: #E24B4A;\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"QProgressBar#throttleBar {\n"
"    background-color: #000000;\n"
"    border: 1px solid #EF9F27;\n"
"    border-radius: 4px;\n"
"    text-align: center;\n"
"    color: transparent;\n"
"}\n"
"QProgressBar#throttleBar::chunk {\n"
"    background-color: #1D9E75;\n"
"    border-radius: 3px;\n"
"}\n"
"")
        self.cardTireTemp = QFrame(self.page_10)
        self.cardTireTemp.setObjectName(u"cardTireTemp")
        self.cardTireTemp.setGeometry(QRect(14, 14, 220, 319))
        self.cardTireTemp.setFrameShape(QFrame.Shape.NoFrame)
        self.tireTempGrid = QFrame(self.cardTireTemp)
        self.tireTempGrid.setObjectName(u"tireTempGrid")
        self.tireTempGrid.setGeometry(QRect(14, 14, 192, 126))
        self.tireTempGrid.setMinimumSize(QSize(192, 126))
        self.tireTempGrid.setFrameShape(QFrame.Shape.NoFrame)
        self.tireFLCell = QFrame(self.tireTempGrid)
        self.tireFLCell.setObjectName(u"tireFLCell")
        self.tireFLCell.setGeometry(QRect(0, 0, 90, 60))
        self.tireFLCell.setFrameShape(QFrame.Shape.NoFrame)
        self.tireFLLabel = QLabel(self.tireFLCell)
        self.tireFLLabel.setObjectName(u"tireFLLabel")
        self.tireFLLabel.setGeometry(QRect(0, 0, 90, 20))
        self.tireFLLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tireFLValue = QLabel(self.tireFLCell)
        self.tireFLValue.setObjectName(u"tireFLValue")
        self.tireFLValue.setGeometry(QRect(0, 20, 90, 40))
        self.tireFLValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tireFRCell = QFrame(self.tireTempGrid)
        self.tireFRCell.setObjectName(u"tireFRCell")
        self.tireFRCell.setGeometry(QRect(96, 0, 90, 60))
        self.tireFRCell.setFrameShape(QFrame.Shape.NoFrame)
        self.tireFRLabel = QLabel(self.tireFRCell)
        self.tireFRLabel.setObjectName(u"tireFRLabel")
        self.tireFRLabel.setGeometry(QRect(0, 0, 90, 20))
        self.tireFRLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tireFRValue = QLabel(self.tireFRCell)
        self.tireFRValue.setObjectName(u"tireFRValue")
        self.tireFRValue.setGeometry(QRect(0, 20, 90, 40))
        self.tireFRValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tireRLCell = QFrame(self.tireTempGrid)
        self.tireRLCell.setObjectName(u"tireRLCell")
        self.tireRLCell.setGeometry(QRect(0, 66, 90, 60))
        self.tireRLCell.setFrameShape(QFrame.Shape.NoFrame)
        self.tireRLLabel = QLabel(self.tireRLCell)
        self.tireRLLabel.setObjectName(u"tireRLLabel")
        self.tireRLLabel.setGeometry(QRect(0, 0, 90, 20))
        self.tireRLLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tireRLValue = QLabel(self.tireRLCell)
        self.tireRLValue.setObjectName(u"tireRLValue")
        self.tireRLValue.setGeometry(QRect(0, 20, 90, 40))
        self.tireRLValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tireRRCell = QFrame(self.tireTempGrid)
        self.tireRRCell.setObjectName(u"tireRRCell")
        self.tireRRCell.setGeometry(QRect(96, 66, 90, 60))
        self.tireRRCell.setFrameShape(QFrame.Shape.NoFrame)
        self.tireRRLabel = QLabel(self.tireRRCell)
        self.tireRRLabel.setObjectName(u"tireRRLabel")
        self.tireRRLabel.setGeometry(QRect(0, 0, 90, 20))
        self.tireRRLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tireRRValue = QLabel(self.tireRRCell)
        self.tireRRValue.setObjectName(u"tireRRValue")
        self.tireRRValue.setGeometry(QRect(0, 20, 90, 40))
        self.tireRRValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.tireTempSep = QFrame(self.cardTireTemp)
        self.tireTempSep.setObjectName(u"tireTempSep")
        self.tireTempSep.setGeometry(QRect(14, 153, 192, 1))
        self.tireTempSep.setFrameShape(QFrame.Shape.HLine)
        self.maxCellHeaderRow = QFrame(self.cardTireTemp)
        self.maxCellHeaderRow.setObjectName(u"maxCellHeaderRow")
        self.maxCellHeaderRow.setGeometry(QRect(14, 167, 192, 42))
        self.maxCellHeaderRow.setMinimumSize(QSize(0, 40))
        self.maxCellHeaderRow.setFrameShape(QFrame.Shape.NoFrame)
        self.maxCellHeader = QLabel(self.maxCellHeaderRow)
        self.maxCellHeader.setObjectName(u"maxCellHeader")
        self.maxCellHeader.setGeometry(QRect(0, 0, 192, 40))
        self.maxCellValue = QLabel(self.maxCellHeaderRow)
        self.maxCellValue.setObjectName(u"maxCellValue")
        self.maxCellValue.setGeometry(QRect(0, 0, 192, 40))
        self.maxCellValue.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.maxCellBar = QProgressBar(self.cardTireTemp)
        self.maxCellBar.setObjectName(u"maxCellBar")
        self.maxCellBar.setGeometry(QRect(14, 220, 192, 40))
        self.maxCellBar.setMinimum(0)
        self.maxCellBar.setMaximum(60)
        self.maxCellBar.setValue(43)
        self.maxCellBar.setTextVisible(False)
        self.scaleLabelsRow = QFrame(self.cardTireTemp)
        self.scaleLabelsRow.setObjectName(u"scaleLabelsRow")
        self.scaleLabelsRow.setGeometry(QRect(14, 272, 192, 50))
        self.scaleLabelsRow.setFrameShape(QFrame.Shape.NoFrame)
        self.scaleLabel0 = QLabel(self.scaleLabelsRow)
        self.scaleLabel0.setObjectName(u"scaleLabel0")
        self.scaleLabel0.setGeometry(QRect(0, 0, 22, 25))
        self.scaleLabel0.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.scaleLabel15 = QLabel(self.scaleLabelsRow)
        self.scaleLabel15.setObjectName(u"scaleLabel15")
        self.scaleLabel15.setGeometry(QRect(34, 0, 28, 25))
        self.scaleLabel15.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scaleLabel30 = QLabel(self.scaleLabelsRow)
        self.scaleLabel30.setObjectName(u"scaleLabel30")
        self.scaleLabel30.setGeometry(QRect(82, 0, 28, 25))
        self.scaleLabel30.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scaleLabel45 = QLabel(self.scaleLabelsRow)
        self.scaleLabel45.setObjectName(u"scaleLabel45")
        self.scaleLabel45.setGeometry(QRect(130, 0, 28, 25))
        self.scaleLabel45.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.scaleLabel60 = QLabel(self.scaleLabelsRow)
        self.scaleLabel60.setObjectName(u"scaleLabel60")
        self.scaleLabel60.setGeometry(QRect(162, 0, 30, 25))
        self.scaleLabel60.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.scaleLabelDQ = QLabel(self.scaleLabelsRow)
        self.scaleLabelDQ.setObjectName(u"scaleLabelDQ")
        self.scaleLabelDQ.setGeometry(QRect(155, 25, 37, 25))
        self.scaleLabelDQ.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.cardSpeed = QFrame(self.page_10)
        self.cardSpeed.setObjectName(u"cardSpeed")
        self.cardSpeed.setGeometry(QRect(246, 14, 252, 263))
        self.cardSpeed.setFrameShape(QFrame.Shape.NoFrame)
        self.speedLayout = QVBoxLayout(self.cardSpeed)
        self.speedLayout.setSpacing(6)
        self.speedLayout.setObjectName(u"speedLayout")
        self.speedLayout.setContentsMargins(6, 6, 6, 6)
        self.speedValue = QLabel(self.cardSpeed)
        self.speedValue.setObjectName(u"speedValue")
        self.speedValue.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.speedLayout.addWidget(self.speedValue)

        self.speedUnit = QLabel(self.cardSpeed)
        self.speedUnit.setObjectName(u"speedUnit")
        self.speedUnit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.speedLayout.addWidget(self.speedUnit)

        self.cardTirePSI = QFrame(self.page_10)
        self.cardTirePSI.setObjectName(u"cardTirePSI")
        self.cardTirePSI.setGeometry(QRect(529, 14, 228, 319))
        self.cardTirePSI.setFrameShape(QFrame.Shape.NoFrame)
        self.tirePSIHeader = QLabel(self.cardTirePSI)
        self.tirePSIHeader.setObjectName(u"tirePSIHeader")
        self.tirePSIHeader.setGeometry(QRect(14, 14, 74, 16))
        self.tirePSIGrid = QFrame(self.cardTirePSI)
        self.tirePSIGrid.setObjectName(u"tirePSIGrid")
        self.tirePSIGrid.setGeometry(QRect(14, 42, 200, 138))
        self.tirePSIGrid.setMinimumSize(QSize(200, 138))
        self.tirePSIGrid.setFrameShape(QFrame.Shape.NoFrame)
        self.psiFLCell = QFrame(self.tirePSIGrid)
        self.psiFLCell.setObjectName(u"psiFLCell")
        self.psiFLCell.setGeometry(QRect(0, 0, 90, 66))
        self.psiFLCell.setFrameShape(QFrame.Shape.NoFrame)
        self.psiFLLabel = QLabel(self.psiFLCell)
        self.psiFLLabel.setObjectName(u"psiFLLabel")
        self.psiFLLabel.setGeometry(QRect(0, 0, 90, 20))
        self.psiFLLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.psiFLValue = QLabel(self.psiFLCell)
        self.psiFLValue.setObjectName(u"psiFLValue")
        self.psiFLValue.setGeometry(QRect(0, 20, 90, 46))
        self.psiFLValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.psiFRCell = QFrame(self.tirePSIGrid)
        self.psiFRCell.setObjectName(u"psiFRCell")
        self.psiFRCell.setGeometry(QRect(110, 0, 90, 66))
        self.psiFRCell.setFrameShape(QFrame.Shape.NoFrame)
        self.psiFRLabel = QLabel(self.psiFRCell)
        self.psiFRLabel.setObjectName(u"psiFRLabel")
        self.psiFRLabel.setGeometry(QRect(0, 0, 90, 20))
        self.psiFRLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.psiFRValue = QLabel(self.psiFRCell)
        self.psiFRValue.setObjectName(u"psiFRValue")
        self.psiFRValue.setGeometry(QRect(0, 20, 90, 46))
        self.psiFRValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.psiRLCell = QFrame(self.tirePSIGrid)
        self.psiRLCell.setObjectName(u"psiRLCell")
        self.psiRLCell.setGeometry(QRect(0, 72, 90, 66))
        self.psiRLCell.setFrameShape(QFrame.Shape.NoFrame)
        self.psiRLLabel = QLabel(self.psiRLCell)
        self.psiRLLabel.setObjectName(u"psiRLLabel")
        self.psiRLLabel.setGeometry(QRect(0, 0, 90, 20))
        self.psiRLLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.psiRLValue = QLabel(self.psiRLCell)
        self.psiRLValue.setObjectName(u"psiRLValue")
        self.psiRLValue.setGeometry(QRect(0, 20, 90, 46))
        self.psiRLValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.psiRRCell = QFrame(self.tirePSIGrid)
        self.psiRRCell.setObjectName(u"psiRRCell")
        self.psiRRCell.setGeometry(QRect(110, 72, 90, 66))
        self.psiRRCell.setFrameShape(QFrame.Shape.NoFrame)
        self.psiRRLabel = QLabel(self.psiRRCell)
        self.psiRRLabel.setObjectName(u"psiRRLabel")
        self.psiRRLabel.setGeometry(QRect(0, 0, 90, 20))
        self.psiRRLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.psiRRValue = QLabel(self.psiRRCell)
        self.psiRRValue.setObjectName(u"psiRRValue")
        self.psiRRValue.setGeometry(QRect(0, 20, 90, 46))
        self.psiRRValue.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.psiSep = QFrame(self.cardTirePSI)
        self.psiSep.setObjectName(u"psiSep")
        self.psiSep.setGeometry(QRect(14, 195, 200, 1))
        self.psiSep.setFrameShape(QFrame.Shape.HLine)
        self.socHeaderRow = QFrame(self.cardTirePSI)
        self.socHeaderRow.setObjectName(u"socHeaderRow")
        self.socHeaderRow.setGeometry(QRect(14, 213, 200, 40))
        self.socHeaderRow.setMinimumSize(QSize(0, 40))
        self.socHeaderRow.setFrameShape(QFrame.Shape.NoFrame)
        self.socHeader = QLabel(self.socHeaderRow)
        self.socHeader.setObjectName(u"socHeader")
        self.socHeader.setGeometry(QRect(0, 0, 192, 40))
        self.socValue = QLabel(self.socHeaderRow)
        self.socValue.setObjectName(u"socValue")
        self.socValue.setGeometry(QRect(10, 0, 192, 40))
        self.socValue.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)
        self.socBar = QProgressBar(self.cardTirePSI)
        self.socBar.setObjectName(u"socBar")
        self.socBar.setGeometry(QRect(14, 265, 200, 40))
        self.socBar.setMinimumSize(QSize(0, 40))
        self.socBar.setMinimum(0)
        self.socBar.setMaximum(100)
        self.socBar.setValue(68)
        self.socBar.setTextVisible(False)
        self.cardBrake = QFrame(self.page_10)
        self.cardBrake.setObjectName(u"cardBrake")
        self.cardBrake.setGeometry(QRect(14, 345, 201, 82))
        self.cardBrake.setFrameShape(QFrame.Shape.NoFrame)
        self.brakeBar = QProgressBar(self.cardBrake)
        self.brakeBar.setObjectName(u"brakeBar")
        self.brakeBar.setGeometry(QRect(14, 10, 173, 40))
        self.brakeBar.setMinimum(0)
        self.brakeBar.setMaximum(100)
        self.brakeBar.setValue(18)
        self.brakeBar.setTextVisible(False)
        self.brakeLabel = QLabel(self.cardBrake)
        self.brakeLabel.setObjectName(u"brakeLabel")
        self.brakeLabel.setGeometry(QRect(14, 58, 173, 24))
        self.brakeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.cardPitMode = QFrame(self.page_10)
        self.cardPitMode.setObjectName(u"cardPitMode")
        self.cardPitMode.setGeometry(QRect(246, 345, 267, 75))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(11)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cardPitMode.sizePolicy().hasHeightForWidth())
        self.cardPitMode.setSizePolicy(sizePolicy)
        self.cardPitMode.setFrameShape(QFrame.Shape.StyledPanel)
        self.pitModeLayout = QHBoxLayout(self.cardPitMode)
        self.pitModeLayout.setSpacing(16)
        self.pitModeLayout.setObjectName(u"pitModeLayout")
        self.pitModeLayout.setContentsMargins(16, 16, 16, 16)
        self.pitModeLabel = QLabel(self.cardPitMode)
        self.pitModeLabel.setObjectName(u"pitModeLabel")
        self.pitModeLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.pitModeLayout.addWidget(self.pitModeLabel)

        self.cardThrottle = QFrame(self.page_10)
        self.cardThrottle.setObjectName(u"cardThrottle")
        self.cardThrottle.setGeometry(QRect(529, 345, 228, 82))
        self.cardThrottle.setFrameShape(QFrame.Shape.NoFrame)
        self.throttleBar = QProgressBar(self.cardThrottle)
        self.throttleBar.setObjectName(u"throttleBar")
        self.throttleBar.setGeometry(QRect(14, 10, 200, 40))
        self.throttleBar.setMinimum(0)
        self.throttleBar.setMaximum(100)
        self.throttleBar.setValue(64)
        self.throttleBar.setTextVisible(False)
        self.throttleLabel = QLabel(self.cardThrottle)
        self.throttleLabel.setObjectName(u"throttleLabel")
        self.throttleLabel.setGeometry(QRect(14, 58, 200, 24))
        self.throttleLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stackedWidget.addWidget(self.page_10)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(9)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionsettings.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.titleLabel.setText(QCoreApplication.translate("MainWindow", u"TELEMETRY - INPUT TRACE", None))
        self.frontBrakeValueTop.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"FRONT BRAKE", None))
        self.rearBrakeValueTop.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"REAR BRAKE", None))
        self.speedValueTop.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"SPEED", None))
        self.throttleValueTop.setText(QCoreApplication.translate("MainWindow", u"0%", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"THROTTLE", None))
        self.front_brake_text_2.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.speed_text_2.setText(QCoreApplication.translate("MainWindow", u"km/h", None))
        self.throttle_text_2.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.statFBLabel.setText(QCoreApplication.translate("MainWindow", u"FRONT BRAKE", None))
        self.front_brake_text.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.statRBLabel.setText(QCoreApplication.translate("MainWindow", u"REAR BRAKE", None))
        self.rear_brake_text.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.statSPLabel.setText(QCoreApplication.translate("MainWindow", u"SPEED", None))
        self.speed_text.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.statTHLabel.setText(QCoreApplication.translate("MainWindow", u"THROTTLE", None))
        self.throttle_text.setText(QCoreApplication.translate("MainWindow", u"--", None))
        self.label_13.setText("")
        self.front_brake_text_3.setText(QCoreApplication.translate("MainWindow", u"%", None))
        self.statusDot.setText("")
        self.headerTitle.setText(QCoreApplication.translate("MainWindow", u"BATTERY MONITOR", None))
        self.packLabel.setText(QCoreApplication.translate("MainWindow", u"PACK TOTAL", None))
        self.packBadge.setText(QCoreApplication.translate("MainWindow", u"\u25cf NORMAL", None))
        self.packValue.setText(QCoreApplication.translate("MainWindow", u"48.6", None))
        self.packUnit.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.packMin.setText(QCoreApplication.translate("MainWindow", u"Min: 40.0 V", None))
        self.packMax.setText(QCoreApplication.translate("MainWindow", u"Max: 58.8 V", None))
        self.cellLabel.setText(QCoreApplication.translate("MainWindow", u"CELL VOLTAGE", None))
        self.cellBadge.setText(QCoreApplication.translate("MainWindow", u"\u25cf BALANCED", None))
        self.cellValue.setText(QCoreApplication.translate("MainWindow", u"3.71", None))
        self.cellUnit.setText(QCoreApplication.translate("MainWindow", u"V", None))
        self.cellMin.setText(QCoreApplication.translate("MainWindow", u"Min: 3.0 V", None))
        self.cellMax.setText(QCoreApplication.translate("MainWindow", u"Max: 4.2 V", None))
        self.footer.setText(QCoreApplication.translate("MainWindow", u"REAL-TIME VOLTAGE READOUT", None))
        self.labelDot1.setText(QCoreApplication.translate("MainWindow", u"\u2022", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"RUNNING", None))
        self.labelCorner1.setText(QCoreApplication.translate("MainWindow", u"CH1", None))
        self.running_perc.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.labelUnit1.setText(QCoreApplication.translate("MainWindow", u"percent", None))
        self.labelDot2.setText(QCoreApplication.translate("MainWindow", u"\u2022", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"GATED", None))
        self.labelCorner2.setText(QCoreApplication.translate("MainWindow", u"CH2", None))
        self.gated_percent.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.labelUnit2.setText(QCoreApplication.translate("MainWindow", u"percent", None))
        self.labelDot3.setText(QCoreApplication.translate("MainWindow", u"\u2022", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"RUNNING", None))
        self.labelCorner3.setText(QCoreApplication.translate("MainWindow", u"T1", None))
        self.running_temp.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.labelUnit3.setText(QCoreApplication.translate("MainWindow", u"celsius", None))
        self.labelDot4.setText(QCoreApplication.translate("MainWindow", u"\u2022", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"MAX TEMP", None))
        self.labelCorner4.setText(QCoreApplication.translate("MainWindow", u"T2", None))
        self.cur_max_temp.setText(QCoreApplication.translate("MainWindow", u"00.0", None))
        self.labelUnit4.setText(QCoreApplication.translate("MainWindow", u"celsius", None))
        self.thermalSectionDot.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.thermalSectionTitle.setText(QCoreApplication.translate("MainWindow", u"THERMAL MONITOR", None))
        self.componentHeader.setText(QCoreApplication.translate("MainWindow", u"Component", None))
        self.flHeader.setText(QCoreApplication.translate("MainWindow", u"FL", None))
        self.frHeader.setText(QCoreApplication.translate("MainWindow", u"FR", None))
        self.rlHeader.setText(QCoreApplication.translate("MainWindow", u"RL", None))
        self.rrHeader.setText(QCoreApplication.translate("MainWindow", u"RR", None))
        self.motorLabel.setText(QCoreApplication.translate("MainWindow", u"Motor", None))
        self.motorFLValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.motorFRValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.motorRLValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.motorRRValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.igbtLabel.setText(QCoreApplication.translate("MainWindow", u"IGBT", None))
        self.igbtFLValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.igbtFRValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.igbtRLValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.igbtRRValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.coldPlateLabel.setText(QCoreApplication.translate("MainWindow", u"Cold Plate", None))
        self.coldPlateFLValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.coldPlateFRValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.coldPlateRLValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.coldPlateRRValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.motorLoopTitle.setText(QCoreApplication.translate("MainWindow", u"MOTOR LOOP", None))
        self.motorLoopStartLabel.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.motorLoopEndLabel.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.motorLoopStartValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.motorLoopEndValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.inverterLoopTitle.setText(QCoreApplication.translate("MainWindow", u"INVERTER LOOP", None))
        self.inverterLoopStartLabel.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.inverterLoopEndLabel.setText(QCoreApplication.translate("MainWindow", u"End", None))
        self.inverterLoopStartValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.inverterLoopEndValue.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.page6Dot.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.page6Title.setText(QCoreApplication.translate("MainWindow", u"INVERTER MONITOR", None))
        self.barPercentStyle.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.barPercentStyle2.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.barPercentStyle3.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.barPercentStyle4.setText(QCoreApplication.translate("MainWindow", u"100%", None))
        self.canLabelStyle.setText(QCoreApplication.translate("MainWindow", u"CAN\n"
"1", None))
        self.canLabelStyle2.setText(QCoreApplication.translate("MainWindow", u"CAN 2", None))
        self.canLabelStyle3.setText(QCoreApplication.translate("MainWindow", u"CAN 3", None))
        self.canLabelStyle4.setText(QCoreApplication.translate("MainWindow", u"CAN 4", None))
        self.linkErrorsTitle.setText(QCoreApplication.translate("MainWindow", u"LINK ERRORS", None))
        self.linkErrorText.setText(QCoreApplication.translate("MainWindow", u"L1", None))
        self.linkErrorText2.setText(QCoreApplication.translate("MainWindow", u"L2", None))
        self.linkErrorText3.setText(QCoreApplication.translate("MainWindow", u"L3", None))
        self.linkErrorText4.setText(QCoreApplication.translate("MainWindow", u"L4", None))
        self.tableHeaderLabel.setText(QCoreApplication.translate("MainWindow", u"Inverter", None))
        self.tableHeaderLabel2.setText(QCoreApplication.translate("MainWindow", u"Code", None))
        self.tableRowLabel.setText(QCoreApplication.translate("MainWindow", u"Inverter 1", None))
        self.tableRowValue.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tableRowLabel2.setText(QCoreApplication.translate("MainWindow", u"Inverter 2", None))
        self.tableRowValue2.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tableRowLabel3.setText(QCoreApplication.translate("MainWindow", u"Inverter 3", None))
        self.tableRowValue3.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.tableRowLabel4.setText(QCoreApplication.translate("MainWindow", u"Inverter 4", None))
        self.tableRowValue4.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.bms_title.setText(QCoreApplication.translate("MainWindow", u"Battery Management", None))
        self.bms_subtitle.setText(QCoreApplication.translate("MainWindow", u"BMS Monitor", None))
        self.dotCharging.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.statusChargingLabel.setText(QCoreApplication.translate("MainWindow", u"Charging", None))
        self.badgeCharging.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.dotBalancing.setText(QCoreApplication.translate("MainWindow", u"\u25cf", None))
        self.statusBalancingLabel.setText(QCoreApplication.translate("MainWindow", u"Balancing", None))
        self.badgeBalancing.setText(QCoreApplication.translate("MainWindow", u"Off", None))
        self.lblCurrent.setText(QCoreApplication.translate("MainWindow", u"CURRENT", None))
        self.valCurrent.setText(QCoreApplication.translate("MainWindow", u"0 A", None))
        self.lblVoltage.setText(QCoreApplication.translate("MainWindow", u"VOLTAGE", None))
        self.valVoltage.setText(QCoreApplication.translate("MainWindow", u"0 V", None))
        self.lblMinTemp.setText(QCoreApplication.translate("MainWindow", u"MIN CELL TEMP", None))
        self.valMinTemp.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.lblMaxTemp.setText(QCoreApplication.translate("MainWindow", u"MAX CELL TEMP", None))
        self.valMaxTemp.setText(QCoreApplication.translate("MainWindow", u"0 \u00b0C", None))
        self.lblMinVolt.setText(QCoreApplication.translate("MainWindow", u"MIN CELL VOLT", None))
        self.valMinVolt.setText(QCoreApplication.translate("MainWindow", u"0 V", None))
        self.lblMaxVolt.setText(QCoreApplication.translate("MainWindow", u"MAX CELL VOLT", None))
        self.valMaxVolt.setText(QCoreApplication.translate("MainWindow", u"0 V", None))
        self.label_throttle_title.setText(QCoreApplication.translate("MainWindow", u"Throttle Percentage", None))
        self.label_vx.setText(QCoreApplication.translate("MainWindow", u"Vx", None))
        self.vx_value.setText(QCoreApplication.translate("MainWindow", u"00 km/h", None))
        self.label_front_brake.setText(QCoreApplication.translate("MainWindow", u"Front Brake Pressure", None))
        self.front_brake_value.setText(QCoreApplication.translate("MainWindow", u"00.0 bar", None))
        self.label_rear_brake.setText(QCoreApplication.translate("MainWindow", u"Rear Brake Pressure", None))
        self.rear_brake_value.setText(QCoreApplication.translate("MainWindow", u"00.0 bar", None))
        self.label_imd_res.setText(QCoreApplication.translate("MainWindow", u"IMD RES", None))
        self.imd_res_value.setText(QCoreApplication.translate("MainWindow", u"000 kOhm", None))
        self.label_total_volt.setText(QCoreApplication.translate("MainWindow", u"TOTAL VOLT", None))
        self.total_volt_value.setText(QCoreApplication.translate("MainWindow", u"000 V", None))
        self.label_fl_voltage.setText(QCoreApplication.translate("MainWindow", u"FL Voltage", None))
        self.fl_voltage_value.setText(QCoreApplication.translate("MainWindow", u"000 V", None))
        self.label_fl_error.setText(QCoreApplication.translate("MainWindow", u"FL Error Info", None))
        self.fl_error_value.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.label_rl_temp_inv.setText(QCoreApplication.translate("MainWindow", u"RL Temp Inverter", None))
        self.rl_temp_inv_value.setText(QCoreApplication.translate("MainWindow", u"00.0 C", None))
        self.label_rl_temp_motor.setText(QCoreApplication.translate("MainWindow", u"RL Temp Motor", None))
        self.rl_temp_motor_value.setText(QCoreApplication.translate("MainWindow", u"00.0 C", None))
        self.label_rr_error.setText(QCoreApplication.translate("MainWindow", u"RR Error Info", None))
        self.rr_error_value.setText(QCoreApplication.translate("MainWindow", u"0000", None))
        self.label_rl_temp_igbt.setText(QCoreApplication.translate("MainWindow", u"RL Temp IGBT", None))
        self.rl_temp_igbt_value.setText(QCoreApplication.translate("MainWindow", u"00.0 C", None))
        self.label_min_volt.setText(QCoreApplication.translate("MainWindow", u"Min Volt", None))
        self.min_volt_value.setText(QCoreApplication.translate("MainWindow", u"0.00 V", None))

        __sortingEnabled = self.fl_table.isSortingEnabled()
        self.fl_table.setSortingEnabled(False)
        ___qtablewidgetitem = self.fl_table.item(0, 0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Wheel Speed", None));
        ___qtablewidgetitem1 = self.fl_table.item(0, 1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"0000", None));
        ___qtablewidgetitem2 = self.fl_table.item(1, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Torque", None));
        ___qtablewidgetitem3 = self.fl_table.item(1, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"0.0", None));
        ___qtablewidgetitem4 = self.fl_table.item(2, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Rot Pot", None));
        ___qtablewidgetitem5 = self.fl_table.item(2, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"00.0", None));
        ___qtablewidgetitem6 = self.fl_table.item(3, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Brake Temp", None));
        ___qtablewidgetitem7 = self.fl_table.item(3, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"00.0", None));
        self.fl_table.setSortingEnabled(__sortingEnabled)


        __sortingEnabled1 = self.fr_table.isSortingEnabled()
        self.fr_table.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.fr_table.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Wheel Speed", None));
        ___qtablewidgetitem9 = self.fr_table.item(0, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"0000", None));
        ___qtablewidgetitem10 = self.fr_table.item(1, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Torque", None));
        ___qtablewidgetitem11 = self.fr_table.item(1, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"0.0", None));
        ___qtablewidgetitem12 = self.fr_table.item(2, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Rot Pot", None));
        ___qtablewidgetitem13 = self.fr_table.item(2, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"00.0", None));
        ___qtablewidgetitem14 = self.fr_table.item(3, 0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Brake Temp", None));
        ___qtablewidgetitem15 = self.fr_table.item(3, 1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"00.0", None));
        self.fr_table.setSortingEnabled(__sortingEnabled1)


        __sortingEnabled2 = self.rl_table.isSortingEnabled()
        self.rl_table.setSortingEnabled(False)
        ___qtablewidgetitem16 = self.rl_table.item(0, 0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Wheel Speed", None));
        ___qtablewidgetitem17 = self.rl_table.item(0, 1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"0000", None));
        ___qtablewidgetitem18 = self.rl_table.item(1, 0)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Torque", None));
        ___qtablewidgetitem19 = self.rl_table.item(1, 1)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"0.0", None));
        ___qtablewidgetitem20 = self.rl_table.item(2, 0)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Rot Pot", None));
        ___qtablewidgetitem21 = self.rl_table.item(2, 1)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"00.0", None));
        ___qtablewidgetitem22 = self.rl_table.item(3, 0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Brake Temp", None));
        ___qtablewidgetitem23 = self.rl_table.item(3, 1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"00.0", None));
        self.rl_table.setSortingEnabled(__sortingEnabled2)


        __sortingEnabled3 = self.rr_table.isSortingEnabled()
        self.rr_table.setSortingEnabled(False)
        ___qtablewidgetitem24 = self.rr_table.item(0, 0)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Wheel Speed", None));
        ___qtablewidgetitem25 = self.rr_table.item(0, 1)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"0000", None));
        ___qtablewidgetitem26 = self.rr_table.item(1, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Torque", None));
        ___qtablewidgetitem27 = self.rr_table.item(1, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"0.0", None));
        ___qtablewidgetitem28 = self.rr_table.item(2, 0)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Rot Pot", None));
        ___qtablewidgetitem29 = self.rr_table.item(2, 1)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"00.0", None));
        ___qtablewidgetitem30 = self.rr_table.item(3, 0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Brake Temp", None));
        ___qtablewidgetitem31 = self.rr_table.item(3, 1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"00.0", None));
        self.rr_table.setSortingEnabled(__sortingEnabled3)

        self.label_5.setText("")
        self.lbl_cell_volt_alarm.setText(QCoreApplication.translate("MainWindow", u"Cell Voltage Alarm", None))
        self.lbl_coolant_temp_alarm.setText(QCoreApplication.translate("MainWindow", u"Coolant Temperature Alarm", None))
        self.lbl_coolant_flow_alarm.setText(QCoreApplication.translate("MainWindow", u"Coolant Flow Alarm", None))
        self.lbl_cell_temp_alarm.setText(QCoreApplication.translate("MainWindow", u"Cell Temperature Alarm", None))
        self.lbl_hv_batt_ok.setText(QCoreApplication.translate("MainWindow", u"HV Batt Ok", None))
        self.lbl_can_ok.setText(QCoreApplication.translate("MainWindow", u"CAN Ok", None))
        self.val_speed.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_kmh.setText(QCoreApplication.translate("MainWindow", u"km/h", None))
        self.val_soc.setText(QCoreApplication.translate("MainWindow", u"000 %", None))
        self.lbl_soc.setText(QCoreApplication.translate("MainWindow", u"SOC", None))
        self.val_inv_volt.setText(QCoreApplication.translate("MainWindow", u"000 V", None))
        self.lbl_inv_volt.setText(QCoreApplication.translate("MainWindow", u"Inverter", None))
        self.lbl_min_cell.setText(QCoreApplication.translate("MainWindow", u"Minimum\n"
"Cell Voltage", None))
        self.val_min_cell.setText(QCoreApplication.translate("MainWindow", u"0.00 V", None))
        self.lbl_max_igbt.setText(QCoreApplication.translate("MainWindow", u"Max\n"
"IGBT Temp", None))
        self.val_max_igbt.setText(QCoreApplication.translate("MainWindow", u"00.0 C", None))
        self.lbl_max_inv.setText(QCoreApplication.translate("MainWindow", u"Max\n"
"Inverter Temp", None))
        self.val_max_inv.setText(QCoreApplication.translate("MainWindow", u"00.0 C", None))
        self.lbl_max_motor.setText(QCoreApplication.translate("MainWindow", u"Max\n"
"Motor Temp", None))
        self.val_max_motor.setText(QCoreApplication.translate("MainWindow", u"00.0 C", None))
        self.tireFLLabel.setText(QCoreApplication.translate("MainWindow", u"FL", None))
        self.tireFLValue.setText(QCoreApplication.translate("MainWindow", u"84", None))
        self.tireFRLabel.setText(QCoreApplication.translate("MainWindow", u"FR", None))
        self.tireFRValue.setText(QCoreApplication.translate("MainWindow", u"82", None))
        self.tireRLLabel.setText(QCoreApplication.translate("MainWindow", u"RL", None))
        self.tireRLValue.setText(QCoreApplication.translate("MainWindow", u"91", None))
        self.tireRRLabel.setText(QCoreApplication.translate("MainWindow", u"RR", None))
        self.tireRRValue.setText(QCoreApplication.translate("MainWindow", u"93", None))
        self.tireTempSep.setProperty(u"role", QCoreApplication.translate("MainWindow", u"hsep", None))
        self.maxCellHeader.setText(QCoreApplication.translate("MainWindow", u"MAX CELL", None))
        self.maxCellHeader.setProperty(u"role", QCoreApplication.translate("MainWindow", u"sectionHeader", None))
        self.maxCellValue.setText(QCoreApplication.translate("MainWindow", u"43\u00b0", None))
        self.scaleLabel0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.scaleLabel0.setProperty(u"role", QCoreApplication.translate("MainWindow", u"scaleLabel", None))
        self.scaleLabel15.setText(QCoreApplication.translate("MainWindow", u"15", None))
        self.scaleLabel15.setProperty(u"role", QCoreApplication.translate("MainWindow", u"scaleLabel", None))
        self.scaleLabel30.setText(QCoreApplication.translate("MainWindow", u"30", None))
        self.scaleLabel30.setProperty(u"role", QCoreApplication.translate("MainWindow", u"scaleLabel", None))
        self.scaleLabel45.setText(QCoreApplication.translate("MainWindow", u"45", None))
        self.scaleLabel60.setText(QCoreApplication.translate("MainWindow", u"60", None))
        self.scaleLabelDQ.setText(QCoreApplication.translate("MainWindow", u"DQ", None))
        self.speedValue.setText(QCoreApplication.translate("MainWindow", u"72", None))
        self.speedUnit.setText(QCoreApplication.translate("MainWindow", u"KM / H", None))
        self.tirePSIHeader.setText(QCoreApplication.translate("MainWindow", u"TIRE PSI", None))
        self.tirePSIHeader.setProperty(u"role", QCoreApplication.translate("MainWindow", u"sectionHeader", None))
        self.psiFLLabel.setText(QCoreApplication.translate("MainWindow", u"FL", None))
        self.psiFLLabel.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cornerLabel", None))
        self.psiFLValue.setText(QCoreApplication.translate("MainWindow", u"12.4", None))
        self.psiFLValue.setProperty(u"role", QCoreApplication.translate("MainWindow", u"tireValueWhite", None))
        self.psiFRLabel.setText(QCoreApplication.translate("MainWindow", u"FR", None))
        self.psiFRLabel.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cornerLabel", None))
        self.psiFRValue.setText(QCoreApplication.translate("MainWindow", u"12.6", None))
        self.psiFRValue.setProperty(u"role", QCoreApplication.translate("MainWindow", u"tireValueWhite", None))
        self.psiRLLabel.setText(QCoreApplication.translate("MainWindow", u"RL", None))
        self.psiRLLabel.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cornerLabel", None))
        self.psiRLValue.setText(QCoreApplication.translate("MainWindow", u"12.1", None))
        self.psiRLValue.setProperty(u"role", QCoreApplication.translate("MainWindow", u"tireValueWhite", None))
        self.psiRRLabel.setText(QCoreApplication.translate("MainWindow", u"RR", None))
        self.psiRRLabel.setProperty(u"role", QCoreApplication.translate("MainWindow", u"cornerLabel", None))
        self.psiRRValue.setText(QCoreApplication.translate("MainWindow", u"12.2", None))
        self.psiRRValue.setProperty(u"role", QCoreApplication.translate("MainWindow", u"tireValueWhite", None))
        self.psiSep.setProperty(u"role", QCoreApplication.translate("MainWindow", u"hsep", None))
        self.socHeader.setText(QCoreApplication.translate("MainWindow", u"SOC", None))
        self.socHeader.setProperty(u"role", QCoreApplication.translate("MainWindow", u"sectionHeader", None))
        self.socValue.setText(QCoreApplication.translate("MainWindow", u"68%", None))
        self.brakeLabel.setText(QCoreApplication.translate("MainWindow", u"BRAKE", None))
        self.pitModeLabel.setText(QCoreApplication.translate("MainWindow", u"PIT MODE", None))
        self.throttleLabel.setText(QCoreApplication.translate("MainWindow", u"THROTTLE", None))
    # retranslateUi

