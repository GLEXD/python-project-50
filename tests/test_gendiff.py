FILE1_JSON = "tests/fixtures/file1.json"
FILE2_JSON = "tests/fixtures/file2.json"


def test_generate_diff():
    expected = """{
  - follow: false
    host: hexlet.io
  - proxy: 123.234.53.22
  - timeout: 50
  + timeout: 20
  + verbose: true
}"""
    from gendiff import generate_diff
    result = generate_diff(FILE1_JSON, FILE2_JSON)
    assert result == expected
