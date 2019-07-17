# southwireOCR
Southwire OCR Project Repository

KEY WORDS:
OCR - Optical Character Recognition
Essential Information - Receiving Report #, Purchase Order #, Date, and Person who received the document

GOAL:
Automate the process of inputting/uploading Southwire's goods receipt slips and their accompanying picking/delivery ticket(s) along with essential information identifiers into ApplicationXtender. Without going into too much detail, I plan to do this by writing a Python script/program that is capable of doing the following:

1. Utilize OCR technology to gain access to the text from each scanned image. Use this text to recognize if the scanned image is a goods receipt slip or a picking ticket. Also use this text to search for essential information on the goods receipts using simple logic and regular expressions.
2. Order the image files into a specific order based on their identity, and create a dictionary that matches goods receipts with their respective picking tickets.
3. Crop the images around where there essential information is typically located (depends on the dpi of the scan, but I accounted for this) and then utilize OCR technology again to gain access to the text from each cropped image. With this text in a list, search the list for the essential information using simple logic and regular expressions.
4. Compare the essential information found from the full text list to the cropped text list and create variables that indicates what the true value of each piece of essential information is.
5. Create and output a .txt file that contains, line by line, the essential information one goods receipt and matching picking ticket with the addition of the name of the picking ticket file that goes with that specific essential information.
6. Send the .txt file and accompanying picking ticket files to Rachel Argo at corporate who has a way to automatically upload batches with this as her input.


PROCESS:
1. Scan Document --> Image File (Scanner)
2. Image File --> Plain Text (OCR and Python Script)
3. Plain Text --> Essential Information (Python Script)
4. Essential Information --> Text File (Python Script)
5. Text File --> ApplicationXtender (Rachel Argo)