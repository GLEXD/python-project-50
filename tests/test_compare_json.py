import json
import pytest
from gendiff.compare_json import compare_jsons


def load_json(file_path):
    with open(file_path) as f:
        return json.load(f)
def test_json_comparison():
    file1 = "tests/test_data/file1.json"
    file2 = "tests/test_data/file2.json"
    result = compare_jsons(file1, file2)
    assert result == True
