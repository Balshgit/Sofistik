import json
import logging
from random import randint
import sys
import time
from functools import wraps

from PIL import Image, ImageDraw, ImageFont


logger = logging.getLogger('main_logger')
formatter = logging.Formatter(datefmt="%Y.%m.%d %H:%M:%S", fmt='%(asctime)s | func name: %(funcName)s |'
                                                               ' message: %(message)s')
                              # fmt='%(asctime)s | %(levelname)s | process: %(process)d | module name: %(name)s | '
                              #     'func name: %(funcName)s | line number: %(lineno)s | message: %(message)s',)
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def time_execute(func):
    @wraps(func)
    def new_func(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        dt = end - begin
        logger.info(f'{func.__name__} ended its work: in {round(dt,2)} seconds.')
    return new_func


def write_to_file(data: dict, filename: str) -> None:
    with open(filename, mode='w') as file:
        write_data = json.dumps(data, separators=(',', ':'))
        file.write(write_data)


def read_data_from_file(filename: str) -> dict:
    with open(filename, mode='r') as file:
        data = (json.load(file))
    for quad_number, coords in data.items():
        rectangle = list()
        for coord in coords:
            rectangle.append(tuple(coord))
        data[quad_number] = rectangle
    return data


@time_execute
def create_image(quad: dict, image_name: str) -> None:

    img = Image.new('RGB', (2000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for quad_number, rectangle in quad.items():

        # Prepare text
        text_x, text_y = get_text_coordinates(rectangle)
        fontsize = 15
        font = ImageFont.truetype(font="../fonts/Roboto-Thin.ttf", size=fontsize)

        # draw result
        draw.polygon(rectangle, fill=(randint(0, 255), randint(0, 255), randint(0, 255)), outline='yellow')
        draw.text((text_x, text_y), quad_number, font=font, fill='yellow')
    img.save(image_name)


def get_text_coordinates(quad: list) -> tuple:
    all_x_coords, all_y_coords = [], []
    for coord in quad:
        all_x_coords.append(coord[0])
        all_y_coords.append(coord[1])

    # all_x_coords.remove(max(all_x_coords))
    # all_x_coords.remove(min(all_x_coords))
    # all_y_coords.remove(max(all_y_coords))
    # all_y_coords.remove(min(all_y_coords))

    average_x = max(all_x_coords) - (max(all_x_coords) - min(all_x_coords)) / 2
    average_y = max(all_y_coords) - (max(all_y_coords) - min(all_y_coords)) / 2

    return average_x * 0.97, average_y * 0.95
