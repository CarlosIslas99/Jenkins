from fastapi import FastAPI, HTTPException, Path
from typing import Dict, List

app = FastAPI()

# Datos de las carreras, materias y créditos
carreras = {
    "Ingeniería en Gestión Empresarial": {
        "Contabilidad Financiera": 6,
        "Administración de Operaciones": 5,
        "Mercadotecnia": 4,
        "Finanzas": 4,
        "Recursos Humanos": 4,
        "Emprendimiento": 3,
        "Ética Profesional": 2,
        "Proyecto Integrador": 10
    },
    "Ingeniería Electromecánica": {
        "Circuitos Eléctricos": 7,
        "Máquinas Eléctricas": 6,
        "Electrónica": 5,
        "Mecánica": 5,
        "Termodinámica": 4,
        "Control Automático": 4,
        "Materiales de Ingeniería": 3,
        "Proyecto Integrador": 10
    },
    "Ingeniería en Electrónica": {
        "Circuitos Eléctricos": 7,
        "Electrónica Digital": 6,
        "Telecomunicaciones": 5,
        "Microcontroladores": 5,
        "Señales y Sistemas": 4,
        "Control Automático": 4,
        "Diseño Electrónico": 3,
        "Proyecto Integrador": 10
    },
    "Ingeniería en Mecatrónica": {
        "Mecánica": 7,
        "Electrónica": 6,
        "Programación de Computadoras": 5,
        "Control Automático": 5,
        "Robótica": 4,
        "Mecatrónica": 4,
        "Diseño Mecánico": 3,
        "Proyecto Integrador": 10
    },
    "Ingeniería en Sistemas Computacionales": {
        "Programación de Computadoras": 8,
        "Algoritmos y Estructuras de Datos": 6,
        "Bases de Datos": 5,
        "Redes de Computadoras": 4,
        "Sistemas Operativos": 4,
        "Inteligencia Artificial": 3,
        "Ética Profesional": 2,
        "Proyecto Integrador": 10
    },
    "Ingeniería en Tecnologías de la Información y Comunicación": {
        "Redes de Computadoras": 7,
        "Telecomunicaciones": 6,
        "Seguridad Informática": 5,
        "Administración de Redes": 5,
        "Desarrollo Web": 4,
        "Multimedia": 4,
        "Bases de Datos": 3,
        "Proyecto Integrador": 10
    },
    "Ingeniería Industrial": {
        "Procesos de Manufactura": 7,
        "Planificación y Control de la Producción": 6,
        "Diseño de Producto": 5,
        "Ingeniería de Calidad": 5,
        "Ergonomía": 4,
        "Investigación de Operaciones": 4,
        "Logística y Distribución": 3,
        "Proyecto Integrador": 10
    },
    "Ingeniería Química": {
        "Química General": 7,
        "Química Orgánica": 6,
        "Química Inorgánica": 5,
        "Termodinámica Química": 5,
        "Fisicoquímica": 4,
        "Química Analítica": 4,
        "Operaciones Unitarias": 3,
        "Proyecto Integrador": 10
    },
    "Ingeniería Bioquímica": {
        "Bioquímica": 7,
        "Microbiología": 6,
        "Biotecnología": 5,
        "Química Orgánica": 5,
        "Biología Molecular": 4,
        "Genética": 4,
        "Fisiología Vegetal": 3,
        "Proyecto Integrador": 10
    }
}

# Ruta para obtener la lista de carreras
@app.get("/carreras", response_model=List[str])
def obtener_carreras():
    return list(carreras.keys())

# Ruta para obtener las materias de una carrera
@app.get("/carreras/{nombre_carrera}", response_model=Dict[str, int])
def obtener_materias(nombre_carrera: str = Path(..., title="Nombre de la carrera")):
    if nombre_carrera not in carreras:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    return carreras[nombre_carrera]

# Ruta para obtener los créditos de una materia de una carrera
@app.get("/carreras/{nombre_carrera}/{nombre_materia}", response_model=int)
def obtener_creditos(nombre_carrera: str = Path(..., title="Nombre de la carrera"), nombre_materia: str = Path(..., title="Nombre de la materia")):
    if nombre_carrera not in carreras:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    if nombre_materia not in carreras[nombre_carrera]:
        raise HTTPException(status_code=404, detail="Materia no encontrada")
    return carreras[nombre_carrera][nombre_materia]

# Ruta para crear una nueva carrera
@app.post("/carreras", response_model=str)
def crear_carrera(nueva_carrera: Dict[str, Dict[str, int]]):
    nombre_carrera = list(nueva_carrera.keys())[0]
    if nombre_carrera in carreras:
        raise HTTPException(status_code=400, detail="La carrera ya existe")
    carreras.update(nueva_carrera)
    return f"Carrera '{nombre_carrera}' creada exitosamente"

# Ruta para actualizar una carrera existente
@app.put("/carreras/{nombre_carrera}", response_model=str)
def actualizar_carrera(nombre_carrera: str, datos_actualizados: Dict[str, int]):
    if nombre_carrera not in carreras:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    carreras[nombre_carrera].update(datos_actualizados)
    return f"Datos de la carrera '{nombre_carrera}' actualizados exitosamente"

# Ruta para eliminar una carrera
@app.delete("/carreras/{nombre_carrera}", response_model=str)
def eliminar_carrera(nombre_carrera: str):
    if nombre_carrera not in carreras:
        raise HTTPException(status_code=404, detail="Carrera no encontrada")
    del carreras[nombre_carrera]
    return f"Carrera '{nombre_carrera}' eliminada exitosamente"


# Ruta principal
@app.get("/")
def read_root():
    return {"mensaje": "Bienvenido a la API de Carreras Universitarias"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
