import json


def convert_to_json(diff):
    result = json.dumps(
        diff,
        indent=2,
        ensure_ascii=False,
        separators=(',', ': ')
    )
    return result
