# filechange.py

# Changes the files to a numerical order.

import os, sys, glob

filenames = glob.glob('*.jpg')



# The following is a for loop that iterates through every file in filenames
# and places all of the gr files into the grfilenames list and all of the
# pt files into the ptfilenames list based on the OCR'd corner of the page.


counter = 1
for file in filenames:
    os.rename(file, str(counter) + '.jpg')
    counter += 1