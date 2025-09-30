import json
import os

import yaml


class ExtensionError(Exception):
    pass


def parse_data(file, extension):
    if extension == 'json':
        return json.loads(file)
    elif extension in ['yml', 'yaml']:
        return yaml.load(file, Loader=yaml.Loader)
    else:
        raise ExtensionError(f'Unsupported file format: {extension}')


def get_data(file_path):
    extension = os.path.splitext(file_path)[1][1:].lower()
    file_cont = file_read(file_path)
    return parse_data(file_cont, extension)


def file_read(file_path):
    with open(file_path) as file:
        return file.read()
