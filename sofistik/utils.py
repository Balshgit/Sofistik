import json
from PIL import Image, ImageDraw, ImageFont


def write_to_file(data: dict, filename: str) -> None:
    with open(filename, mode='w') as file:
        write_data = json.dumps(data, separators=(',', ':'))
        file.write(write_data)


def read_data_from_file(filename: str) -> dict:
    with open(filename, mode='r') as file:
        data = (json.load(file))
    return data


def create_image(data: list, image_name: str) -> None:
    img = Image.new('RGB', (2000, 1000), (255, 255, 255))
    d = ImageDraw.Draw(img)
    for rectangle in data:
        d.polygon(rectangle, fill="green", outline='yellow')
    img.save(image_name)
