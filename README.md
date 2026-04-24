# inventario-servidores
# Gestión e Integración de Inventario de Servidores

Este proyecto es una solución desarrollada en **Python** para procesar, limpiar y almacenar un inventario de servidores proveniente de un archivo de texto heredado con formato irregular. El sistema normaliza los datos, los serializa en formato **JSON** y finalmente los persiste en una base de datos relacional **SQLite**.

## Características Principales

* **Limpieza y Normalización de Datos:** Lee archivos de texto con formatos inconsistentes (espacios extra, distintos separadores, mayúsculas/minúsculas mezcladas) y los estandariza.
* **Validación de Datos:** Descarta registros erróneos (IPs inválidas, falta de datos obligatorios) y genera un informe de validación.
* **Arquitectura Modular:** Dividido en submódulos independientes (`inventario`, `servers_json`, `sqlite_servers`) para facilitar su mantenimiento y escalabilidad.
* **Persistencia en JSON:** Generación e importación de archivos `.json` para la portabilidad de los datos.
* **Integración con SQLite:** Creación automática de la base de datos y tablas, e inserción de datos utilizando **consultas parametrizadas** para prevenir ataques de *SQL Injection*.
* **Interfaz de Línea de Comandos (CLI):** Un menú interactivo para crear la BDD, poblarla y consultar servidores por su nombre.

## Arquitectura y Flujo de Ejecución

El proyecto está dividido en varios módulos que interactúan entre sí. A continuación se muestra el diagrama de secuencia de la integración de módulos:

<img width="2944" height="1408" alt="Gemini_Generated_Image_24dj1724dj1724dj" src="https://github.com/user-attachments/assets/0cd520c2-cdae-44c0-af99-34f08ffc1196" />


## Estructura de los Archivos

* `inventario.py`: Se encarga de la lectura del fichero `inventario.txt`, normalización y validación de reglas de negocio.
* `servers_json.py`: Actúa como puente para guardar y cargar los datos limpios en formato `lista_servidores.json`.
* `sqlite_servers.py`: Orquesta la base de datos `servidores.db` y proporciona el menú interactivo al usuario.

## Tecnologías y Librerías Utilizadas

* **Python 3.x**
* **Librerías estándar:** `json`, `sqlite3`

## Cómo ejecutar el proyecto

1. Clona este repositorio.
2. Asegúrate de tener Python instalado en tu sistema.
3. Ejecuta el módulo principal de la base de datos:

```bash
python sqlite_servers.py
