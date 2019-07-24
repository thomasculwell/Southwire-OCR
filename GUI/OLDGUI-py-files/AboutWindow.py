# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AboutWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_AboutWindow(object):
    def setupUi(self, AboutWindow):
        AboutWindow.setObjectName("AboutWindow")
        AboutWindow.resize(414, 369)
        self.centralwidget = QtWidgets.QWidget(AboutWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 394, 308))
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
        AboutWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(AboutWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 414, 21))
        self.menubar.setObjectName("menubar")
        AboutWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(AboutWindow)
        self.statusbar.setObjectName("statusbar")
        AboutWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AboutWindow)
        QtCore.QMetaObject.connectSlotsByName(AboutWindow)

    def retranslateUi(self, AboutWindow):
        _translate = QtCore.QCoreApplication.translate
        AboutWindow.setWindowTitle(_translate("AboutWindow", "MainWindow"))
        self.label.setText(_translate("AboutWindow", "about_label"))
        self.pushButton.setText(_translate("AboutWindow", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AboutWindow = QtWidgets.QMainWindow()
    ui = Ui_AboutWindow()
    ui.setupUi(AboutWindow)
    AboutWindow.show()
    sys.exit(app.exec_())

