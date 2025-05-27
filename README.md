# Resiliencia adaptativa para Pruebas Automatizadas de APIs usando InterSystems IRIS

Este proyecto demuestra un enfoque de resiliencia adaptativa para pruebas automatizadas de APIs REST ante cambios en la estructura del JSON. La solución se basa en una conexión desde Python a una clase personalizada en InterSystems IRIS escrita en ObjectScript, lo que permite validar dinámicamente si los cambios son coherentes con el modelo de datos, sin acceder directamente a la base mediante la Python DB API.

## Objetivo

- Evitar falsos negativos en pruebas automatizadas cuando se agregan, eliminan o reordenan campos del JSON.
- Consultar la base de datos real para entender si el cambio es válido o debe reportarse como error.
- Proponer una arquitectura resiliente, adaptable y extensible para entornos complejos.

## Tecnologías usadas

- Python 3
- Pytest
- Requests
- InterSystems IRIS (como backend de datos)
- `irisnative` (driver de conexión desde Python)
- JSONSchema (opcional)
- FastAPI o Flask (opcional, para simular endpoints)

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

## Instalar dependencias

pip install -r requirements.txt

## Tests
Se incluye una versión estricta del test (que falla si cambia la estructura) y una versión con validación adaptativa, que absorbe diferencias no críticas sin comprometer la integridad del test.

/tests/

├── test_api_strict.py      ← Falla si cambia el JSON
├── test_api_adaptive.py    ← Incluye lógica adaptativa (warning, no crash)

### Ejecutar pruebas

pytest -s tests/test_api_strict.py
pytest -s tests/test_api_adaptive.py

## Justificación de diseño

Se optó por encapsular la consulta SQL en una clase ObjectScript (Daniela.DataAPI) porque acceder directamente a los registros mediante la Python DB API presentó restricciones de permisos y visibilidad sobre estructuras internas. La solución implementada aprovecha la capacidad de IRIS para exponer dinámicamente objetos JSON a través de métodos invocables, permitiendo una conexión segura, controlada y estructurada desde Python.

## Autoría

Este proyecto fue desarrollado como parte del concurso técnico de InterSystems 2025.
🔗 Enlace al artículo completo: próximamente
