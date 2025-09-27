# Análisis de Datos de Ventas y Clientes

## Descripción del proyecto

Este proyecto consiste en una aplicación básica de análisis de datos en Python, que permite limpiar, preparar y analizar información de ventas y clientes. Utiliza pandas para el procesamiento de datos y responde preguntas clave como:
- ¿Cuál es el producto más vendido?
- ¿Cuántos productos se venden por ciudad?
- ¿Cuántos registros cumplen condiciones específicas?

El proyecto incluye funciones para manejar valores nulos, estandarizar texto, eliminar símbolos y realizar operaciones de filtrado, combinación y agrupación.

## Configuración del entorno

1. **Clona el repositorio:**
   ```bash
   git clone <https://github.com/santiruab1/Second_moment_Phyton.git>
   cd Second_moment_Phyton
   ```

2. **Crea y activa un entorno virtual:**
   ```bash
   python -m venv .env
   .env\Scripts\activate.ps1
   ```

3. **Instala las dependencias:**
   ```bash
   pip install pandas
   ```

## Ejecución del script

1. Asegúrate de tener los archivos `data/clientes.csv` y `data/ventas.csv` en la carpeta `data/`.
2. Ejecuta el script principal:
   ```bash
   python analisis.py
   ```
3. Observa en la consola los resultados de los análisis y operaciones realizadas.
