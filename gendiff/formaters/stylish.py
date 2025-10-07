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
        return "''"
    else:
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
            print(f"DEBUG REMOVED: {key=}, {item=}")
            if key == "wow":
                print(f"DEBUG WOW: old_value is {repr(item['old_value'])}")
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