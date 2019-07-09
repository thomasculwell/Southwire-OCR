# sw-ocr(test)

import os
import tempfile
import subprocess
import re

def ocr(database):
	global big
	big = []
	for i in database:

	    temp = tempfile.NamedTemporaryFile(delete=False)

	    process = subprocess.Popen(['tesseract', i, temp.name], \
		stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	    process.communicate()

	    with open(temp.name + '.txt', 'r', encoding = 'utf-8') as handle:
	        contents = handle.read().split()

	    os.remove(temp.name + '.txt')
	    big.append(contents)


txt = ocr(['scan3.jpg', 'scan4.jpg', 'scan5.jpg'])

def essentialtext(listoftext):
	counter1 = 1
	counter2 = 1
	counter3 = 1
	
	for j in listoftext:
		for i in range(len(j)):
			if j[i] == 'No.' or j[i] == 'NO.':
				try:
					print(str(counter1) + '. GR:   ' + \
					re.search('[5][0][0]\d{7}', j[i+1]).group())
				except:
					try:
						print(str(counter1) + '. GR:   ' + \
						re.search('No.[5][0][0]\d{7}', j[i]).group())
					except:
						print(str(counter1) + '. GR:   ' + \
						re.search('NO.[5][0][0]\d{7}', j[i]).group())
				counter1 += 1

			if j[i] == 'receipt' \
			and j[i+1] == 'date' and j[i+2] == ':':
				print(str(counter2) + '. Date: ' + \
				re.search('[01][0-9]\/[0123][0-9]\/[12][0-9][0-9][0-9]', \
				j[i+3]).group())
				counter2 += 1

			if j[i] == 'PO' and j[i+1] == ':':
				print(str(counter3) + '. PO:   ' + \
				re.search('[4][5][0]\d{7}', j[i+2]).group())
				counter3 += 1

		


essentialtext(big)