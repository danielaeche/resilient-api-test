import pytest
import sys
import os
import logging

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from db_connect import get_api_data

# Configura el logger
logging.basicConfig(level=logging.WARNING)

# Solo esperamos estas claves
EXPECTED_KEYS = {"id", "name"}

def test_api_adaptive_validation():
    data = get_api_data()

    assert isinstance(data, list), "La respuesta de la API no es una lista"

    claves_extra_globales = set() 

    for item in data:
        assert isinstance(item, dict), "Cada ítem debe ser un diccionario"

        keys_recibidas = set(item.keys())
        claves_faltantes = EXPECTED_KEYS - keys_recibidas
        claves_extra = keys_recibidas - EXPECTED_KEYS

        assert not claves_faltantes, f"Faltan claves esperadas: {claves_faltantes}"

        claves_extra_globales.update(claves_extra)

        # Validaciones mínimas sobre los campos esperados
        assert isinstance(item["id"], int)
        assert isinstance(item["name"], str)

    # Emitimos un único warning al final si hubo claves adicionales
    if claves_extra_globales:
        logging.warning(f"Nuevos campos detectados: {claves_extra_globales}")
