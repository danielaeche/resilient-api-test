import logging
from jsonschema import validate
from jsonschema.exceptions import ValidationError

from src.db_connect import get_api_data
from schema import PATIENT_SCHEMA, classify_schema_change, SCHEMA_STATUS_HANDLERS

logging.basicConfig(level=logging.WARNING)

EXPECTED_KEYS = set(PATIENT_SCHEMA["properties"].keys())

# Runs adaptive validation on API response.
# Checks for missing or extra fields and logs the result based on classification.
def test_api_adaptive_validation():
    data = get_api_data()

    # Make sure the API response is a list of JSON objects
    assert isinstance(data, list), "La respuesta de la API no es una lista"

    for item in data:
        assert isinstance(item, dict), "Cada ítem debe ser un diccionario"
        
        received_keys = set(item.keys())
        status, missing, extra = classify_schema_change(EXPECTED_KEYS, received_keys)
        
        handler = SCHEMA_STATUS_HANDLERS.get(status)
        if handler:
            handler(EXPECTED_KEYS, received_keys, extra)

        # Check that expected fields have the correct data types
        try:
            validate(instance=item, schema=PATIENT_SCHEMA)
        except ValidationError as e:
            logging.error(f"Error de validación de esquema: {e.message}")
            raise
        