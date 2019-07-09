import re

with open('eng.txt', 'rt', encoding = 'utf-8') as infile:
	contents = infile.read().split()


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

essentialtext(contents)