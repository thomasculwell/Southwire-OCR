# sw-ocr16.5.py

# Trying something off the wall here.

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
    rr_cropped_img.save('test.jpg')

    rrtext = pytesseract.image_to_string(Image.open('test.jpg'))
    rrlist = rrtext.split()

    global rr
    global isgr

    # This checks to see if file is a GR.
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

    os.remove('test.jpg')





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
    dt_cropped_img.save('test2.jpg')

    dttext = pytesseract.image_to_string(Image.open('test2.jpg'))
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

    os.remove('test2.jpg')




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
    ps_cropped_img.save('test2.jpg')

    pstext = pytesseract.image_to_string(Image.open('test2.jpg'))
    pslist = pstext.split()

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

    os.remove('test2.jpg')





# The following function takes a jpg image as input, pulls the text from
# that entire image, stores the text in a list, separated by spaces, and then
# searches for the Receiving Report #, the Purchase Order #, and the date.
def full_ocr(imgfile):
    fulltext = pytesseract.image_to_string(Image.open(imgfile))
    fulllist = fulltext.split()

    global rr2
    global po2
    global dt2
    global ps2
    global isgr2


    # This checks to see if the file is a GR.
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
            elif re.match('[5][0][0]\d{7}', fulllist[i]) is not None \
            and fulllist[i+1]=='Page' or fulllist[i+1]=='page':
                isgr2 = True
                break
            else:
                isgr2 = False
    except:
        isgr2 = False


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
                rr2 = str(re.match('[5][0][0]\d{7}', fulllist[i]))
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



grfilenames = []
ptfilenames = []
allfilenames = []

# Filenames is a variable that stores all of the jpg files in the current
# directory by searching for them using glob.
filenames = glob.glob('*.jpg')

# Initializes the results.csv file with title columns as follows:
# RR#, PO#, Name, Date
with open('results.csv', 'w') as csvfile:
    csvfile.write(' , Receiving Report #, Purchase Order #, Name, Date' + '\n')

# Initializes the row number for the csv file.
rownumber = 1

counter = 1
counter2 = 1



# The following iterates through each filename, calls each function with 
# that specific file, compares the values of the cropped image with the
# full image, and stores the results in variables.
for file in filenames:
    full_ocr(file)
    rrcrop_ocr(file)
    pocrop_ocr(file)
    dtcrop_ocr(file)
    pscrop_ocr(file)

    # The following if, else statements change the names of the files
    # based on if they are a GR file or a PT file.
    if isgr == True or isgr2 == True:
            os.rename(file, str(counter) + '.jpg')
            allfilenames.append(str(counter) + '.jpg')
            counter += 1
            counter2 = 1
    else:
        os.rename(file, str((counter - 1)) + '.' + str(counter2) \
        +  '.jpg')
        allfilenames.append(str((counter - 1)) + '.' + str(counter2) \
        + '.jpg')
        counter2 += 1


    # The following separates the filenames list into two lists:
    # GR files (grfilenames) and PT files (ptfilenames)
    if len(file.split('.')) == 2:
        grfilenames.append(file)
    elif len(file.split('.')) == 3:
        ptfilenames.append(file)


    # The following is a for loop that matches gr file names with pt
    # file names based on their first character. This makes a dictionary
    # with corresponding pages.
    dicta = defaultdict(list)
    for grfile in grfilenames:
        for ptfile in ptfilenames:
            if grfile.split('.')[0] == ptfile.split('.')[0]:
                dicta[grfile].append(ptfile)


    k = 0
    while k < len(allfilenames):
        if k >= 1:
            if len(allfilenames[k].split('.')) == 2:
                if len(allfilenames[k-1].split('.')) == 2:
                    os.remove(allfilenames[k-1])                    
                    del allfilenames[k-1]
                    k -= 1
            elif len(allfilenames[k].split('.')) == 3:
                k += 0
        k += 1

    for i in dicta[file]:
        image = Image.open(i)
        # image.show()

    if isgr == True or isgr2 == True:
        if rr == rr2 and rr == 'No Receiving Report # Found':
            recrep = 'Check'
        elif rr == rr2:
            recrep = rr
        elif rr != rr2 and re.match('[5][0][0]\d{7}', rr) is not None and \
        re.match('[5][0][0]\d{7}', rr2) is not None:
            recrep = str(rr) + ', ' + str(rr2) + ': Check'
        elif rr != rr2 and re.match('[5][0][0]\d{7}', rr) is not None and \
        re.match('[5][0][0]\d{7}', rr2) is None:
            recrep = str(rr) + ': Check'
        elif rr != rr2 and re.match('[5][0][0]\d{7}', rr) is None and \
        re.match('[5][0][0]\d{7}', rr2) is not None:
            recrep = str(rr2) + ': Check'
        elif rr != rr2 and re.match('[5][0][0]\d{7}', rr) is not None:
            recrep = str(rr) + ': Check'
        elif rr != rr2 and re.match('[5][0][0]\d{7}', rr2) is not None:
            recrep = str(rr2) + ': Check'
        else:
            recrep = str(rr) + ', ' + str(rr2) + ': Check'


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


        if ps == ps2 and ps == 'No Person Found':
            person = 'Check'
        elif ps == ps2:
            person = ps
        elif ps != ps2 and re.match('[a-zA-Z]*', ps) is not None and \
        re.match('[5][0][0]\d{7}', ps2) is not None:
            person = str(ps) + ', ' + str(ps2) + ': Check'
        elif ps != ps2 and re.match('[a-zA-Z]*', ps) is not None and \
        re.match('[a-zA-Z]*', ps2) is None:
            person = str(ps) + ': Check'
        elif ps != ps2 and re.match('[a-zA-Z]*', ps) is None and \
        re.match('[a-zA-Z]*', ps2) is not None:
            person = str(ps2) + ': Check'
        elif ps != ps2 and re.match('[a-zA-Z]*', ps) is not None:
            person = str(ps) + ': Check'
        elif ps != ps2 and re.match('[a-zA-Z]*', ps2) is not None:
            person = str(ps2) + ': Check'
        else:
            person = str(ps) + ', ' + str(ps2) + ': Check'


        csvrow = str(rownumber) + ', ' + recrep + ', ' + purord + ', ' \
        + person + ', ' + date + '@' + str(file) + '\n'

        with open('results.csv', 'a') as csvfile:
            csvfile.write(csvrow)


        rownumber += 1