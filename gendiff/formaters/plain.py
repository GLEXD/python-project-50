def format_value(value):
    if isinstance(value, dict):
        return "[complex value]"
    elif isinstance(value, str):
        return f"'{value}'"
    elif value is None:
        return "null"
    elif isinstance(value, bool):
        return str(value).lower()
    return str(value)


def generate_messages(diff, path=""):
    messages = []
    for item in diff:
        key = item["key"]
        full_path = f"{path}.{key}" if path else key
        status = item["status"]

        if status == "nested":
            nested_diff = item["nested"]
            messages.extend(generate_messages(nested_diff, full_path))
        elif status == "added":
            formatted_value = format_value(item["new_value"])
            message = (
                f"Property '{full_path}' was added with value: "
                f"{formatted_value}"
            )
            messages.append(message)
        elif status == "removed":
            message = f"Property '{full_path}' was removed"
            messages.append(message)
        elif status == "updated":
            formatted_old_value = format_value(item["old_value"])
            formatted_new_value = format_value(item["new_value"])
            message = (
                f"Property '{full_path}' was updated. From "
                f"{formatted_old_value} to {formatted_new_value}"
            )
            messages.append(message)
    return messages


def convert_to_plain(diff):
    messages = generate_messages(diff)
    return "\n".join(messages)
