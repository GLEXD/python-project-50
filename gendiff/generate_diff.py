import json
from pathlib import Path


def generate_diff(file_path1, file_path2, format_name='stylish'):


    def load_data(file_path):
        with open(file_path) as file:
            return json.load(file)

    data1 = load_data(file_path1)
    data2 = load_data(file_path2)

    all_keys = sorted(set(data1.keys()) | set(data2.keys()))
    diff = []

    for key in all_keys:
        if key not in data2:
            diff.append(f"  - {key}: {data1[key]}")

        elif key not in data1:
            diff.append(f"  + {key}: {data2[key]}")

        elif data1[key] != data2[key]:
            diff.append(f"  - {key}: {data1[key]}")
            diff.append(f"  + {key}: {data2[key]}")

        else:
            diff.append(f"    {key}: {data1[key]}")


    return "{\n" + "\n".join(diff) + "\n}"
