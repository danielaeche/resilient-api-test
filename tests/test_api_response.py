import json
import irisnative

def get_api_data():
    host = "localhost"
    port = 1972
    namespace = "USER"
    username = "admin"
    password = "123456"

    connection = irisnative.createConnection(host, port, namespace, username, password)
    iris = irisnative.createIris(connection)

    json_data = iris.classMethodValue("Daniela.DataAPI", "GetAllPatients")
    parsed = json.loads(str(json_data))

    connection.close()
    return parsed

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
