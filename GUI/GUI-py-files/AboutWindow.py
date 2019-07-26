# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'aboutWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

about_label = """Name:      Southwire ApplicationXtender Automation GUI
Version:   GUI running on version 21 from sw-ocr(version).py
Creator:   Thomas Culwell"""

class Ui_aboutWindow(object):
    def setup(self, aboutWindow):

        aboutWindow.setObjectName("aboutWindow")
        aboutWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(aboutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 780, 539))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")

        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        aboutWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(aboutWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        aboutWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(aboutWindow)
        self.statusbar.setObjectName("statusbar")
        aboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(aboutWindow)
        QtCore.QMetaObject.connectSlotsByName(aboutWindow)

    def retranslateUi(self, aboutWindow):
        _translate = QtCore.QCoreApplication.translate
        aboutWindow.setWindowTitle(_translate("aboutWindow", "aboutWindow"))
        self.label.setText(_translate("aboutWindow", about_label))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    aboutWindow = QtWidgets.QaboutWindow()
    ui = Ui_aboutWindow()
    ui.setup(aboutWindow)
    aboutWindow.show()
    sys.exit(app.exec_())
