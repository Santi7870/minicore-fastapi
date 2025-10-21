from fastapi import FastAPI, Query, Request
from datetime import datetime
from typing import Dict
from app.models import usuarios, ventas
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

app = FastAPI()

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Reglas de comisión
REGLAS_COMISION = [
    (1000, 1.15),
    (800, 0.10),
    (600, 0.08),
    (400, 0.06),
]

def obtener_porcentaje_comision(total: float) -> float:
    for limite, porcentaje in REGLAS_COMISION:
        if total >= limite:
            return porcentaje
    return 0.0


@app.get("/comision")
def calcular_comisiones_por_vendedor(
    fecha_inicio: datetime = Query(...),
    fecha_fin: datetime = Query(...)
):
    resumen: Dict[int, Dict] = {}

    for venta in ventas:
        if fecha_inicio <= venta["fecha"] <= fecha_fin:
            usuario_id = venta["usuario_id"]
            resumen.setdefault(usuario_id, {"total_ventas": 0.0})
            resumen[usuario_id]["total_ventas"] += venta["monto"]

    resultado = []
    for usuario in usuarios:
        uid = usuario["id"]
        nombre = usuario["nombre"]
        total = resumen.get(uid, {}).get("total_ventas", 0.0)
        porcentaje = obtener_porcentaje_comision(total)
        comision = round(total * porcentaje, 2)

        resultado.append({
            "usuario": nombre,
            "total_ventas": total,
            "porcentaje_aplicado": porcentaje,
            "comision_calculada": comision
        })

    return {
        "rango": {
            "desde": fecha_inicio.date(),
            "hasta": fecha_fin.date()
        },
        "resultado": resultado
    }


app.mount("/", StaticFiles(directory="app/static", html=True), name="static")


@app.get("/{full_path:path}")
async def serve_vue_app(request: Request):
    return FileResponse(os.path.join("app", "static", "index.html"))
