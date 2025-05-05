import json


def compare_jsons(file1_path, file2_path):
    with open(file1_path) as f1, open(file2_path) as f2:
        data1 = json.load(f1)
        data2 = json.load(f2)
    return data1 == data2
