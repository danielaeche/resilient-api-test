# Classifies a schema change based on expected vs. received keys.
# Returns a status ("critical", "acceptable", "stable") with the missing and extra keys.

def classify_schema_change(expected_keys, received_keys):
    missing_keys = expected_keys - received_keys
    extra_keys = received_keys - expected_keys

    if missing_keys:
        return "critical", missing_keys, extra_keys
    if extra_keys:
        return "acceptable", missing_keys, extra_keys
    return "stable", missing_keys, extra_keys
