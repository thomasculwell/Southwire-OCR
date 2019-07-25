import tempfile
import subprocess
import os

def ocr(imgfile):
    temp = tempfile.NamedTemporaryFile(delete=False)

    process = subprocess.Popen(['tesseract', imgfile, temp.name], \
    stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    process.communicate()

    with open(temp.name + '.txt', 'r', encoding = 'utf-8') as handle:
        contents = handle.read().split()

    os.remove(temp.name + '.txt')
    # os.remove(temp.name)

    return contents

txt = ocr('600x600.tif')
print(txt)
