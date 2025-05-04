import argparse
import json
from pathlib import Path


def parse_file(file_path):
    return json.load(open(file_path))


def main():
    parser = argparse.ArgumentParser(
        prog="gendiff",
        description="Compares two configuration files and shows a difference."
    )


    parser.add_argument("first_file")
    parser.add_argument("second_file")
    parser.add_argument('-f' ,'--format', help='set format of output')
    args = parser.parse_args()


    data1 = parse_file(args.first_file)
    data2 = parse_file(args.second_file)

    print("File 1:", data1)
    print("File 2:", data2)


if __name__ == "__main__":
    main()