REQUEST_VALID_DATA = [
    {
        "nombre": "Juan Perez",
        "nivel": "C",
        "goles": 10,
        "sueldo": 50000,
        "bono": 25000,
        "sueldo_completo": None,
        "equipo": "rojo"
    },
    {
        "nombre": "EL Cuauh",
        "nivel": "Cuauh",
        "goles": 30,
        "sueldo": 100000,
        "bono": 30000,
        "sueldo_completo": None,
        "equipo": "azul"
    },
    {
        "nombre": "Cosme Fulanito",
        "nivel": "A",
        "goles": 7,
        "sueldo": 20000,
        "bono": 10000,
        "sueldo_completo": None,
        "equipo": "azul"
    },
    {
        "nombre": "El Rulo",
        "nivel": "B",
        "goles": 9,
        "sueldo": 30000,
        "bono": 15000,
        "sueldo_completo": None,
        "equipo": "rojo"
    }
]

REQUEST_INVALID_DATA = [
    {
        "nombre": "Juan Perez",
        "nivel": "C",
        "goles": "x",
        "sueldo": "x",
        "bono": "x",
        "sueldo_completo": "x",
        "equipo": "rojo"
    }
]

REQUEST_INVALID_LEVEL = [
    {
        "nombre": "Juan Perez",
        "nivel": "H",
        "goles": 10,
        "sueldo": 50000,
        "bono": 25000,
        "sueldo_completo": None,
        "equipo": "rojo"
    }
]
