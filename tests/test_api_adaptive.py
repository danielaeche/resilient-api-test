import pytest
import sys
import os
import logging
import json
from datetime import datetime

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from db_connect import get_api_data

# Configura el logger
logging.basicConfig(level=logging.WARNING)

# Esperamos estas claves
EXPECTED_KEYS = {"id", "name", "age"}

# Crea un archivo NDJSON para registrar cambios estructurales 
def log_structure_warning(expected, received, extras):
    log_entry = {
        "timestamp": datetime.utcnow().isoformat(),
        "expected_keys": list(expected),
        "received_keys": list(received),
        "new_fields_detected": list(extras),
        "status": "passed_with_warning"
    }
    with open("structure_warnings_log.ndjson", "a") as log_file:
        log_file.write(json.dumps(log_entry) + "\n")

def test_api_adaptive_validation():
    data = get_api_data()

    assert isinstance(data, list), "La respuesta de la API no es una lista"

    global_extra_keys = set() 

    for item in data:
        assert isinstance(item, dict), "Cada ítem debe ser un diccionario"

        received_keys = set(item.keys())
        missing_keys = EXPECTED_KEYS - received_keys
        extra_keys = received_keys - EXPECTED_KEYS

        # Si faltan claves la prueba falla
        assert not missing_keys, f"Faltan claves esperadas: {missing_keys}"

        global_extra_keys.update(extra_keys)

        # Validaciones mínimas sobre los campos esperados
        assert isinstance(item["id"], int)
        assert isinstance(item["name"], str)

    # Si hay claves adicionales > warning mas log
    if global_extra_keys:
        logging.warning(f"Nuevos campos detectados: {global_extra_keys}")
        log_structure_warning(EXPECTED_KEYS, set(data[0].keys()), global_extra_keys)
