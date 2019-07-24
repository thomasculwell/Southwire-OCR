# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'StartProgramWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_StartProgramWindow(object):
    def setup(self, StartProgramWindow):
        StartProgramWindow.setObjectName("StartProgramWindow")
        StartProgramWindow.resize(471, 351)
        self.centralwidget = QtWidgets.QWidget(StartProgramWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 5, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 6, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 0, 1, 1)
        StartProgramWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(StartProgramWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 21))
        self.menubar.setObjectName("menubar")
        StartProgramWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(StartProgramWindow)
        self.statusbar.setObjectName("statusbar")
        StartProgramWindow.setStatusBar(self.statusbar)

        self.retranslateUi(StartProgramWindow)
        QtCore.QMetaObject.connectSlotsByName(StartProgramWindow)

    def retranslateUi(self, StartProgramWindow):
        _translate = QtCore.QCoreApplication.translate
        StartProgramWindow.setWindowTitle(_translate("StartProgramWindow", "Start Program"))
        self.label.setText(_translate("StartProgramWindow", "Once you have entered the path for your files and clicked \"OK\", you can click \"EXECUTE\"."))
        self.pushButton.setText(_translate("StartProgramWindow", "EXECUTE"))
        self.pushButton_2.setText(_translate("StartProgramWindow", "OK"))
        self.label_2.setText(_translate("StartProgramWindow", "Enter the path for the files you will be converting below and then click \"OK\"."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StartProgramWindow = QtWidgets.QStartProgramWindow()
    ui = Ui_StartProgramWindow()
    ui.setup(StartProgramWindow)
    StartProgramWindow.show()
    sys.exit(app.exec_())

