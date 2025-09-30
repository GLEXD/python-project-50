#!/usr/bin/env python3

from gendiff import generate_diff
from gendiff.cli import parse_args


def main():
    first_file, second_file, format_name = parse_args()
    print(generate_diff(first_file, second_file, format_name))


if __name__ == "__main__":
    main()
