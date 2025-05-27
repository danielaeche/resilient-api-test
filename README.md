# Resiliencia adaptativa para Pruebas Automatizadas de APIs usando InterSystems IRIS

Este repositorio contiene un proyecto técnico de validación estructural dinámica ante cambios en la respuesta JSON de una API respaldada por InterSystems IRIS.

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

## Autoría

Este proyecto fue desarrollado como parte del concurso técnico de InterSystems 2025.

🔗 Enlace al artículo completo: próximamente
