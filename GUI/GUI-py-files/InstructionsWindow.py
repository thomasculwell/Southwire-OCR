# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'InstructionsWindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

instructions_label = """Instructions for Southwire ApplicationXtender Automation Program

Installations and Downloads
1.  Install Anaconda through this link:
        a.  https://www.anaconda.com/distribution/
        b.  You should be downloading the python 3.7, 64-bit version for windows (assuming you are working on a windows computer)
        c.  When the setup screen starts, click next.
        d.  Click “I agree” to the terms and conditions.
        e.  Choose “Just me” when asked who to install for. Click Next.
        f.  Click Next when it shows the destination folder.
        g.  In advanced options, check “Register Anaconda as my default Python 3.7” and do NOT check “add anaconda to my PATH environment variable”. Click Install.
        h.  Once installed, click next. Then click next again.
        i.  Uncheck learn more about anaconda cloud and uncheck learn how to get started with anaconda unless you would like to read more about it. Click Finish.
2.  Install Google’s OCR engine for python, Pytesseract
        a.  Open anaconda prompt in windows
        b.  You can do this by going to your computer’s search bar and searching “anaconda” and it should pop up.
        c.  Type “pip install pytesseract” and hit enter
        d.  Wait for pytesseract to install. You will know it is done when a new (base) line appears and you can type again.
3.  Install python’s imaging package, PIL
        a.  In anaconda prompt, type “pip install pillow” and hit enter.
        b.  Wait for PIL to install. You will know it is done when a new (base) line appears and you can type again.
4.  Download IrfanView image editor for windows with the following link:
        a.  https://www.irfanview.com/64bit.htm
        b.  Download the following option: IrfanView-64 English (Version 4.53, extracting EXE file, 3.42 MB)
        c.  When the setup screen shows up, do the following:
        d.  Under create shortcuts, check all 3 options and mark “for current user only”. Click next.
        e.  Under “do you want to associate extensions with IrfanView?” do not change anything and click next.
        f.  Under “destination directory” keep the defaults selected “user’s application data folder” and click next.
        g.  Click done.


Scanning Files
As you should know, only the delivery tickets accompanied by their essential information (receiving report #, PO#, person, and date) are uploaded to ApplicationXtender,
but in order to find the essential information for these delivery tickets, my program needs to access the accompanying goods receipts. This is because the goods receipts
have the receiving report number, purchase order number, person who received, and date in the same place every time. Since this is the case, you will need to scan both the
goods receipts and the delivery tickets in a particular order (and make sure they are in the correct order before you run the program). The files must be in the following
order for the program to work correctly:
1.  The goods receipt(s) that matches with each delivery ticket(s) must come before the delivery ticket for each one.
        a. For example, if I wanted to upload 3 delivery tickets to ApplicationXtender, my files must be ordered like the following:
                i.  Goods receipt 1, Delivery ticket 1, Goods receipt 2, Delivery ticket 2, Goods receipt 3, Delivery ticket 3 where GR1 matches with DT1, GR2 matches with DT2,
                    and GR3 matches with DT3.
                ii. Goods receipt 1 may have multiple files as might any of the others, but as long as they are in order the program will still run correctly.
2.  When scanning your documents, make sure that you save them as .jpg files, and try to save them with 600x600dpi. This will improve the file quality and resolution which
    will improve results.
3.  Once you have a folder with all of your files in this particular order, add the python file to this same folder.


Running the Program
1.  Open Anaconda Prompt.
2.  Navigate to the directory (folder) that holds all of your files.
        a.  To do this, use command “cd” followed by a space and then the name of the next directory you want to access.
            i.  For example, if you are in the documents directory and want to go into a folder called “folder1” that is located inside of the documents directory, simply type
                “cd folder1” and press enter in the anaconda prompt, and it will navigate to that directory.
        b.  If all of your files are in a deeply nested folder (one that is located in several other folders), continue to use “cd foldername” to navigate to the correct folder.
            i.  For example, if your files were in documents → thomas → southwireocr → applicationxtender, then to get to that directory you would type “cd documents” enter
                “cd thomas” enter “cd southwireocr” enter “cd applicationxtender” enter.
                        OR 
                “cd documents/thomas/southwireocr/applicationxtender”
        c.  If you go into the wrong folder, you can go back a directory by typing “cd..” and pressing enter.
        d.  You should always check the directory in which your anaconda prompt starts you off in, because you will have to navigate from that starting directory each time.
        e.  If you need help with anaconda/command prompt syntax for windows, simply google “windows command prompt syntax” or take a look at this link: https://www.thomas-krenn.com/en/wiki/Cmd_commands_under_Windows
3.  Once you have navigated to the correct directory (the directory that holds your .jpg files and the python file) in anaconda, now just type the command “python pythonfilename” and press enter.
        a.  pythonfilename is simply just the name of the python file you are using. If it hasn’t been renamed, it should be called sw-ocr.py, so you would type “python sw-ocr.py” and press enter.
4.  Once you have called the python file and told it to run, the program will begin to change the names of your files in the current directory, and it will eventually output a .txt file and several .tif files that
    correspond to the lines in the .txt file. 
5.  Leave the anaconda prompt open until the program is completely done running. You will know it is done running when there is a new line in the anaconda prompt to type a new command. 
        a. For reference, my program typically takes about one minute for each 8-10 files. So if you were to do 200 files at once, it would take the program approximately 20-25 minutes.
        b. Once the program is completely done running, you can now open the .txt file to see if any mistakes were made. If so, manually correct these before sending it and the accompanying .tif files to Rachel Argo.


Descriptions
Anaconda - “Anaconda is a free and open-source distribution of the Python and R programming languages for scientific computing, that aims to simplify package management and deployment.” - Wikipedia
Pytesseract - “It will recognize and read the text present in images. It can read all image types - png, jpeg, gif, tiff, bmp etc. It’s widely used to process everything from scanned documents.” - MicroPyramid
PIL - “PIL is the Python Imaging Library by Fredrik Lundh and Contributors.” - Pillow
IrfanView - “IrfanView is a fast, compact and innovative FREEWARE (for non-commercial use) graphic viewer for Windows XP, Vista, 7, 8 and 10.” - IrfanView
Directory - basically the same thing as a folder"""

class Ui_InstructionsWindow(object):
    def setup(self, Instructions):
        Instructions.setObjectName("Instructions")
        Instructions.resize(653, 485)
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
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 631, 394))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.label.setObjectName("label")
        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 1, 0, 1, 1)
        Instructions.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Instructions)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 653, 21))
        self.menubar.setObjectName("menubar")
        Instructions.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Instructions)
        self.statusbar.setObjectName("statusbar")
        Instructions.setStatusBar(self.statusbar)

        self.retranslateUi(Instructions)
        QtCore.QMetaObject.connectSlotsByName(Instructions)

    def retranslateUi(self, Instructions):
        _translate = QtCore.QCoreApplication.translate
        Instructions.setWindowTitle(_translate("Instructions", "Instructions"))
        self.label.setText(_translate("Instructions", instructions_label))
        self.pushButton.setText(_translate("Instructions", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Instructions = QtWidgets.QMainWindow()
    ui = Ui_Instructions()
    ui.setup(Instructions)
    Instructions.show()
    sys.exit(app.exec_())

