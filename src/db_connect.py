import irisnative
import json


# Configuración de conexión a InterSystems IRIS
host = "localhost"
port = 1972
namespace = "USER"
username = "admin"
password = "123456"

# Establece la conexión con la instancia IRIS
connection = irisnative.createConnection(host, port, namespace, username, password)
iris = irisnative.createIris(connection)

# Llama al método definido en la clase Daniela.DataAPI
# Este método devuelve un JSON como string representando los pacientes registrados
json_data = iris.classMethodValue("Daniela.DataAPI", "GetAllPatients")

# Convierte el string JSON a estructura Python (lista de diccionarios)
parsed = json.loads(str(json_data))
# Muestra el contenido formateado
print(json.dumps(parsed, indent=2))

# Cierra la conexión
connection.close()
