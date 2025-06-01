import json
from datetime import datetime

# Writes schema check info and status to a log file.
def log_structure_event(expected, received, extras, status, file_path="structure_warnings_log.ndjson"):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "expected_keys": list(expected),
        "received_keys": list(received),
        "new_fields_detected": list(extras),
        "status": status
    }
    with open(file_path, "a") as f:
        f.write(json.dumps(log_entry) + "\n")
