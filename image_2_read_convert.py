from PIL import Image
img = Image.open("/Users/alice/Desktop/crab.png")

# Convert the image to grayscale
gray_img = img.convert("L")
gray_img.show()
gray_img.save('crab_gray.png')

img.close()
gray_img.close()