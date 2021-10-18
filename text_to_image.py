import os

from PIL import Image, ImageDraw, ImageFont



img = Image.new('RGB', (2000, 1000), (255, 255, 255))
d = ImageDraw.Draw(img)
fontsize = 96
font = ImageFont.truetype(font="fonts/Roboto-Thin.ttf", size=fontsize)
d.text((40, 70), '12313', fill=(255, 0, 0), font=font)
d.text((1000, 500), '0903', fill=(255, 0, 0), font=font)
img.save('test_image_from_python.png')

