# sw-ocrGUI.py


import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MainWindow(QWidget):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.window.setWindowTitle('Southwire ApplicationXtender Automation')

        self.instructions_button = QPushButton('Instructions')
        self.instructions_button.clicked.connect(self.instructions_function)

        self.convert_button = QPushButton('Convert')
        self.convert_button.clicked.connect(self.convert_function)
        
        self.layout.addWidget(self.instructions_button)
        self.layout.addWidget(self.convert_button)
        self.window.setLayout(self.layout)
        self.window.show()

    def instructions_function(self):
        Instructions().exec()

    def convert_function(self):
        Convert().exec()


class Instructions(QWidget):
    def __init__(self):
        super(Instructions, self).__init__()

        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.window.setWindowTitle('Instructions')

        self.blahbutton = QPushButton('blah')
        self.layout.addWidget(self.blahbutton)
        self.window.setLayout(self.layout)
        self.window.show()


class Convert(QWidget):
    def __init__(self):
        super(Convert, self).__init__()

        self.window = QWidget()
        self.layout = QVBoxLayout()
        self.window.setWindowTitle('Convert')

        self.blahbutton = QPushButton('blah')
        self.layout.addWidget(self.blahbutton)
        self.window.setLayout(self.layout)
        self.window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())




# app = QApplication([])
# window = QWidget()
# layout = QVBoxLayout()

# instructions_botton = QPushButton('Instructions')
# convert_button = QPushButton('Convert')
# instructions_botton.clicked.connect(instructions_function)

# layout.addWidget(instructions_botton)
# layout.addWidget(convert_button)
# window.setLayout(layout)

# window.show()


# app.exec_()