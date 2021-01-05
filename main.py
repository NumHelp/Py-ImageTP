import PIL.Image
img = PIL.Image.open('pomme.jpg')
exif_data = img._getexif()
print(exif_data)
