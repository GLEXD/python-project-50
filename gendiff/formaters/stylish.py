def generate_indent(depth):
    indent_size = 4
    return " " * (depth * indent_size)


def format_value(value, depth):
    if isinstance(value, dict):
        lines = []
        inner_indent = generate_indent(depth + 1)
        for k, v in value.items():
            lines.append(f"{inner_indent}{k}: {format_value(v, depth + 1)}")
        closing_indent = generate_indent(depth)
        return "{\n" + "\n".join(lines) + f"\n{closing_indent}" + "}"
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def convert_to_stylish(diff, depth=1):
    indent = generate_indent(depth)
    result_lines = []

    def make_line(prefix, key, raw_value):
        value_str = format_value(raw_value, depth)
        if value_str == "":
            return f"{prefix}{key}:"
        else:
            return f"{prefix}{key}: {value_str}"

    for item in diff:
        key = item["key"]
        status = item["status"]

        if status == "nested":
            nested = convert_to_stylish(item["nested"], depth + 1)
            result_lines.append(f"{indent}{key}: {nested}")
        elif status == "added":
            prefix = indent[:-2] + "+ "
            result_lines.append(make_line(prefix, key, item.get("new_value")))
        elif status == "removed":
            prefix = indent[:-2] + "- "
            result_lines.append(make_line(prefix, key, item.get("old_value")))
        elif status == "updated":
            prefix_minus = indent[:-2] + "- "
            prefix_plus = indent[:-2] + "+ "
            result_lines.append(make_line(
                prefix_minus,
                key,
                item.get("old_value")
            ))
            result_lines.append(make_line(
                prefix_plus,
                key,
                item.get("new_value")
            ))
        elif status == "unchanged":
            result_lines.append(make_line(indent, key, item.get("old_value")))
        else:
            raise ValueError(f"Unknown status: {status}")

    outer_indent = generate_indent(depth - 1)
    return "{\n" + "\n".join(result_lines) + f"\n{outer_indent}" + "}"
