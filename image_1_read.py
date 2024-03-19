"""
By using Python Imaging Library (PIL), we can see the images properly and process them easily
https://github.com/python-pillow/Pillow/blob/main/src/PIL/Image.py#L2354C1-L2450C1
https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new

To install PIL(pillow):
https://pillow.readthedocs.io/en/stable/installation.html
"""
from PIL import Image
img = Image.open("/Users/alice/Desktop/crab.png")

print("Image format:", img.format)
print("Image size:", img.size)
print("Image width:", img.width)
print("Image height:", img.height)

img.show()
img.close()

#img.show()
