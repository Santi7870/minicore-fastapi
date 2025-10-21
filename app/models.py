from datetime import datetime

usuarios = [
    {"id": 1, "nombre": "juan"},
    {"id": 2, "nombre": "carlos"},
    {"id": 3, "nombre": "mateo"},
    {"id": 4, "nombre": "ana"},
]

ventas = [
    {"usuario_id": 1, "fecha": datetime(2025, 5, 21), "monto": 400},  # juan
    {"usuario_id": 2, "fecha": datetime(2025, 5, 29), "monto": 600},  # carlos
    {"usuario_id": 2, "fecha": datetime(2025, 6, 3),  "monto": 200},  # carlos
    {"usuario_id": 1, "fecha": datetime(2025, 6, 9),  "monto": 300},  # juan
    {"usuario_id": 3, "fecha": datetime(2025, 6, 11), "monto": 900},  # mateo
    {"usuario_id": 1, "fecha": datetime(2025, 6, 24), "monto": 500},  # juan
    {"usuario_id": 4, "fecha": datetime(2025, 6, 30), "monto": 600},  # ana
]
