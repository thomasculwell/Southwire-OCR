# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InstructionsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Instructions(object):
    def setupUi(self, Instructions):
        Instructions.setObjectName("Instructions")
        Instructions.resize(679, 560)
        self.centralwidget = QtWidgets.QWidget(Instructions)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(10, 10, 10, 10)
        self.gridLayout.setSpacing(5)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 657, 497))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 1, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        Instructions.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Instructions)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 679, 21))
        self.menubar.setObjectName("menubar")
        Instructions.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Instructions)
        self.statusbar.setObjectName("statusbar")
        Instructions.setStatusBar(self.statusbar)

        self.retranslateUi(Instructions)
        QtCore.QMetaObject.connectSlotsByName(Instructions)

    def retranslateUi(self, Instructions):
        _translate = QtCore.QCoreApplication.translate
        Instructions.setWindowTitle(_translate("Instructions", "MainWindow"))
        self.label.setText(_translate("Instructions", "instructions_label"))
        self.pushButton.setText(_translate("Instructions", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Instructions = QtWidgets.QMainWindow()
    ui = Ui_Instructions()
    ui.setupUi(Instructions)
    Instructions.show()
    sys.exit(app.exec_())

