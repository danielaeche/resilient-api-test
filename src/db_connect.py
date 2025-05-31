import irisnative
import json

def get_api_data():
    """
    Conecta con InterSystems IRIS y retorna la respuesta JSON como diccionario de Python.
    Invoca el método GetAllPatients de la clase Dpacientes.DataAPI.
    """
    host = "localhost"
    port = 1972
    namespace = "USER"
    username = "admin"
    password = "123456"

    # Establecer conexión
    connection = irisnative.createConnection(host, port, namespace, username, password)
    iris = irisnative.createIris(connection)

    # Llamar al método definido en IRIS que devuelve un %DynamicArray con pacientes
    raw_data = iris.classMethodValue("Dpacientes.DataAPI", "GetAllPatients")

    # Cerrar la conexión
    connection.close()

    # Convertir de string JSON a objeto Python
    return json.loads(str(raw_data))
