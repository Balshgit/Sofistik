import json


def write_to_file(data: dict, filename: str) -> None:
    with open(filename, mode='w') as file:
        write_data = json.dumps(data, separators=(',', ':'))
        file.write(write_data)


def read_data_from_file(filename: str) -> dict:
    with open(filename, mode='r') as file:
        data = (json.load(file))
    return data
