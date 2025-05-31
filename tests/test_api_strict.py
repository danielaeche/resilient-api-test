import pytest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'src')))
from db_connect import get_api_data


@pytest.fixture(scope="module")
def api_data():
    return get_api_data()

def test_json_structure_is_list(api_data):
    assert isinstance(api_data, list), "La respuesta no es una lista"


def test_each_item_has_expected_keys(api_data):
    expected_keys = {"id", "name", "age"}

    for idx, item in enumerate(api_data):
        assert isinstance(item, dict), f"El ítem {idx} no es un diccionario: {item}"
        missing = expected_keys - item.keys()
        extra = item.keys() - expected_keys

        assert not missing, f"Faltan campos obligatorios en el ítem {idx}: {missing}"
        assert not extra, f"Se detectaron campos inesperados en el ítem {idx}: {extra}. Solo se esperaban: {expected_keys}"
