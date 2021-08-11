# Reto Next-e


###### Crear una mini-aplicación que recopile y almacene datos climáticos.


**1. Función Lambda en AWS que recopile datos climáticos de Open Weathermap API cada 6 horas y los
almacene en DynamoDB.**

**2. Un script que utilizando Pandas obtenga el promedio de temperatura dentro de los periodos
seleccionados**

**3.- (EXTRA) Agregar una interfaz online para acceder fácilmente al script que obtiene el promedio de temperatura**


# Instructions for first-run

###### if you don't have **POETRY**, install it [here](https://python-poetry.org/docs/)
###### if you don't have **PYTHON 3**, install it [here](https://www.python.org/downloads/)
###### if you don't know how to set **ENVIRONMENT VARIABLES**, follow this tutorial for [Windows 10](https://docs.oracle.com/en/database/oracle/machine-learning/oml4r/1.5.1/oread/creating-and-modifying-environment-variables-on-windows.html#GUID-DD6F9982-60D5-48F6-8270-A27EC53807D0)

```bash
# create a virtual environment & install dependencies
poetry install

# create a file called .env file or rename the file called sample.env 
# and use sample.env as a sample to set all environment variables 

# replace python to python3 in bash if 
# executing 'python --version' is not python 3.x.x

# run the program, normally i.e
python src/main.py
```

# Developers

### To deploy

###### if you don't have **SERVERLESS**, install it [here](https://www.serverless.com/framework/docs/getting-started/)
###### if you don't have **NODE**, install it [here](https://nodejs.org/es/)
###### if you don't have **NPM**, install it [here](https://nodejs.org/es/download/package-manager/)
###### if you don't have **PYTHON 3.7**, install it [here](https://tecadmin.net/install-python-3-7-on-ubuntu-linuxmint/)

```bash
# make sure you got all plugins installed and python in version 3.7
serverless plugin install -n serverless-python-requirements

# you need to ask access to aws cloud, contact your administrator
sls deploy
```
