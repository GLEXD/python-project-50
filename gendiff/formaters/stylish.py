def generate_indent(depth):
    return " " * (depth * 4)


def format_value(value, depth):
    indent = generate_indent(depth)
    if isinstance(value, dict):
        items = [
            f"{indent}    {k}: {format_value(v, depth + 1)}"
            for k, v in value.items()
        ]
        return f"{{\n{chr(10).join(items)}\n{indent}}}"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def convert_to_stylish(diff, depth=1):
    indent = generate_indent(depth)
    result = []

    for item in diff:
        key = item["key"]
        status = item["status"]

        if status == "nested":
            nested = convert_to_stylish(item["nested"], depth + 1)
            result.append(f"{indent}{key}: {nested}")
        elif status == "added":
            new_value = format_value(item["new_value"], depth)
            result.append(f"{indent[:-2]}+ {key}: {new_value}")
        elif status == "removed":
            old_value = format_value(item["old_value"], depth)
            result.append(f"{indent[:-2]}- {key}: {old_value}")
        elif status == "updated":
            old_value = format_value(item["old_value"], depth)
            new_value = format_value(item["new_value"], depth)
            result.append(f"{indent[:-2]}- {key}: {old_value}")
            result.append(f"{indent[:-2]}+ {key}: {new_value}")
        elif status == "unchanged":
            old_value = format_value(item["old_value"], depth)
            result.append(f"{indent}{key}: {old_value}")

    result_str = "\n".join(result)
    outer_indent = generate_indent(depth - 1)

    if depth > 1:
        return f"{{\n{result_str}\n{outer_indent}}}"
    else:
        return f"{{\n{result_str}\n}}"
