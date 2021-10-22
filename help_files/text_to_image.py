import os

from PIL import Image, ImageDraw, ImageFont



img = Image.new('RGB', (2000, 1000), (255, 255, 255))
d = ImageDraw.Draw(img)
fontsize = 96
font = ImageFont.truetype(font="fonts/Roboto-Thin.ttf", size=fontsize)
d.text((40, 70), '12313', fill=(255, 0, 0), font=font)
d.text((1000, 500), '0903', fill=(255, 0, 0), font=font)
d.line([(40, 70), (1000, 500)], width=4, fill="#0000ff")
rectangles = [[(1000, 750), (900, 480), (425, 370), (500, 650)],
              [(1500, 350), (1300, 380), (1005, 270), (1100, 200)],
              [(1030, 250), (700, 680), (525, 870), (200, 250)]]
for rectangle in rectangles:
    d.polygon(rectangle, fill="green", outline='yellow')
d.text((600, 500), '2345', fill="yellow", font=font)
img.save('test_image_from_python.png')



