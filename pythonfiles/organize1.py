# organize1.py

# This python script is made to organize/rename file in a way
# that will be convenient to run my culmination.py file on them.

import os
import re
import sys
from PIL import Image
import pytesseract
from collections import defaultdict

# i = 1
# for filename in os.listdir('.'):
#     if filename.startswith('3014'):
#         os.rename(filename, 'GR' + str(i) + '.jpg') 
#     i += 1

# while i < (len(os.listdir()) - 1):

def cropocr(img):
    original = Image.open(img)

    dpi = original.info['dpi']
    # print(dpi)
    if dpi == (600,600):
        l,u,r,d = 2800,0,5200,500
    elif dpi == (400,400):
        l,u,r,d = 2000,0,3400,333
    elif dpi == (300,300):
        l,u,r,d = 1500,0,2550,250
    else:
        l,u,r,d = 3000,0,5000,500

    cropped_img = original.crop((l,u,r,d))
    cropped_img.save('test.jpg')
    # cropped_img.show()

    croptext = pytesseract.image_to_string(Image.open('test.jpg'))
    rrlist = croptext.split()
    # print(rrlist)

    global isgr

    if rrlist == []:
        isgr = False

    try:
        for i in range(len(rrlist)):
            if (rrlist[i]=='No.' or rrlist[i]=='NO.' or rrlist[i]=='N0.' \
            or rrlist[i]=='no.' or rrlist[i]=='nO.' or rrlist[i]=='n0.') \
            and (rrlist[i+2] == 'Page' or rrlist[i+2] == 'page') \
            and re.match('[5][0][0]\d{7}', rrlist[i+1]) is not None:
                isgr = True
                break
            elif (rrlist[i]=='No.' or rrlist[i]=='NO.' or rrlist[i]=='N0.' \
            or rrlist[i]=='no.' or rrlist[i]=='nO.' or rrlist[i]=='n0.') \
            and re.match('[5][0][0]\d{7}', rrlist[i+1]) is not None:
                isgr = True
                break
            elif re.match('[5][0][0]\d{7}', rrlist[i]) is not None:
                isgr = True
                break
            else:
                isgr = False
    except:
        isgr = False

    os.remove('test.jpg')
    # print(isgr)
def fullocr(img):
    fulltext = pytesseract.image_to_string(Image.open(img))
    fulllist = fulltext.split()
    # print(fulllist)

    global isgr2

    if fulllist == []:
        isgr2 = False

    try:
        for i in range(len(fulllist)):
            if (fulllist[i]=='No.' or fulllist[i]=='NO.' or fulllist[i]=='N0.' \
            or fulllist[i]=='no.' or fulllist[i]=='nO.' or fulllist[i]=='n0.') \
            and (fulllist[i+2] == 'Page' or fulllist[i+2] == 'page') \
            and re.match('[5][0][0]\d{7}', fulllist[i+1]) is not None:
                isgr2 = True
                break
            elif (fulllist[i]=='No.' or fulllist[i]=='NO.' or fulllist[i]=='N0.' \
            or fulllist[i]=='no.' or fulllist[i]=='nO.' or fulllist[i]=='n0.') \
            and re.match('[5][0][0]\d{7}', fulllist[i+1]) is not None:
                isgr2 = True
                break
            elif re.match('[5][0][0]\d{7}', fulllist[i]) is not None:
                isgr2 = True
                break
            else:
                isgr2 = False
    except:
        isgr2 = False
    # print(isgr2)
filenames = ['3015_001.jpg','3015_002.jpg','3015_003.jpg','3015_004.jpg',\
'3015_005.jpg','3015_006.jpg','3015_007.jpg','3015_008.jpg','3015_009.jpg',\
'3015_010.jpg','3015_011.jpg','3015_012.jpg','3015_013.jpg']


counter = 1
for file in filenames:
    cropocr(file)
    fullocr(file)
    
    if isgr == isgr2 and isgr == True:
        # print(str(file) + '. GR? ' + str(isgr))
        os.rename(file, str(counter) + '.jpg')
        counter += 1
        counter2 = 1
    elif isgr == isgr2 and isgr == False:
        # print(str(file) + '. GR? ' + str(isgr) + ' for both scans.')
        os.rename(file, str((counter - 1)) + '.' + str(counter2) \
        +  '.jpg')
        counter2 += 1
print(filenames)
