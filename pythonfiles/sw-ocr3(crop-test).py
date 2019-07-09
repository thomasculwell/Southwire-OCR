#! python2
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
filename = "300x300.tif";

x1 = (0, 100, 2200, 200)
x2 = (0, 500, 1000, 700)
x3 = (0, 200, 1200, 400)

image = Image.open(filename);

cropped_image = 'cropped_image'
scores = [x1, x2, x3]
for i in scores:
    cropped_image1 = image.crop(i)
    results = pytesseract.image_to_string(cropped_image1,lang="letsgodigital",boxes=False)
    print(results)