# Validacion estructural adaptativa para Pruebas Automatizadas de APIs usando InterSystems IRIS

Este repositorio contiene un proyecto técnico de validación estructural adaptativa ante cambios en la respuesta JSON de datos expuestos de InterSystems IRIS.

Incluye pruebas automatizadas en Python que contrastan dos enfoques:

- **Validación estricta**: falla ante cualquier diferencia estructural.
- **Validación adaptativa**: tolera cambios menores y registra advertencias.


## Estructura del repositorio

/src/ → Código fuente principal (conexión a IRIS)

/schema/ → Lógica de clasificación, logueo y manejo de resultados

/tests/ → Pruebas automatizadas

/config/ → Carpeta reservada para futuras configuraciones (vacía)

/structure_warnings_log.ndjson → Registro estructurado de cambios detectados

/conftest.py → Configuración para que pytest detecte módulos correctamente

requirements.txt → Dependencias de Python

README.md → Este archivo

venv/→ Entorno virtual (excluido en Git)

## Requisitos

- Tener una instancia de IRIS corriendo (local o remota)
- Python 3.8+
- Acceso de lectura a la base IRIS (con usuario, host y puerto)

### Base de datos IRIS

Este proyecto utiliza una instancia local de InterSystems IRIS en Docker para simular una base de datos con datos reales expuestos como JSON.
Podés correrlo de dos maneras:

1. **Manual** (como se hizo en este MVP):
Podés correr una imagen de IRIS manualmente desde Docker para simular la base de datos.

2. **Con `docker-compose`** *(opcional, no incluido en este repo)*:
Si queres automatizar la ejecución, podés crear un archivo docker-compose.yml por tu cuenta.
  
## Instalación

1. git clone https://github.com/danielaeche/resilient-api-test.git

2. pip install -r requirements.txt

## Cómo ejecutar las pruebas
Desde la raíz del proyecto:

    pytest -s tests/test_api_strict.py
    pytest -rA tests/test_api_adaptive.py

### Descripción de tests:
- /tests/test_api_strict.py: Test que falla ante cualquier diferencia con la estructura esperada.

- /tests/test_api_adaptive.py: Test que valida la estructura de forma adaptativa, clasifica el cambio como stable, acceptable o critical y guarda trazabilidad en formato NDJSON.

## Notas sobre diseño
Esta implementación usa una clase ObjectScript como capa intermedia para estructurar los datos en JSON.
Por restricciones de entorno, no se utilizó acceso directo a las tablas mediante Python DB API, lo cual sería el enfoque ideal para validar en tiempo real la estructura del sistema.

## Autoría

Este proyecto fue desarrollado como parte del concurso técnico de InterSystems 2025.

🔗 Enlace al artículo completo: 
