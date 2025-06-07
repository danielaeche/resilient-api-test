import irisnative
import json

def get_api_data():
    """
    Connects to InterSystems IRIS and returns the JSON response as a Python dictionary.
    Calls the GetAllPatients method from the Dpacientes.DataAPI class.
    """
    host = "localhost"
    port = 1972
    namespace = "USER"
    username = "admin"
    password = "123456"

    # Establish connection
    connection = irisnative.createConnection(host, port, namespace, username, password)
    iris = irisnative.createIris(connection)

    # Call the method defined in IRIS that returns a %DynamicArray with patient data
    raw_data = iris.classMethodValue("Dpacientes.DataAPI", "GetAllPatients")

    # Close the connection
    connection.close()

    # Convert JSON string to Python object
    return json.loads(str(raw_data))
