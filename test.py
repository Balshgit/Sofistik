import asyncio
import time
from multiprocessing import Pool
# from loguru import logger
import sys, os
import random
import json
from sofistik.sofistik.utils import mirror_quad_by_y, logger


# logger.remove()
# logger.add(sys.stdout, colorize=True, format="{time} <green>{message}</green>", level='INFO')


# def time_execute(func):
#     def new_func(*args, **kwargs):
#         begin = time.time()
#         func(*args, **kwargs)
#         end = time.time()
#         dt = end - begin
#         logger.info(f'{func.__name__} ended its work: in {round(dt,2)} seconds.')
#     return new_func
import json

# data = {
#     "10080": [(261.5, 147.0), (184.5, 102.0), (233.5, 51.0), (301.0, 77.0)],
#     "10081": [(720.0, 318.0), (624.5, 265.5), (664.0, 175.0), (756.5, 239.0)]
# }
#
#
# data = mirror_quad_by_y(data)
# logger.info(data)

from PIL import Image, ImageDraw, ImageFont

def create_image(image_name: str) -> None:

    img = Image.new('RGB', (500, 400), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    fontsize = 25
    font = ImageFont.truetype(font="fonts/Roboto-Thin.ttf", size=fontsize)

    rectangle = [(0, 0), (0, 200), (200, 200), (200, 0)]
    all_x_coords, all_y_coords = [], []
    for coord in rectangle:
        all_x_coords.append(coord[0])
        all_y_coords.append(coord[1])

    # all_x_coords.remove(max(all_x_coords))
    # all_x_coords.remove(min(all_x_coords))
    # all_y_coords.remove(max(all_y_coords))
    # all_y_coords.remove(min(all_y_coords))

    average_x = max(all_x_coords) - (max(all_x_coords) - min(all_x_coords)) / 2 - fontsize / 2 / 2 * 6
    average_y = max(all_y_coords) - (max(all_y_coords) - min(all_y_coords)) / 2 - fontsize / 2

    print(average_x, average_y)

    # Prepare text


    # draw result
    draw.polygon([(0, 0), (0, 200), (200, 200), (200, 0)], fill='green', outline='yellow')

    draw.text((average_x, average_y), '123456', font=font, fill='yellow')
    img.save(image_name)


create_image('test.png')
