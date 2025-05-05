import json


def generate_diff(file1_path, file2_path):
    data1 = json.load(open(file1_path))
    data2 = json.load(open(file2_path))

    def stringify(value):
        if isinstance(value, bool):
            return 'true' if value else 'false'
        if value is None:
            return 'null'
        return str(value)
    diff = []
    keys = sorted(data1.keys() | data2.keys())
    for key in keys:
        val1 = data1.get(key)
        val2 = data2.get(key)
        if key not in data2:
            diff.append(f"  - {key}: {stringify(val1)}")
        elif key not in data1:
            diff.append(f"  + {key}: {stringify(val2)}")
        elif val1 != val2:
            diff.append(f"  - {key}: {stringify(val1)}")
            diff.append(f"  + {key}: {stringify(val2)}")
        else:
            diff.append(f"    {key}: {stringify(val1)}")
    return '{\n' + '\n'.join(diff) + '\n}'
