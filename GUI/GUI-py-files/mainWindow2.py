# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow2.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtCore, QtGui, QtWidgets
from ExecuteWindow import *
from InstructionsWindow import *
from AboutWindow import *



# pathvar = 'hello'

class Ui_MainWindow(object):
    global pathvar
    # pathvar = ''

    def enterPath(self):
        global pathvar
        self.dialog = QtWidgets.QInputDialog()
        text, ok = QtWidgets.QInputDialog.getText(self.dialog, 'Path Dialog', 'Enter Path:')
        if ok and text != '':
            pathvar = text
            print(pathvar)
    def execute(self):
        global pathvar
        import swocr21
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
        
        # MainWindow
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(400, 300)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")

        # About Button
        self.aboutButton = QtWidgets.QPushButton(self.centralwidget)
        self.aboutButton.setObjectName("aboutButton")
        self.aboutButton.clicked.connect(self.about)
        self.gridLayout.addWidget(self.aboutButton, 4, 0, 1, 1)

        # Execute Button
        self.executeButton = QtWidgets.QPushButton(self.centralwidget)
        self.executeButton.setObjectName("executeButton")
        self.executeButton.clicked.connect(self.execute)
        self.gridLayout.addWidget(self.executeButton, 1, 0, 1, 1)

        # Instructions Button
        self.instructionsButton = QtWidgets.QPushButton(self.centralwidget)
        self.instructionsButton.setObjectName("instructionsButton")
        self.instructionsButton.clicked.connect(self.instructions)
        self.gridLayout.addWidget(self.instructionsButton, 3, 0, 1, 1)

        # Enter Path Button
        self.enterPathButton = QtWidgets.QPushButton(self.centralwidget)
        self.enterPathButton.setObjectName("enterPathButton")
        self.enterPathButton.clicked.connect(self.enterPath)
        self.gridLayout.addWidget(self.enterPathButton, 2, 0, 1, 1)

        # Title Label
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.aboutButton.setText(_translate("MainWindow", "About"))
        self.executeButton.setText(_translate("MainWindow", "Execute"))
        self.instructionsButton.setText(_translate("MainWindow", "Instructions"))
        self.enterPathButton.setText(_translate("MainWindow", "Enter Path"))
        self.label.setText(_translate("MainWindow", "Southwire ApplicationXtender Automation GUI"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

