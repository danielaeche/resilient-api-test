import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from db_connect import get_api_data


def test_json_structure_is_list():
    data = get_api_data()
    assert isinstance(data, list), "La respuesta no es una lista"

def test_each_item_has_expected_keys():
    expected_keys = {"id", "name", "age"}
    data = get_api_data()

    for item in data:
        assert isinstance(item, dict), "Cada item debe ser un diccionario"
        missing = expected_keys - item.keys()
        assert not missing, f"Faltan claves en el item: {missing}"
