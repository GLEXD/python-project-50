import pytest
from gendiff import generate_diff

FIXTURE_PATH = "tests/fixtures/"


@pytest.mark.parametrize("file_1, file_2, expected, format", [
    ("file_1.json", "file_2.json", "stylish.txt", "stylish"),
    ("file_1.yml", "file_2.yml", "stylish.txt", "stylish"),
    ("file_1.json", "file_2.json", "plain.txt", "plain"),
    ("file_1.yml", "file_2.yml", "plain.txt", "plain"),
    ("file_1.json", "file_2.json", "json.txt", "json"),
    ("file_1.yml", "file_2.yml", "json.txt", "json")
])
def test_gendiff(file_1, file_2, expected, format):
    file_1_path = f"{FIXTURE_PATH}/{file_1}"
    file_2_path = f"{FIXTURE_PATH}/{file_2}"
    expected_path = f"{FIXTURE_PATH}/{expected}"

    result = generate_diff(file_1_path, file_2_path, format)
    with open(expected_path) as expected_file:
        assert result == expected_file.read().rstrip("\n")
