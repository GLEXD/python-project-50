from gendiff.parser import get_data
from gendiff.diff import build_diff
from gendiff.formater import format_diff


def generate_diff(file_1, file_2, format="stylish"):
    dict_1 = get_data(file_1)
    dict_2 = get_data(file_2)
    diff = build_diff(dict_1, dict_2)
    return format_diff(diff, format)
