# This is a script starting after Reeve's suggestion.
# I will go step by step to find the best way to convert
# the image file to a text file and grab the essential
# text.

import os
import tempfile
import subprocess
import re
from PIL import Image

def rrcrop_ocr(img):
    temp = tempfile.NamedTemporaryFile(delete=False)

    original = Image.open(img)
    rr_cropped_img = original.crop((0, 0, 2200, 240))
    rr_cropped_img.save('test.tif')
    rr_cropped_img.show()

    #the 2nd argument needs to be a file not whatever it is now (variable)
    process = subprocess.Popen(['tesseract', 'test.tif', temp.name], \
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r', encoding = 'utf-8') as handle:
        contents = handle.read().split()
    os.remove(temp.name + '.txt')
    print(contents)
    for i in range(len(contents)):
        if (contents[i] == 'No.' or contents[i] == 'NO.' or contents[i] == 'N0.') \
        and (contents[i+2] == 'Page' or contents[i+2] == 'page'):
          print(re.match('[5][0][0]\d{7}', contents[i+1]).group())


def pocrop_ocr(img):
    temp = tempfile.NamedTemporaryFile(delete=False)

    original = Image.open(img)
    po_cropped_img = original.crop((0, 500, 1000, 700))
    # po_cropped_img.show()
    po_cropped_img.save('test1.tif')

    #the 2nd argument needs to be a file not whatever it is now (variable)
    process = subprocess.Popen(['tesseract', 'test1.tif', temp.name], \
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r', encoding = 'utf-8') as handle:
        contents = handle.read().split()

    os.remove(temp.name + '.txt')
    return contents


def dtcrop_ocr(img):
    temp = tempfile.NamedTemporaryFile(delete=False)

    original = Image.open(img)
    dt_cropped_img = original.crop((0, 200, 1200, 400))
    # date_cropped_img.show()
    dt_cropped_img.save('test2.tif')

    #the 2nd argument needs to be a file not whatever it is now (variable)
    process = subprocess.Popen(['tesseract', 'test2.tif', temp.name], \
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r', encoding = 'utf-8') as handle:
        contents = handle.read().split()

    os.remove(temp.name + '.txt')
    return contents

def ocr(imgfile):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', imgfile, temp.name], \
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r', encoding = 'utf-8') as handle:
        contents = handle.read().split()

    os.remove(temp.name + '.txt')
    return contents

def grab(txt):
  for i in range(len(txt)):
      # this finds the receiving report number
      if (txt[i] == 'No.' or txt[i] == 'NO.' or txt[i] == 'N0.') \
      and (txt[i+2] == 'Page' or txt[i+2] == 'page'):
          print(re.match('[5][0][0]\d{7}', txt[i+1]).group())
      # this finds the purchasing order number
      elif (txt[i] == 'PO' or txt[i] =='P0' or txt[i] =='Po' \
      or txt[i] == 'pO' or txt[i] == 'p0' or txt[i] == 'po') \
      and (txt[i+1] == ':'):
          print(re.match('[4][5][0]\d{7}', txt[i+2]).group())
      # this finds the goods receipt date
      elif txt[i] == 'receipt' and txt[i+1] == 'date' and txt[i+2] == ':':
          print(re.match('[01]\d\/[0123]\d\/[12]\d{3}', txt[i+3]).group())

filename = '300x300.tif'

# alltxt = ocr(filename)
rrcrop_ocr(filename)
# potxt = pocrop_ocr(filename)
# dttxt = dtcrop_ocr(filename)
# print(rrtxt)
# print(potxt)
# print(dttxt)
# grab(alltxt)
# now call the grab function, may want to add grab function into all
# other functions




