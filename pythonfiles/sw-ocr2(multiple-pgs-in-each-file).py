# I really hope this works. This is code for multiple text documents
# as input, each of them with several goods receipts inside the file.

import re

database = ['scan1.txt', 'scan2.txt', 'scan3.txt']

counter1 = 1
counter2 = 1
counter3 = 1

for file in database:
	with open(file, encoding = 'utf-8') as infile:
		contents = infile.read().split()
	for i in range(len(contents)):
		if (contents[i] == 'No.' or contents[i] == 'NO.') and \
		(contents[i+1] == 'Page' or contents[i+2] == 'Page'):
			try:
				print(str(counter1) + '. GR:   ' + \
				re.match('[5][0][0]\d{7}', contents[i+1]).group())
			except:
				try:
					print(str(counter1) + '. GR:   ' + \
					re.match('No.[5][0][0]\d{7}', contents[i]).group())
				except:
					try:
						print(str(counter1) + '. GR:   ' + \
						re.match('NO.[5][0][0]\d{7}', contents[i]).group())
					except:
						print(str(counter1) + '. No GR Found')
			counter1 += 1

		if contents[i] == 'receipt' \
		and contents[i+1] == 'date' and contents[i+2] == ':':
			try:
				print(str(counter2) + '. Date: ' + \
				re.match('[01][0-9]\/[0123][0-9]\/[12][0-9][0-9][0-9]', contents[i+3]).group())
			except:
				print(str(counter2) + ('. No Date Found.'))
			counter2 += 1

		if (contents[i] == 'PO' or contents[i] == 'P0') and contents[i+1] == ':':
			try:
				print(str(counter3) + '. PO:   ' + \
				re.match('[4][5][0]\d{7}', contents[i+2]).group())
			except:
				print(str(counter3) + '. No PO Found.')
			counter3 += 1
