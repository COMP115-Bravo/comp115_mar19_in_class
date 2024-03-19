from PIL import Image

# Create an image of 3 by 2 (width by height)
img_pixels = Image.new('L', (3, 2)) 

pixels = [255, 0, 255, 128, 255, 128]
img_pixels.putdata(pixels)

# Read one pixel
pixel_value = img_pixels.getpixel((1, 0)) # col, row
print(f"Red: {pixel_value}")

# # Change one pixel
# img_pixels.putpixel((2, 1), 0)

# Save the image to an image file named pixels
img_pixels.save('six_pixels_gray.png')

img_pixels.show()
img_pixels.close()