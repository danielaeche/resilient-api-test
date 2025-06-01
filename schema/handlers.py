import logging
from .logger import log_structure_event

# Handles critical schema issues: logs and fails the test.
def handle_critical(expected, received, extra):
    log_structure_event(expected, received, extra, "critical")
    raise AssertionError(f"Critical schema issue - Missing: {expected - received}, Extra: {extra}")

# Handles acceptable schema changes: logs a warning and continues.
def handle_acceptable(expected, received, extra):
    logging.warning(f"New acceptable fields detected: {extra}")
    log_structure_event(expected, received, extra, "acceptable")

# Handles stable schema responses: logs normal success.
def handle_stable(expected, received, _):
    log_structure_event(expected, received, set(), "stable")

SCHEMA_STATUS_HANDLERS = {
    "critical": handle_critical,
    "acceptable": handle_acceptable,
    "stable": handle_stable
}
