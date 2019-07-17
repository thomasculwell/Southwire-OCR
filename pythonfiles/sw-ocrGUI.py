# sw-ocrGUI.py

import sys
from typing import *
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QLabel,
    QPushButton,
    QHBoxLayout,
    QVBoxLayout,
    QListView,
    QAbstractItemView,
    QMessageBox,
    QLineEdit,
    QTableView, QDialog, qApp, QGroupBox, QFormLayout, QDialogButtonBox)
from PyQt5.QtGui import (
    QStandardItemModel,
    QStandardItem,
    QPixmap)
from pprint import pprint

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Southwire-ApplicationXtender Automation GUI')
        self.show_instructions_button = QPushButton('Instructions')
        self.show_instructions_button.setEnabled(True)
        # self.table_view.clicked.connect(self.enable_show_pet_item_button)
        self.show_instructions_button.clicked.connect(self.show_instructions_button)
        
        
        self.start = QPushButton('Start')
        self.start.setEnabled(True)
        # self.table_view.clicked.connect(self.enable_show_shelter_item_button)
        self.start.clicked.connect(self.start)
        

        vbox = QVBoxLayout()
        # vbox.addWidget(self.table_view)
        vbox.addWidget(self.show_instructions_button)
        vbox.addWidget(self.show_start_button)
        self.setLayout(vbox)

    def instructionsButton(self):
        instructionsWindow().exec()

    def start(self):
        startWindow().exec()



    def show_pet_item(self):
        current_pet_index = self.table_view.currentIndex().row()
        selected_pet_item = self.table_model.row(current_pet_index)
        PetDetailsDialog(selected_pet_item).exec()

    def show_instructions_button(self):
        instructionsWindow().exec()




class instructionsWindow(QDialog):
    def __init__(self):
        super(InstructionsWindow, self).__init__()
        self.setWindowTitle('Instructions')

class startWindow(QDialog):
    def __init__(self):
        super(startWindow, self).__init__()
        self.setWindowTitle ('Start')




if __name__=='__main__':
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())




