# MiniCore - Sistema de Cálculo de Comisiones

MiniCore es una aplicación web completa que permite calcular comisiones para vendedores basándose en sus ventas totales dentro de un rango de fechas específico. La aplicación utiliza un sistema de comisiones progresivas y proporciona una interfaz intuitiva para consultar los resultados.

## Características Principales

- **Cálculo automático de comisiones** basado en reglas progresivas
- **Filtrado por rango de fechas** personalizable
- **Interfaz web moderna** y responsiva
- **API REST** para integración con otros sistemas
- **Datos en tiempo real** con actualizaciones instantáneas

##  Arquitectura

### Backend (FastAPI)
- **Framework**: FastAPI con Python
- **Base de datos**: Datos en memoria (simulación)
- **API REST**: Endpoint `/comision` para cálculos
- **CORS**: Configurado para desarrollo local

### Frontend (Vue.js 3)
- **Framework**: Vue.js 3 con Composition API
- **Interfaz**: SPA (Single Page Application)
- **Estilos**: CSS vanilla con diseño responsivo

## Sistema de Comisiones

El sistema aplica comisiones progresivas basadas en el total de ventas del vendedor:

| Rango de Ventas | Porcentaje de Comisión |
|----------------|----------------------|
| $1000 o más    | 15%                 |
| $800 - $999    | 10%                 |
| $600 - $799    | 8%                  |
| $400 - $599    | 6%                  |
| Menos de $400  | 0%                  |

## Datos de Ejemplo

La aplicación incluye datos de prueba con:

### Vendedores
- Juan (ID: 1)
- Carlos (ID: 2)
- Mateo (ID: 3)
- Ana (ID: 4)

### Ventas (Mayo-Junio 2025)
- Juan: $400 (21/05), $300 (09/06), $500 (24/06)
- Carlos: $600 (29/05), $200 (03/06)
- Mateo: $900 (11/06)
- Ana: $600 (30/06)

## 🔧 Instalación y Configuración

### Requisitos Previos
- Python 3.8+
- Node.js 16+
- npm o yarn

### Instalación del Backend

```bash
# Clonar el repositorio
git clone <url-del-repositorio>
cd minicore

# Crear entorno virtual
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate

# Instalar dependencias
pip install fastapi uvicorn

# Ejecutar el servidor
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Instalación del Frontend

```bash
# Navegar a la carpeta del frontend
cd app/static

# Instalar dependencias (si tienes package.json)
npm install

# Para desarrollo local, el frontend ya está incluido en los archivos estáticos
```

## Uso de la Aplicación

### Interfaz Web

1. **Accede a la aplicación** 
2. **Selecciona el rango de fechas**:
   - Fecha inicio: Selecciona la fecha desde la cual quieres calcular
   - Fecha fin: Selecciona la fecha hasta la cual quieres calcular
3. **Haz clic en "Calcular"** para obtener los resultados
4. **Revisa la tabla de resultados** que muestra:
   - Nombre del vendedor
   - Total de ventas en el período
   - Porcentaje de comisión aplicado
   - Comisión calculada en dinero

### API REST

#### Endpoint: `GET /comision`

**Parámetros de consulta:**
- `fecha_inicio`: Fecha de inicio en formato ISO (YYYY-MM-DD)
- `fecha_fin`: Fecha de fin en formato ISO (YYYY-MM-DD)

**Ejemplo de solicitud:**
```bash
curl "http://localhost:8000/comision?fecha_inicio=2025-06-01&fecha_fin=2025-06-30"
```

**Ejemplo de respuesta:**
```json
{
  "rango": {
    "desde": "2025-06-01",
    "hasta": "2025-06-30"
  },
  "resultado": [
    {
      "usuario": "juan",
      "total_ventas": 800.0,
      "porcentaje_aplicado": 0.10,
      "comision_calculada": 80.0
    },
    {
      "usuario": "carlos",
      "total_ventas": 200.0,
      "porcentaje_aplicado": 0.0,
      "comision_calculada": 0.0
    },
    {
      "usuario": "mateo",
      "total_ventas": 900.0,
      "porcentaje_aplicado": 0.10,
      "comision_calculada": 90.0
    },
    {
      "usuario": "ana",
      "total_ventas": 600.0,
      "porcentaje_aplicado": 0.08,
      "comision_calculada": 48.0
    }
  ]
}
```

## Estructura del Proyecto

```
minicore/
├── main.py                 # Servidor FastAPI principal
├── app/
│   ├── models.py          # Datos de usuarios y ventas
│   └── static/            # Frontend Vue.js
│       ├── index.html     # Aplicación Vue.js
│       └── ...            # Otros archivos estáticos
├── requirements.txt       # Dependencias de Python
└── README.md             # Este archivo
```

## 🌐 Deployment

La aplicación está deployada y disponible en **Render**:


### Configuración en Render

1. **Servicio**: Web Service
2. **Runtime**: Python 3
3. **Build Command**: `pip install -r requirements.txt`
4. **Auto-Deploy**: Habilitado desde el repositorio principal

##  Funcionalidades Detalladas

### Cálculo de Comisiones
- Agrupa las ventas por vendedor en el rango de fechas seleccionado
- Aplica las reglas de comisión progresivas automáticamente
- Redondea los resultados a 2 decimales para precisión monetaria

### Validación de Datos
- Verifica que ambas fechas estén seleccionadas
- Maneja errores de conexión con el servidor
- Muestra mensajes de error informativos al usuario

### Interfaz Responsiva
- Diseño adaptable a diferentes tamaños de pantalla
- Tabla con formato claro y fácil de leer
- Formulario intuitivo con validación en tiempo real

## Casos de Uso

### Ejemplo 1: Consulta Mensual
**Fechas**: 01/06/2025 - 30/06/2025
**Resultado esperado**: Juan $80, Carlos $0, Mateo $90, Ana $48

### Ejemplo 2: Consulta Bimestral  
**Fechas**: 01/05/2025 - 30/06/2025
**Resultado esperado**: Comisiones completas de todo el período

### Ejemplo 3: Consulta Específica
**Fechas**: 10/06/2025 - 25/06/2025
**Resultado esperado**: Solo ventas en ese rango específico

## Notas Técnicas

- Los datos están almacenados en memoria para fines de demostración
- Las fechas se manejan en formato ISO para compatibilidad
- El sistema es extensible para agregar más vendedores y reglas de comisión
- La API está preparada para integración con sistemas externos


**MiniCore** - Sistema de Cálculo de Comisiones | Desarrollado usando FastAPI y Vue.js
