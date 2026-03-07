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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHeaderView, QLabel,
    QMainWindow, QPlainTextEdit, QSizePolicy, QStackedWidget,
    QStatusBar, QTableWidget, QTableWidgetItem, QWidget)

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
        self.stackedWidget.setGeometry(QRect(10, 11, 771, 441))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.speedbar = QWidget(self.page)
        self.speedbar.setObjectName(u"speedbar")
        self.speedbar.setEnabled(True)
        self.speedbar.setGeometry(QRect(310, 30, 81, 371))
        self.speedbar.setMaximumSize(QSize(100, 16777215))
        self.speedbar.setStyleSheet(u"background-color:rgb(255, 41, 3)")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(670, 410, 91, 31))
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(310, 410, 91, 31))
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.throttlebar = QWidget(self.page)
        self.throttlebar.setObjectName(u"throttlebar")
        self.throttlebar.setEnabled(True)
        self.throttlebar.setGeometry(QRect(670, 30, 81, 371))
        self.throttlebar.setMaximumSize(QSize(100, 16777215))
        self.throttlebar.setStyleSheet(u"background-color:rgb(7, 255, 3)")
        self.frontbrakebar = QWidget(self.page)
        self.frontbrakebar.setObjectName(u"frontbrakebar")
        self.frontbrakebar.setEnabled(True)
        self.frontbrakebar.setGeometry(QRect(0, 30, 81, 371))
        self.frontbrakebar.setMaximumSize(QSize(100, 16777215))
        self.frontbrakebar.setStyleSheet(u"background-color:rgb(58, 143, 255)")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 410, 91, 31))
        self.label.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(110, 410, 91, 31))
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255)")
        self.rearbrakebar = QWidget(self.page)
        self.rearbrakebar.setObjectName(u"rearbrakebar")
        self.rearbrakebar.setEnabled(True)
        self.rearbrakebar.setGeometry(QRect(120, 30, 81, 371))
        self.rearbrakebar.setMaximumSize(QSize(100, 16777215))
        self.rearbrakebar.setStyleSheet(u"background-color:rgb(58, 143, 255)")
        self.plainTextEdit = QPlainTextEdit(self.page)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(460, 130, 104, 261))
        self.plainTextEdit.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.stackedWidget.addWidget(self.page)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.stackedWidget.addWidget(self.page_3)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.CVT_table = QTableWidget(self.page_2)
        if (self.CVT_table.columnCount() < 2):
            self.CVT_table.setColumnCount(2)
        if (self.CVT_table.rowCount() < 6):
            self.CVT_table.setRowCount(6)
        __qtablewidgetitem = QTableWidgetItem()
        self.CVT_table.setItem(0, 0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.CVT_table.setItem(0, 1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.CVT_table.setItem(1, 0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.CVT_table.setItem(1, 1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.CVT_table.setItem(2, 0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.CVT_table.setItem(2, 1, __qtablewidgetitem5)
        font = QFont()
        font.setPointSize(19)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font);
        self.CVT_table.setItem(3, 0, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.CVT_table.setItem(3, 1, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.CVT_table.setItem(4, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.CVT_table.setItem(4, 1, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.CVT_table.setItem(5, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.CVT_table.setItem(5, 1, __qtablewidgetitem11)
        self.CVT_table.setObjectName(u"CVT_table")
        self.CVT_table.setEnabled(True)
        self.CVT_table.setGeometry(QRect(200, 100, 401, 321))
        self.CVT_table.setFont(font)
        self.CVT_table.setStyleSheet(u"\n"
"color: rgb(255, 255, 255);\n"
"")
        self.CVT_table.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CVT_table.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.CVT_table.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContentsOnFirstShow)
        self.CVT_table.setRowCount(6)
        self.CVT_table.setColumnCount(2)
        self.CVT_table.horizontalHeader().setVisible(False)
        self.CVT_table.horizontalHeader().setCascadingSectionResizes(True)
        self.CVT_table.horizontalHeader().setDefaultSectionSize(250)
        self.CVT_table.horizontalHeader().setHighlightSections(True)
        self.CVT_table.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.CVT_table.horizontalHeader().setStretchLastSection(True)
        self.CVT_table.verticalHeader().setVisible(False)
        self.CVT_table.verticalHeader().setDefaultSectionSize(50)
        self.CVT_table.verticalHeader().setStretchLastSection(False)
        self.charging_status_light = QWidget(self.page_2)
        self.charging_status_light.setObjectName(u"charging_status_light")
        self.charging_status_light.setGeometry(QRect(230, 0, 41, 41))
        self.charging_status_light.setStyleSheet(u"background-color: rgb(255, 14, 30);\n"
"border-radius: 20px\n"
"")
        self.balancing_status_light = QWidget(self.page_2)
        self.balancing_status_light.setObjectName(u"balancing_status_light")
        self.balancing_status_light.setGeometry(QRect(230, 50, 41, 41))
        self.balancing_status_light.setStyleSheet(u"background-color: rgb(255, 14, 30);\n"
"border-radius: 20px\n"
"")
        self.label_5 = QLabel(self.page_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(280, 0, 221, 41))
        font1 = QFont()
        font1.setPointSize(17)
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.label_6 = QLabel(self.page_2)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(280, 50, 221, 41))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"color:rgb(255, 255, 255)")
        self.stackedWidget.addWidget(self.page_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionsettings.setText(QCoreApplication.translate("MainWindow", u"settings", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Throttle", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Speed", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Front Brake", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Rear Brake", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("MainWindow", u"Stats for the car:\n"
"\n"
"\n"
".\n"
".\n"
".\n"
".\n"
".\n"
"", None))

        __sortingEnabled = self.CVT_table.isSortingEnabled()
        self.CVT_table.setSortingEnabled(False)
        ___qtablewidgetitem = self.CVT_table.item(0, 0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Current", None));
        ___qtablewidgetitem1 = self.CVT_table.item(0, 1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"0A", None));
        ___qtablewidgetitem2 = self.CVT_table.item(1, 0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Voltage", None));
        ___qtablewidgetitem3 = self.CVT_table.item(1, 1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"0V", None));
        ___qtablewidgetitem4 = self.CVT_table.item(2, 0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Min Cell Temp.", None));
        ___qtablewidgetitem5 = self.CVT_table.item(2, 1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"0 C", None));
        ___qtablewidgetitem6 = self.CVT_table.item(3, 0)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Max Cell Temp.", None));
        ___qtablewidgetitem7 = self.CVT_table.item(3, 1)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"0V", None));
        ___qtablewidgetitem8 = self.CVT_table.item(4, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Min Cell Volt.", None));
        ___qtablewidgetitem9 = self.CVT_table.item(4, 1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"0V", None));
        ___qtablewidgetitem10 = self.CVT_table.item(5, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Max Cell Volt.", None));
        ___qtablewidgetitem11 = self.CVT_table.item(5, 1)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"0V", None));
        self.CVT_table.setSortingEnabled(__sortingEnabled)

        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Charging Status", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Balancing Status", None))
    # retranslateUi

