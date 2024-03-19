# Image files contain binary data, and reading them 
# as text will lead to decoding errors. 
# So we use 'rb' instead of 'r'

#f = open("/Users/alice/Desktop/crab.png", 'rb')
f = open("/Users/alice/Desktop/one_pixel.png", 'rb')

lines = f.readlines()
print(lines)
f.close()

# Image files can be opened in this way, 
# but we only read its binary info represented as 
# hexadecimal characters like \xe9\x09


