# Proyecto SmartWash
Aplicación web desarrollada con Django.

## Requisitos previos
- Python 3 instalado en el sistema.

## 1. Crear y activar el entorno virtual

En macOS / Linux:
```bash
python3 -m venv venv
source venv/bin/activate

python -m venv venv
.\venv\Scripts\Activate.ps1

pip install -r requirements.txt

python manage.py migrate
python manage.py runserver

Después abre en tu navegador la dirección que muestra la terminal (por lo general http://127.0.0.1:8000/).