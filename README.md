# Reto Next-e


###### Crear una mini-aplicación que recopile y almacene datos climáticos.


**1. Función Lambda en AWS que recopile datos climáticos de Open Weathermap API cada 6 horas y los
almacene en DynamoDB.**

**2. Un script que utilizando Pandas obtenga el promedio de temperatura dentro de los periodos
seleccionados**

**3.- (EXTRA) Agregar una interfaz para acceder fácilmente al script que obtiene el promedio de temperatura**


# Instructions for first-run

###### if you don't have **POETRY**, install it here https://python-poetry.org/docs/
###### if you don't have **PYTHON 3**, install it here https://www.python.org/downloads/
###### if you don't know how to set **ENVIRONMENT VARIABLES**, follow this tutorial for [Windows 10](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0)

```bash
# create a virtual environment & install dependencies
poetry install

# manually set the following environment variables
# remember to replace with your own
DYNAMODB_TABLE = openweather_insights_next_e
AWS_DEFAULT_REGION = us-east-2
LONGITUDE = -100.31847
APPID = 44d621212314
LATITUDE = 25.6714

# replace python to python3 in bash if 
# executing 'python --version' is not python 3.x.x

# run the program, normally i.e
python src/main.py
```

# Developers

to sync poetry & requirements.txt _(which natively is used in lambda)_ use the follow command
```bash
poetry export -f requirements.txt --output requirements.txt
```
