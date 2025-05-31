# Validacion estructural daptativa para Pruebas Automatizadas de APIs usando InterSystems IRIS

Este repositorio contiene un proyecto técnico de validación estructural adaptativa ante cambios en la respuesta JSON de datos expuestos de InterSystems IRIS.

Incluye pruebas automatizadas en Python que contrastan dos enfoques:

- **Validación estricta**: falla ante cualquier diferencia estructural.
- **Validación adaptativa**: tolera cambios menores y registra advertencias.


## Estructura del repositorio

/src                → Código fuente principal

/tests              → Pruebas automatizadas

/config             → Configs opcionales 

README.md           → Este archivo

requirements.txt    → Dependencias del entorno

venv/               → Entorno virtual (excluido en Git)

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
  
   
### Instalar dependencias

pip install -r requirements.txt

## Tests
Se incluye una versión estricta del test (que falla si cambia la estructura) y una versión con validación adaptativa, que absorbe diferencias no críticas sin comprometer la integridad del test.

/tests/

├── test_api_strict.py      ← Falla si cambia el JSON

├── test_api_adaptive.py    ← Incluye lógica adaptativa (warning, no crash)

### Ejecutar pruebas

pytest -s tests/test_api_strict.py

pytest -rA tests/test_api_adaptive.py

### Notas sobre diseño
Esta implementación usa una clase ObjectScript como capa intermedia para estructurar los datos en JSON.
Por restricciones de entorno, no se utilizó acceso directo a las tablas mediante Python DB API, lo cual sería el enfoque ideal para validar en tiempo real la estructura del sistema.

## Autoría

Este proyecto fue desarrollado como parte del concurso técnico de InterSystems 2025.

🔗 Enlace al artículo completo: 
