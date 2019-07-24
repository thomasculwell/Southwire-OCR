# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sw-ocrgui.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(565, 422)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 543, 359))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.instructions_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.instructions_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.instructions_button.setObjectName("instructions_button")
        self.gridLayout_2.addWidget(self.instructions_button, 0, 0, 1, 1)
        self.conversion_button = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.conversion_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.conversion_button.setObjectName("conversion_button")
        self.gridLayout_2.addWidget(self.conversion_button, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 565, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.instructions_button.clicked.connect(self.show_instructions)
        self.conversion_button.clicked.connect(self.show_conversion)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.instructions_button.setText(_translate("MainWindow", "Instructions"))
        self.conversion_button.setText(_translate("MainWindow", "Conversion"))

    def show_instructions(self):
        msg = QMessageBox()
        msg.setWindowTitle('Instructions')
        msg.setText('text')

        x = msg.exec_()

    def show_conversion(self):
        msg = QMessageBox()
        msg.setWindowTitle('Conversion')
        msg.setText('text')

        x = msg.exec_()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

