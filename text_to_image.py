import os

from PIL import Image, ImageDraw, ImageFont



img = Image.new('RGB', (2000, 1000), (255, 255, 255))
d = ImageDraw.Draw(img)
fontsize = 96
font = ImageFont.truetype(font="fonts/Roboto-Black.ttf", size=fontsize)
d.text((20, 20), 'Hello', fill=(255, 0, 0), font=font)
img.save('test_image_from_python.png')

print(os.environ.get('PATH'))
