# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from ExecuteWindow import *
from InstructionsWindow import *
from AboutWindow import *

class Ui_MainWindow(object):
    def startprogram(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_StartProgramWindow()
        self.ui.setup(self.window)
        self.window.show()
    def instructions(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_InstructionsWindow()
        self.ui.setup(self.window)
        self.window.show()
    def about(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_AboutWindow()
        self.ui.setup(self.window)
        self.window.show()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(336, 316)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.about_button = QtWidgets.QPushButton(self.centralwidget)
        self.about_button.setObjectName("about_button")
        self.about_button.clicked.connect(self.about)
        self.gridLayout.addWidget(self.about_button, 3, 0, 1, 1)
        self.instructions_button = QtWidgets.QPushButton(self.centralwidget)
        self.instructions_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.instructions_button.setObjectName("instructions_button")
        self.instructions_button.clicked.connect(self.instructions)
        self.gridLayout.addWidget(self.instructions_button, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.startprogram_button = QtWidgets.QPushButton(self.centralwidget)
        self.startprogram_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.startprogram_button.setObjectName("startprogram_button")
        self.startprogram_button.clicked.connect(self.startprogram)
        self.gridLayout.addWidget(self.startprogram_button, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 336, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Southwire ApplicationXtender Automation GUI"))
        self.about_button.setText(_translate("MainWindow", "About"))
        self.instructions_button.setText(_translate("MainWindow", "Instructions"))
        self.label.setText(_translate("MainWindow", "Southwire ApplicationXtender Automation GUI"))
        self.startprogram_button.setText(_translate("MainWindow", "Start Program"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

