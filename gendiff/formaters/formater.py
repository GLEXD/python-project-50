from gendiff.formaters.json import convert_to_json
from gendiff.formaters.plain import convert_to_plain
from gendiff.formaters.stylish import convert_to_stylish


class FormatError(Exception):
    pass


def format_diff(diff, format):
    if format == 'stylish':
        return convert_to_stylish(diff)
    elif format == 'plain':
        return convert_to_plain(diff)
    elif format == 'json':
        return convert_to_json(diff)
    else:
        raise FormatError(f'Unknown format: {format}')