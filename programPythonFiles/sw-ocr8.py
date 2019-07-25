# sw-ocr8.py
# Minor accuracy changes

import os
import re
import sys
from PIL import Image
import pytesseract


# The following function takes a jpg image as input, crops that image
# down to a smaller section around the Receiving Report #, pulls the text
# from that image, stores the text in a list, separated by spaces, and then
# searches for the Receiving Report #.

def rrcrop_ocr(img):
    original = Image.open(img)
    rr_cropped_img = original.crop((3000, 0, 5000, 500))
    rr_cropped_img.save('test.jpg')
    # rr_cropped_img.show()

    rrtext = pytesseract.image_to_string(Image.open('test.jpg'))
    rrlist = rrtext.split()
    # print(rrlist)

    global rr

    if rrlist == []:
        rr = 'No Receiving Report # Found'

    try:
        for i in range(len(rrlist)):
            if (rrlist[i]=='No.' or rrlist[i]=='NO.' or rrlist[i]=='N0.' \
            or rrlist[i]=='no.' or rrlist[i]=='nO.' or rrlist[i]=='n0.') \
            and (rrlist[i+2] == 'Page' or rrlist[i+2] == 'page'):
                rr = re.match('[5][0][0]\d{7}', rrlist[i+1]).group()
                break
            else:
                rr = 'No Receiving Report # Found'
    except:
        rr = 'No Receiving Report # Found'

    os.remove('test.jpg')
    # print(rr)




# The following function takes a jpg image as input, crops that image
# down to a smaller section around the Purchase Order #, pulls the text
# from that image, stores the text in a list, separated by spaces, and then
# searches for the Purchase Order #.

def pocrop_ocr(img):
    original = Image.open(img)
    po_cropped_img = original.crop((0, 800, 3000, 1400))
    po_cropped_img.save('test2.jpg')
    # po_cropped_img.show()

    potext = pytesseract.image_to_string(Image.open('test2.jpg'))
    polist = potext.split()
    # print(polist)

    global po

    if polist == []:
        po = 'No Purchase Order # Found'

    try:
        for i in range(len(polist)):
            if (polist[i]=='PO' or polist[i]=='P0' or polist[i]=='Po' \
            or polist[i]=='pO' or polist[i]=='p0' or polist[i]=='po') \
            and (polist[i+1]==':' or polist[i+1]=='i' or polist[i+1]=='l' \
            or polist[i+1]=='I'):
                po = re.match('[4][5][0]\d{7}', polist[i+2]).group()
                break
            elif (polist[i]=='PO' or polist[i]=='P0' or polist[i]=='Po' \
            or polist[i]=='pO' or polist[i]=='p0' or polist[i]=='po') \
            and (polist[i+2]==':' or polist[i+2]=='i'):
                po = re.match('[4][5][0]\d{7}', polist[i+3]).group()
                break
            elif (polist[i]=='PO:' or polist[i]=='P0:' or polist[i]=='Po:' \
            or polist[i]=='pO:' or polist[i]=='p0:' or polist[i]=='po:'):
                po = re.match('[4][5][0]\d{7}', polist[i+1]).group()
                break
            elif re.match('[4][5][0]\d{7}', polist[i]) is not None:
                po = re.match('[4][5][0]\d{7}', polist[i])
                break
            else:
                po = 'No Purchase Order # Found'
    except:
        po = 'No Purchase Order # Found'

    os.remove('test2.jpg')
    # print(po)




# The following function takes a jpg image as input, crops that image
# down to a smaller section around the date, pulls the text
# from that image, stores the text in a list, separated by spaces, and then
# searches for the date.

def dtcrop_ocr(img):
    original = Image.open(img)
    dt_cropped_img = original.crop((0, 400, 3000, 800))
    dt_cropped_img.save('test2.jpg')
    # dt_cropped_img.show()

    dttext = pytesseract.image_to_string(Image.open('test2.jpg'))
    dtlist = dttext.split()
    # print(dtlist)

    global dt

    if dtlist == []:
        dt = 'No Date Found'

    try:
        for i in range(len(dtlist)):
            if (dtlist[i]=='receipt' and dtlist[i+1]=='date' \
            and (dtlist[i+2]==':' or dtlist[i+2]=='i' or dtlist[i+2]=='l' \
            or dtlist[i+2]=='I')):
                dt = re.match('[01]\d\/[0123]\d\/[12]\d{3}', dtlist[i+3]).group()
                break
            else:
                dt = 'No Date Found'
    except:
        dt = 'No Date Found'

    os.remove('test2.jpg')
    # print(dt)




# The following function takes a jpg image as input, pulls the text from
# that entire image, stores the text in a list, separated by spaces, and then
# searches for the Receiving Report #, the Purchase Order #, and the date.

def full_ocr(imgfile):
    fulltext = pytesseract.image_to_string(Image.open(imgfile))
    fulllist = fulltext.split()
    # print(fulllist)

    global rr2
    global po2
    global dt2

    # This finds the Receiving Report #
    try:
        for i in range(len(fulllist)):
            if (fulllist[i]=='No.' or fulllist[i]=='NO.' or fulllist[i]=='N0.' \
            or fulllist[i]=='no.' or fulllist[i]=='nO.' or fulllist[i]=='n0.') \
            and (fulllist[i+2] == 'Page' or fulllist[i+2] == 'page'):
                rr2 = re.match('[5][0][0]\d{7}', fulllist[i+1]).group()
                break
            else:
                rr2 = 'No Receiving Report # Found'
    except:
        rr2 = 'No Receiving Report # Found'


    # This finds the Purchasing Order #
    try:
        for i in range(len(fulllist)):
            if (fulllist[i]=='PO' or fulllist[i]=='P0' or fulllist[i]=='Po' \
            or fulllist[i]=='pO' or fulllist[i]=='p0' or fulllist[i]=='po') \
            and (fulllist[i+1]==':' or fulllist[i+1]=='i' or fulllist[i+1]=='l' \
            or fulllist[i+1]=='I'):
                po2 = re.match('[4][5][0]\d{7}', fulllist[i+2]).group()
                break
            elif (fulllist[i]=='PO' or fulllist[i]=='P0' or fulllist[i]=='Po' \
            or fulllist[i]=='pO' or fulllist[i]=='p0' or fulllist[i]=='po') \
            and (fulllist[i+2]==':' or fulllist[i+2]=='i'):
                po2 = re.match('[4][5][0]\d{7}', fulllist[i+3]).group()
                break
            elif (fulllist[i]=='PO:' or fulllist[i]=='P0:' or fulllist[i]=='Po:' \
            or fulllist[i]=='pO:' or fulllist[i]=='p0:' or fulllist[i]=='po:'):
                po2 = re.match('[4][5][0]\d{7}', fulllist[i+1]).group()
                break
            elif re.match('[4][5][0]\d{7}', fulllist[i]) is not None:
                po2 = re.match('[4][5][0]\d{7}', fulllist[i]).group()
                break
            else:
                po2 = 'No Purchase Order # Found'
    except:
        po2 = 'No Purchase Order # Found'


    # This finds the date
    try:
        for i in range(len(fulllist)):
            if (fulllist[i]=='receipt' and fulllist[i+1]=='date' \
            and (fulllist[i+2]==':' or fulllist[i+2]=='i' or fulllist[i+2]=='l' \
            or fulllist[i+2]=='I')):
                dt2 = re.match('[01]\d\/[0123]\d\/[12]\d{3}', fulllist[i+3]).group()
                break
            elif fulllist[i+1]=='date' and (fulllist[i+2]==':' \
            or fulllist[i+2]=='i' or fulllist[i+2]=='l'):
                dt2 = re.match('[01]\d\/[0123]\d\/[12]\d{3}', fulllist[i+3]).group()
                break
            else:
                dt2 = 'No Date Found'
    except:
        dt2 = 'No Date Found'


# List all of the file names in this list.

grfilenames = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg','6.jpg','7.jpg','8.jpg',\
'9.jpg','10.jpg','11.jpg', '12.jpg', '13.jpg', '14.jpg', '15.jpg', '16.jpg',\
'17.jpg']


# This iterates through each filename, calls each function with that specific
# file, compares the values of the cropped image with the full image, and 
# gives results based on that comparison.

i = 1
for file in grfilenames:
    full_ocr(file)
    rrcrop_ocr(file)
    pocrop_ocr(file)
    dtcrop_ocr(file)

    if rr == rr2 and rr == 'No Receiving Report # Found':
        print(str(file) + '. RR: ' + rr + ' for either scan.')
    elif rr == rr2:
        print(str(file) + '. RR: ' + rr)
    else:
        print(str(file) + '. RR: ' + \
        'Receiving Report Numbers Do Not Match. Cropped RR is ' + \
        rr + ', and Full RR is ' + rr2 + '.')


    if po == po2:
        print(str(file) + '. PO: ' + po)
    else:
        print(str(file) + '. PO: ' + \
        'Purchase Order Numbers Do Not Match. Cropped PO is ' + \
        po + ', and Full PO is ' + po2 + '.')


    if dt == dt2:
        print(str(file) + '. DT: ' + dt + '\n')
    else:
        print(str(file) + '. DT: ' + 'Dates Do Not Match. Cropped Date is ' + \
        dt + ', and Full Date is ' + dt2 + '.' + '\n')

    i += 1
