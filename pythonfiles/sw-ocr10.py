# sw-ocr10.py
# Compares grfilenames to ptfilenames for matching purposes

import os
import re
import sys
from PIL import Image
import pytesseract
from collections import defaultdict





# The following function takes a jpg image as input, crops that image
# down to a smaller section around the Receiving Report #, pulls the text
# from that image, stores the text in a list, searches for the RR #,
# and stores the RR # in a variable.

def rrcrop_ocr(img):
    original = Image.open(img)

    dpi = original.info['dpi']
    # print(dpi)
    if dpi == (600,600):
        l,u,r,d = 3000,0,5100,500
    elif dpi == (400,400):
        l,u,r,d = 2000,0,3400,333
    elif dpi == (300,300):
        l,u,r,d = 1500,0,2550,250
    else:
        l,u,r,d = 3000,0,5000,500

    rr_cropped_img = original.crop((l,u,r,d))
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
            elif rrlist[i]=='No.' or rrlist[i]=='NO.' or rrlist[i]=='N0.' \
            or rrlist[i]=='no.' or rrlist[i]=='nO.' or rrlist[i]=='n0.':
                rr = re.match('[5][0][0]\d{7}', rrlist[i+1]).group()
                break
            elif re.match('[5][0][0]\d{7}', rrlist[i]) is not None:
                rr = re.match('[5][0][0]\d{7}', rrlist[i])
                break
            else:
                rr = 'No Receiving Report # Found'
    except:
        rr = 'No Receiving Report # Found'

    os.remove('test.jpg')
    # print(rr)










# The following function takes a jpg image as input, crops that image
# down to a smaller section around the Purchase Order #, pulls the text
# from that image, stores the text in a list, searches for the PO #,
# and stores the PO # in a variable.

def pocrop_ocr(img):
    original = Image.open(img)

    dpi = original.info['dpi']
    # print(dpi)
    if dpi == (600,600):
        l,u,r,d = 0,800,3000,1400
    elif dpi == (400,400):
        l,u,r,d = 0,533,2000,933
    elif dpi == (300,300):
        l,u,r,d = 0,400,1500,700
    else:
        l,u,r,d = 0,800,3000,1400

    po_cropped_img = original.crop((l,u,r,d))
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
# from that image, stores the text in a list, searches for the date,
# and stores the date in a variable.

def dtcrop_ocr(img):
    original = Image.open(img)

    dpi = original.info['dpi']
    # print(dpi)
    if dpi == (600,600):
        l,u,r,d = 0,400,3000,800
    elif dpi == (400,400):
        l,u,r,d = 0,267,2000,533
    elif dpi == (300,300):
        l,u,r,d = 0,200,1500,400
    else:
        l,u,r,d = 0,400,3000,800

    dt_cropped_img = original.crop((l,u,r,d))
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
            elif dtlist[i+1]=='date' and (dtlist[i+2]==':' \
            or dtlist[i+2]=='i' or dtlist[i+2]=='l'):
                dt = re.match('[01]\d\/[0123]\d\/[12]\d{3}', dtlist[i+3]).group()
                break
            elif re.match('[01]\d\/[0123]\d\/[12]\d{3}', dtlist[i]) is not None:
                dt = re.match('[01]\d\/[0123]\d\/[12]\d{3}', dtlist[i])
                break
            else:
                dt = 'No Date Found'
    except:
        dt = 'No Date Found'

    os.remove('test2.jpg')
    # print(dt)









# The following function takes a jpg image as input, crops that image
# down to a smaller section around the person, pulls the text
# from that image, stores the text in a list, searches for the person,
# and stores the person in a variable.

def pscrop_ocr(img):
    original = Image.open(img)

    dpi = original.info['dpi']
    # print(dpi)
    if dpi == (600,600):
        l,u,r,d = 0,4000,5000,6700
    elif dpi == (400,400):
        l,u,r,d = 0,2667,3333,4467
    elif dpi == (300,300):
        l,u,r,d = 0,2000,2500,3350
    else:
        l,u,r,d = 0,4000,5000,6700

    ps_cropped_img = original.crop((l,u,r,d))
    ps_cropped_img.save('test2.jpg')
    # ps_cropped_img.show()

    pstext = pytesseract.image_to_string(Image.open('test2.jpg'))
    pslist = pstext.split()
    # print(pslist)

    global ps

    if pslist == []:
        ps = 'No Person Found'

    try:
        for i in range(len(pslist)):
            if pslist[i]=='Received' and pslist[i+1]=='by' \
            and (pslist[i+2]==':' or pslist[i+2]=='i' or pslist[i+2]=='l' \
            or pslist[i+2]=='I' or pslist[i+2]=='-:') \
            and (pslist[i+4]=='S' or pslist[i+4]=='s' or pslist[i+4]=='5'):
                ps = re.match('[a-zA-Z]*', pslist[i+3]).group()
                break
            elif pslist[i]=='Received' and pslist[i+1]=='by' \
            and (pslist[i+4]=='S' or pslist[i+4]=='5' or pslist[i+4]=='s'):
                ps = re.match('[a-zA-Z]*', pslist[i+3]).group()
                break
            elif pslist[i]=='Received' and pslist[i+1]=='by' \
            and (pslist[i+2]==':' or pslist[i+2]=='i' or pslist[i+2]=='l' \
            or pslist[i+2]=='I' or pslist[i+2]=='-:'):
                ps = re.match('[a-zA-Z]*', pslist[i+3]).group()
                break
            elif (pslist[i]=='S' or pslist[i]=='s' or pslist[i]=='5') \
            and (pslist[i+1]=='I' or pslist[i+1]=='i' or pslist[i+1]=='l' \
            or pslist[i+1]=='IG' or pslist[i+1]=='lG'):
                ps = re.match('[a-zA-Z]*', pslist[(i-1)]).group()
                break
            else:
                ps = 'No Person Found'
    except:
        ps = 'No Person Found'

    os.remove('test2.jpg')






# The following function takes a jpg image as input, pulls the text from
# that entire image, stores the text in a list, separated by spaces, and then
# searches for the Receiving Report #, the Purchase Order #, and the date.

def full_ocr(imgfile):
    fulltext = pytesseract.image_to_string(Image.open(imgfile))
    fulllist = fulltext.split()
    # fulllist = ['Received', 'by', ' ', ' ', ' ', 'COLED']
    # print(fulllist)

    global rr2
    global po2
    global dt2
    global ps2





    # This finds the Receiving Report #
    try:
        for i in range(len(fulllist)):
            if (fulllist[i]=='No.' or fulllist[i]=='NO.' or fulllist[i]=='N0.' \
            or fulllist[i]=='no.' or fulllist[i]=='nO.' or fulllist[i]=='n0.') \
            and (fulllist[i+2] == 'Page' or fulllist[i+2] == 'page'):
                rr2 = re.match('[5][0][0]\d{7}', fulllist[i+1]).group()
                break
            elif fulllist[i]=='No.' or fulllist[i]=='NO.' or fulllist[i]=='N0.' \
            or fulllist[i]=='no.' or fulllist[i]=='nO.' or fulllist[i]=='n0.':
                rr2 = re.match('[5][0][0]\d{7}', fulllist[i+1]).group()
                break
            elif re.match('[5][0][0]\d{7}', fulllist[i]) is not None:
                rr2 = re.match('[5][0][0]\d{7}', fulllist[i])
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
            elif re.match('[01]\d\/[0123]\d\/[12]\d{3}', fulllist[i]) is not None:
                dt2 = re.match('[01]\d\/[0123]\d\/[12]\d{3}', fulllist[i])
                break
            else:
                dt2 = 'No Date Found'
    except:
        dt2 = 'No Date Found'





    # This finds the person
    try:
        for i in range(len(fulllist)):
            if fulllist[i]=='Received' and fulllist[i+1]=='by' \
            and (fulllist[i+2]==':' or fulllist[i+2]=='i' or fulllist[i+2]=='l' \
            or fulllist[i+2]=='I' or fulllist[i+2]=='-:') \
            and (fulllist[i+4]=='S' or fulllist[i+4]=='s' or fulllist[i+4]=='5'):
                ps2 = re.match('[a-zA-Z]*', fulllist[i+3]).group()
                break
            elif fulllist[i]=='Received' and fulllist[i+1]=='by' \
            and (fulllist[i+4]=='S' or fulllist[i+4]=='5' or fulllist[i+4]=='s'):
                ps2 = re.match('[a-zA-Z]*', fulllist[i+3]).group()
                break
            elif fulllist[i]=='Received' and fulllist[i+1]=='by' \
            and (fulllist[i+2]==':' or fulllist[i+2]=='i' or fulllist[i+2]=='l' \
            or fulllist[i+2]=='I' or fulllist[i+2]=='-:'):
                ps2 = re.match('[a-zA-Z]*', fulllist[i+3]).group()
                break
            elif (fulllist[i]=='S' or fulllist[i]=='s' or fulllist[i]=='5') \
            and (fulllist[i+1]=='I' or fulllist[i+1]=='i' or fulllist[i+1]=='l' \
            or fulllist[i+1]=='IG' or fulllist[i+1]=='lG'):
                ps2 = re.match('[a-zA-Z]*', fulllist[(i-1)]).group()
                break
            else:
                ps2 = 'No Person Found'
    except:
        ps2 = 'No Person Found'










# Below are two lists. One is all of the goods receipt file names and the 
# other is all of the picking ticket file names. Below that is a for loop
# that matches gr file names with pt file names based on their first character.
# Below that iterates through each gr file name, calls each function with 
# that specific file, compares the values of the cropped image with the
# full image, and gives results based on that comparison.

grfilenames = ['1.jpg','2.jpg','3.jpg']

# grfilenames = ['1.jpg', '2.jpg', '3.jpg','4.jpg','5.jpg', '6.jpg', \
# '7.jpg','8.jpg','9.jpg', '10.jpg', '11.jpg','12.jpg','13.jpg', \
# '14.jpg','15.jpg','16.jpg','17.jpg','300-1.jpg','300-2.jpg', \
# '300-3.jpg','300-4.jpg','300-5.jpg','400-1.jpg','400-2.jpg', \
# '400-3.jpg','400-4.jpg','400-5.jpg']

ptfilenames = ['1.1.jpg', '2.1.jpg', '3.1.jpg', '4.1.jpg', '5.1.jpg',\
'6.1.jpg','6.2.jpg']

dicta = defaultdict(list)
for grfile in grfilenames:
    for ptfile in ptfilenames:
        if grfile[0] == ptfile[0]:
            dicta[grfile].append(ptfile)



for file in grfilenames:
    full_ocr(file)
    rrcrop_ocr(file)
    pocrop_ocr(file)
    dtcrop_ocr(file)
    pscrop_ocr(file)

    for i in dicta[file]:
        image = Image.open(i)
        image.show()

    if rr == rr2 and rr == 'No Receiving Report # Found':
        print(str(file) + '. RR: ' + rr + ' for either scan.')
    elif rr == rr2:
        print(str(file) + '. RR: ' + rr)
    else:
        print(str(file) + '. RR: ' + \
        'Receiving Report Numbers Do Not Match. Cropped RR is ' + \
        rr + ', and Full RR is ' + rr2 + '.')


    if po == po2 and po == 'No Purchase Order # Found':
        print(str(file) + '. PO: ' + po + 'for either scan.')
    elif po == po2:
        print(str(file) + '. PO: ' + po)
    else:
        print(str(file) + '. PO: ' + \
        'Purchase Order Numbers Do Not Match. Cropped PO is ' + \
        po + ', and Full PO is ' + po2 + '.')


    if dt == dt2 and dt == 'No Date Found':
        print(str(file) + '. DT: ' + dt + 'for either scan.')
    elif dt == dt2:
        print(str(file) + '. DT: ' + dt)
    else:
        print(str(file) + '. DT: ' + 'Dates Do Not Match. Cropped Date is ' + \
        dt + ', and Full Date is ' + dt2 + '.')


    if ps == ps2 and ps == 'No Person Found':
        print(str(file) + '. PS: ' + ps + 'for either scan.' + '\n')
    elif ps == ps2:
        print(str(file) + '. PS: ' + ps + '\n')
    else:
        print(str(file) + '. PS: ' + ps + '      People Do Not Match. Cropped Person is ' + \
        ps + ', and Full Person is ' + ps2 + '.' + '\n')