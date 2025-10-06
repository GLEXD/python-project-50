def generate_indent(depth):
    indent_size = 4
    return " " * (depth * indent_size)


def format_value(value, indent_level):
    indent = generate_indent(indent_level)
    if isinstance(value, dict):
        items = [
            f"{indent}    {k}: {format_value(v, indent_level + 1)}"
            for k, v in value.items()
        ]
        items_str = "\n".join(items)
        return f"{{\n{items_str}\n{indent}}}"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return "true" if value else "false"
    elif value == "":
        return ""
    else:
        return str(value)


def convert_to_stylish(diff, depth=1):
    indent = generate_indent(depth)
    result = []

    for item in diff:
        key = item["key"]
        status = item["status"]

        def val_str(v):
            s = format_value(v, depth)
            return f" {s}" if s != "" else ""

        if status == "nested":
            nested = convert_to_stylish(item["nested"], depth + 1)
            result.append(f"{indent}{key}: {nested}")
        elif status == "added":
            result.append(f"{indent[:-2]}+ {key}:{val_str(item['new_value'])}")
        elif status == "removed":
            result.append(f"{indent[:-2]}- {key}:{val_str(item['old_value'])}")
        elif status == "updated":
            result.append(f"{indent[:-2]}- {key}:{val_str(item['old_value'])}")
            result.append(f"{indent[:-2]}+ {key}:{val_str(item['new_value'])}")
        elif status == "unchanged":
            result.append(f"{indent}{key}:{val_str(item['old_value'])}")

    result_str = "\n".join(result)
    outer_indent = generate_indent(depth - 1)

    if depth > 1:
        return f"{{\n{result_str}\n{outer_indent}}}"
    else:
        return f"{{\n{result_str}\n}}"
