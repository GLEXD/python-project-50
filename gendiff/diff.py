def build_diff(dict1, dict2):
    diff = []
    all_keys = sorted(set(dict1.keys()) | set(dict2.keys()))

    for key in all_keys:
        if key not in dict2:
            diff.append(
                {"key": key, "status": "removed", "old_value": dict1[key]}
            )
        elif key not in dict1:
            diff.append(
                {"key": key, "status": "added", "new_value": dict2[key]}
            )
        elif isinstance(dict1[key], dict) and isinstance(dict2[key], dict):
            nested_diff = build_diff(dict1[key], dict2[key])
            diff.append(
                {"key": key, "status": "nested", "nested": nested_diff}
            )
        elif dict1[key] != dict2[key]:
            diff.append({
                "key": key,
                "status": "updated",
                "old_value": dict1[key],
                "new_value": dict2[key]
            })
        else:
            diff.append(
                {"key": key, "status": "unchanged", "old_value": dict1[key]}
            )

    return diff
