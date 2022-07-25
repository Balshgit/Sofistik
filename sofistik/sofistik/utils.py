import json
import logging
import sys
import time
from functools import wraps
from pathlib import Path
from random import randint

from PIL import Image, ImageDraw, ImageFont

logger = logging.getLogger('main_logger')
formatter = logging.Formatter(datefmt="%Y.%m.%d %H:%M:%S",
                              fmt='%(asctime)s | %(levelname)s | func name: %(funcName)s | message: %(message)s')
handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(formatter)
logger.setLevel(logging.INFO)
logger.addHandler(handler)


def time_execute(func):
    """
    Decorator for calculate execution time

    :param func: decorated function
    """
    @wraps(func)
    def new_func(*args, **kwargs):
        begin = time.time()
        func(*args, **kwargs)
        end = time.time()
        dt = end - begin
        logger.info(f'{func.__name__} ended its work: in {round(dt, 2)} seconds.')

    return new_func


def write_to_file(data: dict, filename: str) -> None:
    """
    Write dict to file in json format

    :param data: Data to write
    :param filename: File name in absolute path
    """
    with open(filename, mode='w') as file:
        write_data = json.dumps(data, separators=(',', ':'))
        file.write(write_data)


def read_data_from_file(filename: Path) -> dict:
    """
    Read data from file. Data must be in json format

    :param filename: filename for read data from

    :return: Data as dict from file
    """
    with open(filename, mode='r') as file:
        data = (json.load(file))
    for quad_number, coords in data.items():
        rectangle = [list(coord) for coord in coords]
        data[quad_number] = rectangle
    return data


@time_execute
def create_image(quad_dict: dict, image_name: str) -> None:
    """
    Create image from quad dict data

    :param quad_dict: Data with quad number and it coords as a list or tuple
    :param image_name: Set image name
    """
    img = Image.new('RGB', (1500, 500), (255, 255, 255))
    draw = ImageDraw.Draw(img)

    # quad = mirror_quad_by_y(quad_dict)
    for quad_number, rectangle in quad_dict.items():
        # Prepare text
        fontsize = 15
        text_x, text_y = get_text_coordinates(rectangle, fontsize)
        font = ImageFont.truetype(font="fonts/Roboto-Thin.ttf", size=fontsize)

        # draw result
        draw.polygon(rectangle, fill=(randint(0, 255), randint(0, 255), randint(0, 255)), outline='yellow')

        draw.text((text_x, text_y), str(quad_number), font=font, fill='black')
    img.save(image_name)


def get_text_coordinates(rectangle: list, fontsize: int) -> tuple:
    """
    Write quad number in central of rectangle

    :param rectangle: List of rectangle coords
    :param fontsize: Set font size

    :return: X, Y coords in the middle of rectangle
    """
    all_x_coords, all_y_coords = [], []
    for coord in rectangle:
        all_x_coords.append(coord[0])
        all_y_coords.append(coord[1])

    average_x = (max(all_x_coords) + min(all_x_coords)) / 2 - fontsize / 2 / 2 * 6
    average_y = (max(all_y_coords) + min(all_y_coords)) / 2 - fontsize / 2

    return average_x * 1, average_y * 1


def mirror_quad_by_y(quad: dict) -> dict:
    """
    Mirror quad by Y coord

    :param quad: Quad instance

    :return: Quad instance with mirror y coords
    """
    all_y_coords = []
    for rectangle in quad.values():
        for coord in rectangle:
            all_y_coords.append(coord[1])
    max_y = max(all_y_coords)
    for quad_number, rectangle in quad.items():
        for coord in rectangle:
            coord[1] = max_y - coord[1]
        quad[quad_number] = [tuple(coord) for coord in rectangle]
    return quad
