# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ExecuteWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ExecuteWindow(object):
    def setupUi(self, ExecuteWindow):
        ExecuteWindow.setObjectName("ExecuteWindow")
        ExecuteWindow.resize(471, 351)
        self.centralwidget = QtWidgets.QWidget(ExecuteWindow)
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
        ExecuteWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(ExecuteWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 471, 21))
        self.menubar.setObjectName("menubar")
        ExecuteWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(ExecuteWindow)
        self.statusbar.setObjectName("statusbar")
        ExecuteWindow.setStatusBar(self.statusbar)

        self.retranslateUi(ExecuteWindow)
        QtCore.QMetaObject.connectSlotsByName(ExecuteWindow)

    def retranslateUi(self, ExecuteWindow):
        _translate = QtCore.QCoreApplication.translate
        ExecuteWindow.setWindowTitle(_translate("ExecuteWindow", "MainWindow"))
        self.label.setText(_translate("ExecuteWindow", "Once you have entered the path for your files and clicked \"OK\", you can click \"EXECUTE\"."))
        self.pushButton.setText(_translate("ExecuteWindow", "EXECUTE"))
        self.pushButton_2.setText(_translate("ExecuteWindow", "OK"))
        self.label_2.setText(_translate("ExecuteWindow", "Enter the path for the files you will be converting below and then click \"OK\"."))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ExecuteWindow = QtWidgets.QMainWindow()
    ui = Ui_ExecuteWindow()
    ui.setupUi(ExecuteWindow)
    ExecuteWindow.show()
    sys.exit(app.exec_())

