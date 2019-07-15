# sw-ocr21.py

# Merge multiple matching ptfiles into one
# tif file and convert jpg files to tif and
# order the files in one by one acending order.

import os
import re
import sys
from PIL import Image
import pytesseract
from collections import defaultdict
import glob



# The following function takes a jpg image as input, crops that image
# down to a smaller section around the Receiving Report #, pulls the text
# from that image, stores the text in a list, searches for the RR #,
# and stores the RR # in a variable.
def rrcrop_ocr(img):
    original = Image.open(img)

    dpi = original.info['dpi']

    if dpi == (600,600):
        l,u,r,d = 3000,0,5100,500
    elif dpi == (400,400):
        l,u,r,d = 2000,0,3400,333
    elif dpi == (300,300):
        l,u,r,d = 1500,0,2550,250
    else:
        l,u,r,d = 3000,0,5000,500

    rr_cropped_img = original.crop((l,u,r,d))
    rr_cropped_img.save('test1.jpg')
    # rr_cropped_img.show()

    rrtext = pytesseract.image_to_string(Image.open('test1.jpg'))
    rrlist = rrtext.split()
    # print('RR list:')
    # print(rrlist)

    global rr

    if rrlist == []:
        rr = 'No Receiving Report # Found'
    try:
        for i in range(len(rrlist)):
            if (rrlist[i]=='No.' or rrlist[i]=='NO.' or rrlist[i]=='N0.' \
            or rrlist[i]=='no.' or rrlist[i]=='nO.' or rrlist[i]=='n0.') \
            and (rrlist[i+2] == 'Page' or rrlist[i+2] == 'page'):
                rr = str(re.match('[5][0][0]\d{7}', rrlist[i+1]).group())
                break
            elif rrlist[i]=='No.' or rrlist[i]=='NO.' or rrlist[i]=='N0.' \
            or rrlist[i]=='no.' or rrlist[i]=='nO.' or rrlist[i]=='n0.':
                rr = str(re.match('[5][0][0]\d{7}', rrlist[i+1]).group())
                break
            elif re.match('[5][0][0]\d{7}', rrlist[i]) is not None:
                rr = str(re.match('[5][0][0]\d{7}', rrlist[i]).group())
                break
            else:
                rr = 'No Receiving Report # Found'
    except:
        rr = 'No Receiving Report # Found'

    os.remove('test1.jpg')





# The following function takes a jpg image as input, crops that image
# down to a smaller section around the Purchase Order #, pulls the text
# from that image, stores the text in a list, searches for the PO #,
# and stores the PO # in a variable.
def pocrop_ocr(img):
    original = Image.open(img)

    dpi = original.info['dpi']

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

    potext = pytesseract.image_to_string(Image.open('test2.jpg'))
    polist = potext.split()

    global po

    if polist == []:
        po = 'No Purchase Order # Found'

    try:
        for i in range(len(polist)):
            if (polist[i]=='PO' or polist[i]=='P0' or polist[i]=='Po' \
            or polist[i]=='pO' or polist[i]=='p0' or polist[i]=='po') \
            and (polist[i+1]==':' or polist[i+1]=='i' or polist[i+1]=='l' \
            or polist[i+1]=='I'):
                po = str(re.match('[4][5][0]\d{7}', polist[i+2]).group())
                break
            elif (polist[i]=='PO' or polist[i]=='P0' or polist[i]=='Po' \
            or polist[i]=='pO' or polist[i]=='p0' or polist[i]=='po') \
            and (polist[i+2]==':' or polist[i+2]=='i'):
                po = str(re.match('[4][5][0]\d{7}', polist[i+3]).group())
                break
            elif (polist[i]=='PO:' or polist[i]=='P0:' or polist[i]=='Po:' \
            or polist[i]=='pO:' or polist[i]=='p0:' or polist[i]=='po:'):
                po = str(re.match('[4][5][0]\d{7}', polist[i+1]).group())
                break
            elif re.match('[4][5][0]\d{7}', polist[i]) is not None:
                po = str(re.match('[4][5][0]\d{7}', polist[i]).group())
                break
            else:
                po = 'No Purchase Order # Found'
    except:
        po = 'No Purchase Order # Found'

    os.remove('test2.jpg')





# The following function takes a jpg image as input, crops that image
# down to a smaller section around the date, pulls the text
# from that image, stores the text in a list, searches for the date,
# and stores the date in a variable.
def dtcrop_ocr(img):
    original = Image.open(img)

    dpi = original.info['dpi']

    if dpi == (600,600):
        l,u,r,d = 0,400,3000,800
    elif dpi == (400,400):
        l,u,r,d = 0,267,2000,533
    elif dpi == (300,300):
        l,u,r,d = 0,200,1500,400
    else:
        l,u,r,d = 0,400,3000,800

    dt_cropped_img = original.crop((l,u,r,d))
    dt_cropped_img.save('test3.jpg')

    dttext = pytesseract.image_to_string(Image.open('test3.jpg'))
    dtlist = dttext.split()

    global dt

    if dtlist == []:
        dt = 'No Date Found'

    try:
        for i in range(len(dtlist)):
            if (dtlist[i]=='receipt' and dtlist[i+1]=='date' \
            and (dtlist[i+2]==':' or dtlist[i+2]=='i' or dtlist[i+2]=='l' \
            or dtlist[i+2]=='I')):
                dt = str(re.match('[01]\d\/[0123]\d\/[12]\d{3}', dtlist[i+3]).group())
                break
            elif dtlist[i+1]=='date' and (dtlist[i+2]==':' \
            or dtlist[i+2]=='i' or dtlist[i+2]=='l'):
                dt = str(re.match('[01]\d\/[0123]\d\/[12]\d{3}', dtlist[i+3]).group())
                break
            elif re.match('[01]\d\/[0123]\d\/[12]\d{3}', dtlist[i]) is not None:
                dt = str(re.match('[01]\d\/[0123]\d\/[12]\d{3}', dtlist[i]).group())
                break
            else:
                dt = 'No Date Found'
    except:
        dt = 'No Date Found'

    os.remove('test3.jpg')




# The following function takes a jpg image as input, crops that image
# down to a smaller section around the person, pulls the text
# from that image, stores the text in a list, searches for the person,
# and stores the person in a variable.
def pscrop_ocr(img):
    original = Image.open(img)

    dpi = original.info['dpi']

    if dpi == (600,600):
        l,u,r,d = 0,4000,5000,6700
    elif dpi == (400,400):
        l,u,r,d = 0,2667,3333,4467
    elif dpi == (300,300):
        l,u,r,d = 0,2000,2500,3350
    else:
        l,u,r,d = 0,4000,5000,6700

    ps_cropped_img = original.crop((l,u,r,d))
    ps_cropped_img.save('test4.jpg')
    # ps_cropped_img.show()

    pstext = pytesseract.image_to_string(Image.open('test4.jpg'))
    pslist = pstext.split()
    # print('PS list:')
    # print(pslist)

    global ps

    if pslist == []:
        ps = 'No Person Found'

    try:
        for i in range(len(pslist)):
            if pslist[i]=='Received' and pslist[i+1]=='by' \
            and (pslist[i+2]==':' or pslist[i+2]=='i' or pslist[i+2]=='l' \
            or pslist[i+2]=='I' or pslist[i+2]=='-:' or pslist[i+2]=='_:') \
            and (pslist[i+4]=='S' or pslist[i+4]=='s' or pslist[i+4]=='5' \
            or pslist[i+4]=='_'):
                ps = str(re.match('[a-zA-Z]*', pslist[i+3]).group())
                break
            elif pslist[i]=='Received' and pslist[i+1]=='by' \
            and (pslist[i+4]=='S' or pslist[i+4]=='5' or pslist[i+4]=='s'):
                ps = str(re.match('[a-zA-Z]*', pslist[i+3]).group())
                break
            elif pslist[i]=='Received' and pslist[i+1]=='by' \
            and (pslist[i+2]==':' or pslist[i+2]=='i' or pslist[i+2]=='l' \
            or pslist[i+2]=='I' or pslist[i+2]=='-:'):
                ps = str(re.match('[a-zA-Z]*', pslist[i+3]).group())
                break
            elif (pslist[i]=='S' or pslist[i]=='s' or pslist[i]=='5') \
            and (pslist[i+1]=='I' or pslist[i+1]=='i' or pslist[i+1]=='l' \
            or pslist[i+1]=='IG' or pslist[i+1]=='lG'):
                ps = str(re.match('[a-zA-Z]*', pslist[(i-1)]).group())
                break
            else:
                ps = 'No Person Found'
    except:
        ps = 'No Person Found'

    os.remove('test4.jpg')





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
    global ps2
    global isgr2


    # This checks to see if the file is a GR.
    # if fulllist == []:
    #     isgr2 = False
    # try:
    #     for i in range(len(fulllist)):
    #         if (fulllist[i]=='No.' or fulllist[i]=='NO.' or fulllist[i]=='N0.' \
    #         or fulllist[i]=='no.' or fulllist[i]=='nO.' or fulllist[i]=='n0.') \
    #         and (fulllist[i+2] == 'Page' or fulllist[i+2] == 'page') \
    #         and re.match('[5][0][0]\d{7}', fulllist[i+1]) is not None:
    #             isgr2 = True
    #             break
    #         elif (fulllist[i]=='No.' or fulllist[i]=='NO.' or fulllist[i]=='N0.' \
    #         or fulllist[i]=='no.' or fulllist[i]=='nO.' or fulllist[i]=='n0.') \
    #         and re.match('[5][0][0]\d{7}', fulllist[i+1]) is not None:
    #             isgr2 = True
    #             break
    #         elif re.match('[5][0][0]\d{7}', fulllist[i]) is not None \
    #         and fulllist[i+1]=='Page' or fulllist[i+1]=='page':
    #             isgr2 = True
    #             break
    #         else:
    #             isgr2 = False
    # except:
    #     isgr2 = False


    # This finds the Receiving Report #
    try:
        for i in range(len(fulllist)):
            if (fulllist[i]=='No.' or fulllist[i]=='NO.' or fulllist[i]=='N0.' \
            or fulllist[i]=='no.' or fulllist[i]=='nO.' or fulllist[i]=='n0.') \
            and (fulllist[i+2] == 'Page' or fulllist[i+2] == 'page'):
                rr2 = str(re.match('[5][0][0]\d{7}', fulllist[i+1]).group())
                break
            elif fulllist[i]=='No.' or fulllist[i]=='NO.' or fulllist[i]=='N0.' \
            or fulllist[i]=='no.' or fulllist[i]=='nO.' or fulllist[i]=='n0.':
                rr2 = str(re.match('[5][0][0]\d{7}', fulllist[i+1]).group())
                break
            elif re.match('[5][0][0]\d{7}', fulllist[i]) is not None:
                rr2 = str(re.match('[5][0][0]\d{7}', fulllist[i]).group())
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
                po2 = str(re.match('[4][5][0]\d{7}', fulllist[i+2]).group())
                break
            elif (fulllist[i]=='PO' or fulllist[i]=='P0' or fulllist[i]=='Po' \
            or fulllist[i]=='pO' or fulllist[i]=='p0' or fulllist[i]=='po') \
            and (fulllist[i+2]==':' or fulllist[i+2]=='i'):
                po2 = str(re.match('[4][5][0]\d{7}', fulllist[i+3]).group())
                break
            elif (fulllist[i]=='PO:' or fulllist[i]=='P0:' or fulllist[i]=='Po:' \
            or fulllist[i]=='pO:' or fulllist[i]=='p0:' or fulllist[i]=='po:'):
                po2 = str(re.match('[4][5][0]\d{7}', fulllist[i+1]).group())
                break
            elif re.match('[4][5][0]\d{7}', fulllist[i]) is not None:
                po2 = str(re.match('[4][5][0]\d{7}', fulllist[i]).group())
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
                dt2 = str(re.match('[01]\d\/[0123]\d\/[12]\d{3}', fulllist[i+3]).group())
                break
            elif fulllist[i+1]=='date' and (fulllist[i+2]==':' \
            or fulllist[i+2]=='i' or fulllist[i+2]=='l'):
                dt2 = str(re.match('[01]\d\/[0123]\d\/[12]\d{3}', fulllist[i+3]).group())
                break
            elif re.match('[01]\d\/[0123]\d\/[12]\d{3}', fulllist[i]) is not None:
                dt2 = str(re.match('[01]\d\/[0123]\d\/[12]\d{3}', fulllist[i]).group())
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
                ps2 = str(re.match('[a-zA-Z]*', fulllist[i+3]).group())
                break
            elif fulllist[i]=='Received' and fulllist[i+1]=='by' \
            and (fulllist[i+4]=='S' or fulllist[i+4]=='5' or fulllist[i+4]=='s'):
                ps2 = str(re.match('[a-zA-Z]*', fulllist[i+3]).group())
                break
            elif fulllist[i]=='Received' and fulllist[i+1]=='by' \
            and (fulllist[i+2]==':' or fulllist[i+2]=='i' or fulllist[i+2]=='l' \
            or fulllist[i+2]=='I' or fulllist[i+2]=='-:'):
                ps2 = str(re.match('[a-zA-Z]*', fulllist[i+3]).group())
                break
            elif (fulllist[i]=='S' or fulllist[i]=='s' or fulllist[i]=='5') \
            and (fulllist[i+1]=='I' or fulllist[i+1]=='i' or fulllist[i+1]=='l') \
            and (fulllist[i+2]=='G' or fulllist[i+2]=='6'):
                ps2 = str(re.match('[a-zA-Z]*', fulllist[i-1]).group())
                break
            else:
                ps2 = 'No Person Found'
    except:
        ps2 = 'No Person Found'





# The following function takes a jpg image as input, crops that image
# down to a smaller section around the GR identifier, pulls the text
# from that image, stores the text in a list, searches for the GR identifier,
# and stores whether it is a GR or not as a boolean variable.
def gr_cropocr(img):
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
    cropped_img.save('test5.jpg')
    # cropped_img.show()

    croptext = pytesseract.image_to_string(Image.open('test5.jpg'))
    rrlist = croptext.split()

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

    os.remove('test5.jpg')




# EXECUTION TIME
# The following three chunks of code execute the functions
# and make this train go round and round.


# Initializations
filenames = glob.glob('*.jpg')
allfilenames = []
grfilenames = []
ptfilenames = []
counter1 = 1
counter2 = 1
counter3 = 1
counter4 = 1

# The following creates a .txt file and writes the first line to it.
with open('results.txt', 'w') as txtfile:
    txtfile.write('Receiving Report #, Purchase Order #, Name, Date@Image File' + '\n')


# The following iterates through each filename and gets isgr
# from the function  gr_cropocr. If it is a goods receipt (if isgr = True),
# it is renamed accordingly (whole number.jpg) and then added to the list
# allfilenames. If it is not a goods receipt, it is renamed accordingly
# (GRwholenumber.decimalnumber.jpg) and then added to the list
# allfilenames.
for file in filenames:
    gr_cropocr(file)
    if isgr == True: #or isgr2 == True:
        os.rename(file, str(counter1) + '.jpg')
        allfilenames.append(str(counter1) + '.jpg')
        counter1 += 1
        counter2 = 1
    else:
        os.rename(file, str((counter1 - 1)) + '.' + str(counter2) \
        +  '.jpg')
        allfilenames.append(str((counter1 - 1)) + '.' + str(counter2) \
        + '.jpg')
        counter2 += 1

# The following loops iterate through the list allfilenames and removes
# duplicate GRs.
k = 1
while k < len(allfilenames):
    if len(allfilenames[k].split('.')) == 2 and \
    len(allfilenames[k-1].split('.')) == 2:
        os.remove(allfilenames[k-1])                    
        del allfilenames[k-1]
        k -= 1
    k += 1

# The following loop iterates through the files in allfilenames and
# appends the good receipt files to grfilenames and the picking ticket
# files to ptfilenames.
for file in allfilenames:
    if len(file.split('.')) == 2:
        grfilenames.append(file)
    elif len(file.split('.')) == 3:
        ptfilenames.append(file)

# The following creates a dictionary called dicta that holds the goods
# receipts as keys and picking tickets as values.
dicta = defaultdict(list)
for grfile in grfilenames:
    for ptfile in ptfilenames:
        if grfile.split('.')[0] == ptfile.split('.')[0]:
            dicta[grfile].append(ptfile)


# The following renames the GR's into numerical order
# after the duplicates have been removed.
# counter = 1
# for file in dicta:
#     counter2 = 1
#     if file == (str(counter) + '.jpg'):
#         counter += 1
#     else:
#         os.rename(file, str(counter) + '.jpg')
#         dicta[str(counter) + '.jpg'] = dicta.pop(file)
#         # for i in dicta[str(counter) + '.jpg']:
#         #     i = str(counter) + '.' + str(counter2) + '.jpg'
#         #     counter2 += 1
#         counter += 1


# The following iterates only through the GR files in dicta
# and uses the 4 functions to pull the RR, PO, DT, and PS from each.
# Then, it compares the values of rr & rr2, po & po2, dt & dt2, and
# ps & ps2. Based on this comparison, final values are assigned to
# the variables recrep, purord, date, and person, respectively.
# All of these final values are then added to the txt file for each
# file in dicta.
for file in dicta:
    full_ocr(file)
    rrcrop_ocr(file)
    pocrop_ocr(file)
    dtcrop_ocr(file)
    pscrop_ocr(file)


    # The following compares the receiving report found from
    # a cropped OCR scan and the receiving report found from
    # a full page OCR scan and sets the variable recrep equal
    # to their match or a regex match of one of them.
    if rr == rr2 and rr == 'No Receiving Report # Found':
        recrep = 'Check'
    elif rr == rr2:
        recrep = rr
    elif rr != rr2 and re.match('[5][0][0]\d{7}', rr) is not None and \
    re.match('[5][0][0]\d{7}', rr2) is not None:
        recrep = str(rr) + ', ' + str(rr2) + ': Check'
    elif rr != rr2 and re.match('[5][0][0]\d{7}', rr) is not None and \
    re.match('[5][0][0]\d{7}', rr2) is None:
        recrep = str(rr)# + ': Check'
    elif rr != rr2 and re.match('[5][0][0]\d{7}', rr) is None and \
    re.match('[5][0][0]\d{7}', rr2) is not None:
        recrep = str(rr2)# + ': Check'
    elif rr != rr2 and re.match('[5][0][0]\d{7}', rr) is not None:
        recrep = str(rr)# + ': Check'
    elif rr != rr2 and re.match('[5][0][0]\d{7}', rr2) is not None:
        recrep = str(rr2)# + ': Check'
    else:
        recrep = str(rr) + ', ' + str(rr2) + ': Check'

    # The following compares the purchase order found from
    # a cropped OCR scan and the purchase order found from
    # a full page OCR scan and sets the variable purord equal
    # to their match or a regex match of one of them.
    if po == po2 and po == 'No Purchase Order # Found':
        purord = 'Check'
    elif po == po2:
        purord = po
    elif po != po2 and re.match('[4][5][0]\d{7}', po) is not None and \
    re.match('[4][5][0]\d{7}', po2) is not None:
        purord = str(po) + ', ' + str(po2) + ': Check'
    elif po != po2 and re.match('[4][5][0]\d{7}', po) is not None and \
    re.match('[4][5][0]\d{7}', po2) is None:
        purord = str(po) + ': Check'
    elif po != po2 and re.match('[4][5][0]\d{7}', po) is None and \
    re.match('[4][5][0]\d{7}', po2) is not None:
        purord = str(po2) + ': Check'
    elif po != po2 and re.match('[4][5][0]\d{7}', po) is not None:
        purord = str(po) + ': Check'
    elif po != po2 and re.match('[4][5][0]\d{7}', po2) is not None:
        purord = str(po2) + ': Check'
    else:
        purord = str(po) + ', ' + str(po2) + ': Check'

    # The following compares the date found from
    # a cropped OCR scan and the date found from
    # a full page OCR scan and sets the variable date equal
    # to their match or a regex match of one of them.
    if dt == dt2 and dt == 'No Date Found':
        date = 'Check'
    elif dt == dt2:
        date = dt
    elif dt != dt2 and re.match('[01]\d\/[0123]\d\/[12]\d{3}', dt) is not None and \
    re.match('[01]\d\/[0123]\d\/[12]\d{3}', dt2) is not None:
        date = str(dt) + ', ' + str(dt2) + ': Check'
    elif dt != dt2 and re.match('[01]\d\/[0123]\d\/[12]\d{3}', dt) is not None and \
    re.match('[01]\d\/[0123]\d\/[12]\d{3}', dt2) is None:
        date = str(dt) + ': Check'
    elif dt != dt2 and re.match('[01]\d\/[0123]\d\/[12]\d{3}', dt) is None and \
    re.match('[01]\d\/[0123]\d\/[12]\d{3}', dt2) is not None:
        date = str(dt2) + ': Check'
    elif dt != dt2 and re.match('[01]\d\/[0123]\d\/[12]\d{3}', dt) is not None:
        date = str(dt) + ': Check'
    elif dt != dt2 and re.match('[01]\d\/[0123]\d\/[12]\d{3}', dt2) is not None:
        date = str(dt2) + ': Check'
    else:
        date = str(dt) + ', ' + str(dt2) + ': Check'

    # The following compares the name found from
    # a cropped OCR scan and the name found from
    # a full page OCR scan and sets the variable person equal
    # to their match or a regex match of one of them.
    if ps == ps2 and ps == 'No Person Found':
        person = 'No Person Found'
    elif ps == ps2:
        person = ps
    elif ps != ps2 and re.match('^[a-zA-Z0-9]*$', ps) is not None and \
    re.match('[5][0][0]\d{7}', ps2) is not None:
        person = str(ps) + ', ' + str(ps2) + ': Check'
    elif ps != ps2 and re.match('^[a-zA-Z0-9]*$', ps) is not None and \
    re.match('[a-zA-Z]*', ps2) is None:
        person = str(ps)# + ': Check'
    elif ps != ps2 and re.match('^[a-zA-Z0-9]*$', ps2) is not None and \
    re.match('[a-zA-Z]*', ps) is None:
        person = str(ps2)# + ': Check'
    elif ps != ps2 and re.match('^[a-zA-Z0-9]*$', ps) is not None:
        person = str(ps)# + ': Check'
    elif ps != ps2 and re.match('^[a-zA-Z0-9]*$', ps2) is not None:
        person = str(ps2)# + ': Check'
    else:
        person = str(ps) + ', ' + str(ps2) + ': Check'

    # The following is a command line call that converts several
    # input image files into one multi-page .tif file.
    multitif = 'C:\\"Program Files"\\IrfanView\\i_view64.exe /multitif=(C:\\Users\\culwellt\\Documents\\southwireOCR\\tester\\' + file.split('.')[0] + '.tif,'

    # The following determines whether to use the multitif command
    # line function or the convert command line function on the
    # picking tickets. This is determined by the number of picking
    # tickets with each goods receipt. If there is more than one,
    # multitif is used. If there is only one, convert is used.
    if len(dicta[file]) > 1:
        for ptfile in dicta[file]:
            multitif = multitif + 'C:\\Users\\culwellt\\Documents\\southwireOCR\\tester\\' + ptfile + ','
        multitif = multitif[:-1]
        multitif = multitif + '/killmesoftly'
        os.system(multitif)
    else:
        for ptfile in dicta[file]:
            convert = 'C:\\"Program Files"\\IrfanView\\i_view64.exe C:\\Users\\culwellt\\Documents\\southwireOCR\\tester\\' + ptfile + ' /convert=C:\\Users\\culwellt\\Documents\\southwireOCR\\tester\\' + file.split('.')[0] + '.tif'
        os.system(convert)

    # The following deletes the old ptfiles from dicta.
    for ptfile in dicta[file]:
        os.remove(ptfile)

    # The following creates a variable that describes the new
    # .tif file that has been created from the process above.
    newfilename = file.split('.')[0] + '.tif'

    # The following creates a variable that stores a single line
    # of text that will be appended to the .txt file.
    txtrow = recrep + ', ' + purord + ', ' + person + ', ' + date + \
    '@' + newfilename + '\n'
    
    # The following opens the .txt file and appends the line
    # of text that is stored in the variable "txtrow".
    with open('results.txt', 'a') as txtfile:
        txtfile.write(txtrow)