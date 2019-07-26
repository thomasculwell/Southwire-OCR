# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'PathDialog.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PATH(object):
    def setup(self, PATH):
        PATH.setObjectName("PATH")
        PATH.resize(400, 300)
        self.gridLayout = QtWidgets.QGridLayout(PATH)
        self.gridLayout.setObjectName("gridLayout")
        self.buttonBox = QtWidgets.QDialogButtonBox(PATH)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 1)
        self.label = QtWidgets.QLabel(PATH)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(PATH)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.retranslateUi(PATH)
        self.buttonBox.accepted.connect(PATH.accept)
        self.buttonBox.rejected.connect(PATH.reject)
        QtCore.QMetaObject.connectSlotsByName(PATH)


    def retranslateUi(self, PATH):
        _translate = QtCore.QCoreApplication.translate
        PATH.setWindowTitle(_translate("PATH", "Dialog"))
        self.label.setText(_translate("PATH", "Enter the Path for your files in the following text box and then press \"OK\"."))

    def getText(self):
        text, okPressed = QInputDialog.getText(self, "Get text","Your name:", QLineEdit.Normal, "")
        if okPressed and text != '':
            print(text)

    def ok_pressed(self):
    	self.getText()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    PATH = QtWidgets.QDialog()
    ui = Ui_PATH()
    ui.setup(PATH)
    PATH.show()
    sys.exit(app.exec_())

