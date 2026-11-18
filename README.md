# ecommerce-api

REST API desarrollado con FastAPI para un E-commerce.

## Requerimientos

[Python 3.11+](https://www.python.org/)

## Comandos

```bash
# Crear entorno virtual (venv)
python -m venv <nombre del entorno>

# Ingresar al entorno virtual
.\venv\Scripts\activate

# Instalar FastAPI
pip install "fastapi[standard]"

# Crear requirements (parecido a package.json)
pip freeze > requirements.txt

# Inicializar servidor FastAPI
uvicorn src.app:app --host=127.0.0.1 --port=8000 --reload=True
```

## Clonar y ejecutar repositorio

```bash
# Clonar repositorio
git clone https://github.com/itsronalds/fastapi-ecommerce.git

# Entran en el repositorio
cd fastapi-ecommerce

# Crear entorno virtual (venv)
python -m venv venv

# Ingresar al entorno virtual
.\venv\Scripts\activate

# Instalar dependencias dentro del venv
pip install -r requirements.txt

# Ejeuctar el proyecto
py main.py
```

