import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from db_connect import get_api_data

# En esta simulación, fingimos que el test solo espera "id" y "name"
EXPECTED_KEYS = {"id", "name"}

def test_api_adaptive_validation():
    data = get_api_data()

    assert isinstance(data, list), "La respuesta de la API no es una lista"

    for item in data:
        assert isinstance(item, dict), "Cada ítem debe ser un diccionario"

        keys_recibidas = set(item.keys())
        claves_faltantes = EXPECTED_KEYS - keys_recibidas
        claves_extra = keys_recibidas - EXPECTED_KEYS

        assert not claves_faltantes, f"Faltan claves esperadas: {claves_faltantes}"

        if claves_extra:
            print(f"[WARNING] Nuevos campos detectados: {claves_extra}")
        
        # Si querés hacer logging real, usar `logging.warning()` aquí
        
        # Validaciones mínimas sobre los campos que sí esperamos
        assert isinstance(item["id"], int)
        assert isinstance(item["name"], str)
