import json
from PIL import Image, ImageDraw, ImageFont
from random import randint


def write_to_file(data: dict, filename: str) -> None:
    with open(filename, mode='w') as file:
        write_data = json.dumps(data, separators=(',', ':'))
        file.write(write_data)


def read_data_from_file(filename: str) -> dict:
    with open(filename, mode='r') as file:
        data = (json.load(file))
    return data


def create_image(quad: dict, image_name: str) -> None:

    img = Image.new('RGB', (2000, 1000), (255, 255, 255))
    draw = ImageDraw.Draw(img)
    for quad_number, rectangle in quad.items():

        coords = list(rectangle)

        # Prepare text
        text_x, text_y = text_coordinates(coords)
        fontsize = 15
        font = ImageFont.truetype(font="../fonts/Roboto-Thin.ttf", size=fontsize)

        # draw result
        draw.polygon(coords, fill=(randint(0, 255), randint(0, 255), randint(0, 255)), outline='yellow')
        draw.text((text_x, text_y), quad_number, font=font, fill='yellow')
    img.save(image_name)


def text_coordinates(quad: list) -> tuple:
    all_x_coords, all_y_coords = [], []
    for coord in quad:
        all_x_coords.append(coord[0])
        all_y_coords.append(coord[1])

    # all_x_coords.remove(max(all_x_coords))
    # all_x_coords.remove(min(all_x_coords))
    # all_y_coords.remove(max(all_y_coords))
    # all_y_coords.remove(min(all_y_coords))

    average_x = max(all_x_coords) - (max(all_x_coords) - min(all_x_coords)) / 2  # + min(all_x_coords)
    average_y = max(all_y_coords) - (max(all_y_coords) - min(all_y_coords)) / 2  # + min(all_y_coords)

    return average_x * 0.97, average_y * 0.95
