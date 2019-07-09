# Southwire-OCR for Axweb Uploads

# Make the Tiff files more clear.

# Need to add the tesseract conversion in this python script instead of 
# doing it purely through the command line. Basically, I want to make this 
# one fluid motion of tif --> essential information.

# Max said something about how I could do something in notepad?

# Use RegEx to solve issue of not getting all information with OCR.
# If this doesn't work, I'll probably have to use something with
# a image cropping technology and specify particular points of each
# sheet to crop. With this, though, if the scanner doesn't scan each
# paper exactly straight, it could grab information that isn't correct.

# Get database variable to automatically take files from file explorer and
# make a list of file.
import os
import tempfile
import subprocess
import re

def ocr(imgfile):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', imgfile, temp.name], \
	stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r', encoding = 'utf-8') as handle:
        contents = handle.read().split()

    os.remove(temp.name + '.txt')
    return contents

def essentialtext(listoftext):
	counter1 = 1
	counter2 = 1
	counter3 = 1
	
	for i in range(len(listoftext)):
		if listoftext[i] == 'No.' or listoftext[i] == 'NO.':
			try:
				print(str(counter1) + '. GR:   ' + \
				re.match('[5][0][0]\d{7}', listoftext[i+1]).group())
			except:
				try:
					print(str(counter1) + '. GR:   ' + \
					re.match('No.[5][0][0]\d{7}', listoftext[i]).group())
				except:
					try:
						print(str(counter1) + '. GR:   ' + \
						re.match('NO.[5][0][0]\d{7}', listoftext[i]).group())
					except:
						print('No GR Found')
			counter1 += 1

		if listoftext[i] == 'receipt' \
		and listoftext[i+1] == 'date' and listoftext[i+2] == ':':
			print(str(counter2) + '. Date: ' + \
			re.match('[01][0-9]\/[0123][0-9]\/[12][0-9]{[0-9][0-9]}', \
			listoftext[i+3]).group())
			counter2 += 1

		if listoftext[i] == 'PO' and listoftext[i+1] == ':':
			print(str(counter3) + '. PO:   ' + \
			re.match('[4][5][0]\d{7}', listoftext[i+2]).group())
			counter3 += 1

		

txt = ocr('600x600.tif')
essentialtext(txt)