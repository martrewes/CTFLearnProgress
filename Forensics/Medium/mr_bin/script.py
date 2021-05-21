from exif import Image

with open('image.jpg', 'rb') as image_file:
    my_image = Image(image_file)

print(my_image.y_resolution)
