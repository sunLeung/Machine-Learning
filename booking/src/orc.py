import pytesseract

from PIL import Image

image = Image.open('D://Machine-Learning//booking//src//image.png')

vcode = pytesseract.image_to_string(image)

print(vcode)
