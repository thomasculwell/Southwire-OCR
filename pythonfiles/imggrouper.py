# imggrouper.py

import os
import sys

file = 'new.tif'
command = 'C:\\PROGRA~1\\IrfanView\\i_view64.exe /multitif=(C:\\Users\\culwellt\\Documents\\southwireOCR\\tester\\' + file + ','

ptfilelist = ['1.1.jpg','2.1.jpg','5.1.jpg','6.1.jpg','6.2.jpg','6.3.jpg']

if len(ptfilelist) > 1:
    for ptfile in ptfilelist:
        command = command + 'C:\\Users\\culwellt\\Documents\\southwireOCR\\tester\\' + ptfile + ','

    os.system(command)