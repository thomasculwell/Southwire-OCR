# tesseract demonstration

import re

filename = 'eng2.txt'
with open(filename, 'r', encoding = 'utf-8') as handle:
    listoftext = handle.read().split()

counter = 1
counter1 = 1
counter2 = 2
counter3 = 3

for i in range(len(listoftext)):
		if listoftext[i] == 'No.' or listoftext[i] == 'NO.':
			try:
				print(str(counter1) + '. GR:   ' + \
				re.search('[5][0][0]\d{7}', listoftext[i+1]).group())
			except:
				try:
					print(str(counter1) + '. GR:   ' + \
					re.search('No.[5][0][0]\d{7}', listoftext[i]).group())
				except:
					print(str(counter1) + '. GR:   ' + \
					re.search('NO.[5][0][0]\d{7}', listoftext[i]).group())
			counter1 += 1

		if listoftext[i] == 'receipt' \
		and listoftext[i+1] == 'date' and listoftext[i+2] == ':':
			print(str(counter2) + '. Date: ' + \
			re.search('[01][0-9]\/[0123][0-9]\/[12][0-9][0-9][0-9]', \
			listoftext[i+3]).group())
			counter2 += 1

		if listoftext[i] == 'PO' and listoftext[i+1] == ':':
			print(str(counter3) + '. PO:   ' + \
			re.search('[4][5][0]\d{7}', listoftext[i+2]).group())
			counter3 += 1

		if listoftext[i] == 'No.' or listoftext[i] == 'NO.' and \
		listoftext[i] == 'receipt' and listoftext[i+1] == 'date' and \
		listoftext[i+2] == ':' and listoftext[i] == 'PO' and \
		listoftext[i+1] == ':':
			print(counter)
			counter += 1