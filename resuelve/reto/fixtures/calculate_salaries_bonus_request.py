REQUEST_VALID_DATA = {
    "jugadores": [
        {
            "nombre": "Juan Perez",
            "nivel": "C",
            "goles": 5,
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
            "goles": 3,
            "sueldo": 20000,
            "bono": 10000,
            "sueldo_completo": None,
            "equipo": "azul"
        },
        {
            "nombre": "El Rulo",
            "nivel": "B",
            "goles": 4,
            "sueldo": 30000,
            "bono": 15000,
            "sueldo_completo": None,
            "equipo": "rojo"
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

REQUEST_EMPTY_PLAYERS = {"jugadores": [], "niveles": []}

REQUEST_EMPTY_LEVELS = {
    "jugadores": [
        {
            "nombre": "Juan Perez",
            "nivel": "C",
            "goles": 5,
            "sueldo": 50000,
            "bono": 25000,
            "sueldo_completo": None,
            "equipo": "rojo"
        }
    ], "niveles": []}

REQUEST_TEAM_NOT_PROVIDED = {
    "jugadores": [
        {
            "nombre": "Juan Perez",
            "nivel": "C",
            "goles": 5,
            "sueldo": 50000,
            "bono": 25000,
            "sueldo_completo": None,
            "equipo": "verde"
        }
    ], "niveles": [
        {
            "equipo": "rojo",
            "A": 5,
            "B": 12,
            "C": 15,
            "Cuauh": 20
        }
    ]
}

REQUEST_PLAYER_INFO_NOT_PROVIDED = {
    "jugadores": [
        {
        }
    ], "niveles": []}