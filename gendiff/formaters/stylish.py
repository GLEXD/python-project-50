def format_value(value, depth):
    indent = "    " * depth
    if isinstance(value, dict):
        lines = ["{"]
        for key, val in value.items():
            lines.append(f"{indent}    {key}: {format_value(val, depth + 1)}")
        lines.append(f"{indent}}}")
        return "\n".join(lines)
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    elif value == "":
        return " "
    else:
        return str(value)


def convert_to_stylish(diff, depth=0):
    indent = "    " * depth
    lines = []

    for item in diff:
        key = item["key"]
        status = item["status"]

        if status == "nested":
            nested_value = convert_to_stylish(item["nested"], depth + 1)
            lines.append(f"{indent}    {key}: {nested_value}")
        elif status == "added":
            value = format_value(item["new_value"], depth + 1)
            lines.append(f"{indent}  + {key}: {value}")
        elif status == "removed":
            value = format_value(item["old_value"], depth + 1)
            lines.append(f"{indent}  - {key}: {value}")
        elif status == "updated":
            old_value = format_value(item["old_value"], depth + 1)
            new_value = format_value(item["new_value"], depth + 1)
            lines.append(f"{indent}  - {key}: {old_value}")
            lines.append(f"{indent}  + {key}: {new_value}")
        elif status == "unchanged":
            value = format_value(item["old_value"], depth + 1)
            lines.append(f"{indent}    {key}: {value}")

    result = "\n".join(lines)
    if depth == 0:
        return "{\n" + result + "\n}"
    else:
        return "{\n" + result + "\n" + indent + "}"
