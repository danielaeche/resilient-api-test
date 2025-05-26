# Resiliencia adaptativa para Pruebas Automatizadas de APIs usando InterSystems IRIS

Este proyecto demuestra un enfoque de Resiliencia adaptativa para pruebas automatizadas de APIs REST ante cambios en la estructura del JSON. La solución se basa en una conexión en tiempo real con una base de datos InterSystems IRIS mediante la Python DB API, que permite validar dinámicamente si los cambios son coherentes con el modelo de datos.

## Objetivo

- Evitar falsos negativos en pruebas automatizadas cuando se agregan, eliminan o reordenan campos del JSON.
- Consultar la base de datos real para entender si el cambio es válido o debe reportarse como error.
- Proponer una arquitectura resiliente, adaptable y extensible para entornos complejos.

## Tecnologías usadas

- Python 3
- Pytest
- Requests
- InterSystems IRIS
- Python DB API (`iris` package)
- JSONSchema (opcional)
- FastAPI (opcional, para simular endpoints)

## Estructura del repositorio

/src → Código fuente principal
/tests → Pruebas automatizadas
/config → Configs opcionales (esquemas, mapeos, etc.)
README.md → Este archivo

## Requisitos

- Tener una instancia de IRIS corriendo (local o remota)
- Python 3.8+
- Acceso de lectura a la base IRIS (con usuario, host y puerto)

## Cómo correr el MVP

> Esto se completará cuando esté listo el código funcional.

## Autoría

Este proyecto fue desarrollado como parte del concurso técnico de InterSystems 2025.

---
🔗 Pronto vas a encontrar el enlace al artículo completo acá.