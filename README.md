# Reto Resuelve

Solución para el reto resuelve, se puede iniciar con docker-compose o con conda y la versión 3.8 de python

## Requerimientos

Python 3.8

## Descargar el proyecto
```python
#Clonar el repositorio.
$ git clone git@github.com:dagopoot/reto_resuelve.git resuelve

#Nos posicionamos en la carpeta creada
$ cd resuelve
```

## Iniciar con docker-compose

En caso de que no tengamos instalado docker-compose, instalarlo con ayuda del manual oficial

https://docs.docker.com/compose/install/

```python
#iniciamos el contenedor
$ sudo docker-compose up
```

## Iniciar con Conda

En caso de que no tengamos instalado Conda, instalarlo con ayuda del manual oficial

https://docs.conda.io/en/latest/miniconda.html

```python
#creamos un nuevo ambiente con python 3.8
$ conda create --name resuelve python=3.8

#activamos el ambiente recién creado
$ conda activate resuelve

#instalamos los paquetes requeridos por el proyecto
$ pip install -r ./resuelve/requirements.txt

#iniciamos el servidor
$ python ./resuelve/manage.py runserver
```

## Unit test

### Con docker

```python
#con el proyecto iniciado, ejecute
$ docker ps

#copie el valor del CONTAINER ID correspondiente a la imagen a continuación
CONTAINER ID     IMAGE                       COMMAND
a1ads6dt34ad     backend_backend_django      "python /code/resuelve"

#Sustituya el valor en lugar de <container-id>, este comando ejecutara las pruebas
$ docker exec -it <container-id> python /code/manage.py test reto
```

### Con conda

```python
#asegúrese que esté activado el ambiente
$ conda activate resuelve

#ejecute para iniciar las pruebas
$ python ./resuelve/manage.py test reto
```

# Endpoints

## Calcular salarios del equipo Resuelve FC

El primer endpoint calcula los salarios para el equipo Resuelve FC, 

POST http://localhost:8000/api/reto/calculate_salaries

recibe como parámetros un objeto similar al siguiente

```python
[
    {  
        "nombre":"Juan Perez",
        "nivel":"C",
        "goles":10,
        "sueldo":50000,
        "bono":25000,
        "sueldo_completo":null,
        "equipo":"rojo"
    },
    {  
        "nombre":"EL Cuauh",
        "nivel":"Cuauh",
        "goles":30,
        "sueldo":100000,
        "bono":30000,
        "sueldo_completo":null,
        "equipo":"azul"
    },
    {  
        "nombre":"Cosme Fulanito",
        "nivel":"A",
        "goles":7,
        "sueldo":20000,
        "bono":10000,
        "sueldo_completo":null,
        "equipo":"azul"
    },
    {  
        "nombre":"El Rulo",
        "nivel":"B",
        "goles":9,
        "sueldo":30000,
        "bono":15000,
        "sueldo_completo":null,
        "equipo":"rojo"
    }
]
```

devuelve el arreglo agregando el número de goles que cada jugador tiene como meta y su sueldo completo

```python
[
    {
        "nombre": "Juan Perez",
        "goles_minimos": 15,
        "goles": 10,
        "sueldo": "50000.00",
        "bono": "25000.00",
        "sueldo_completo": "67833.33",
        "equipo": "rojo"
    },
    {
        "nombre": "EL Cuauh",
        "goles_minimos": 20,
        "goles": 30,
        "sueldo": "100000.00",
        "bono": "30000.00",
        "sueldo_completo": "130000.00",
        "equipo": "azul"
    },
    {
        "nombre": "Cosme Fulanito",
        "goles_minimos": 5,
        "goles": 7,
        "sueldo": "20000.00",
        "bono": "10000.00",
        "sueldo_completo": "30000.00",
        "equipo": "azul"
    },
    {
        "nombre": "El Rulo",
        "goles_minimos": 10,
        "goles": 9,
        "sueldo": "30000.00",
        "bono": "15000.00",
        "sueldo_completo": "42450.00",
        "equipo": "rojo"
    }
]
```

## Calcular salarios para otros equipos

El segundo endpoint calcula los salarios para otros equipos, debe proporcionar la tabla de objetivos de goles para cada uno de los equipos

POST http://localhost:8000/api/reto/calculate_salaries_bonus

recibe como parámetros un objeto similar al siguiente

```python
{
    "jugadores": [
        {  
            "nombre":"Juan Perez",
            "nivel":"C",
            "goles":5,
            "sueldo":50000,
            "bono":25000,
            "sueldo_completo":null,
            "equipo":"rojo"
        },
        {  
            "nombre":"EL Cuauh",
            "nivel":"Cuauh",
            "goles":30,
            "sueldo":100000,
            "bono":30000,
            "sueldo_completo":null,
            "equipo":"azul"
        },
        {  
            "nombre":"Cosme Fulanito",
            "nivel":"A",
            "goles":3,
            "sueldo":20000,
            "bono":10000,
            "sueldo_completo":null,
            "equipo":"azul"
        },
        {  
            "nombre":"El Rulo",
            "nivel":"B",
            "goles":4,
            "sueldo":30000,
            "bono":15000,
            "sueldo_completo":null,
            "equipo":"rojo"
        }
    ],
    "niveles": [
        {
            "equipo": "rojo",
            "A": 5,
            "B": 12,
            "C": 15,
            "Cuauh": 20
        },
        {
            "equipo": "azul",
            "A": 6,
            "B": 10,
            "C": 15,
            "Cuauh": 60
        }
    ]
}
```

devuelve el arreglo agregando el número de goles que cada jugador tiene como meta y su sueldo completo

```python
[
    {
        "nombre": "Juan Perez",
        "goles_minimos": 15,
        "goles": 5,
        "sueldo": "50000.00",
        "bono": "25000.00",
        "sueldo_completo": "58333.33",
        "equipo": "rojo"
    },
    {
        "nombre": "EL Cuauh",
        "goles_minimos": 60,
        "goles": 30,
        "sueldo": "100000.00",
        "bono": "30000.00",
        "sueldo_completo": "115000.00",
        "equipo": "azul"
    },
    {
        "nombre": "Cosme Fulanito",
        "goles_minimos": 6,
        "goles": 3,
        "sueldo": "20000.00",
        "bono": "10000.00",
        "sueldo_completo": "25000.00",
        "equipo": "azul"
    },
    {
        "nombre": "El Rulo",
        "goles_minimos": 12,
        "goles": 4,
        "sueldo": "30000.00",
        "bono": "15000.00",
        "sueldo_completo": "35000.00",
        "equipo": "rojo"
    }
]
```
