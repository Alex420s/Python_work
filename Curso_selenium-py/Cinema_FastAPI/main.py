from fastapi import FastAPI
from fastapi.responses import JSONResponse
import json
from scraper import scrape_cinepolis  # Importar la función de scraping

app = FastAPI()

def load_peliculas():
    # Cargar los datos del archivo JSON
    with open("peliculas_guardadas.json", "r", encoding="utf-8") as f:
        return json.load(f)

@app.get("/peliculas")
async def get_peliculas():
    # Ejecutar el scraping para actualizar los datos
    scrape_cinepolis()
    
    # Cargar los datos actualizados
    peliculas_data = load_peliculas()
    
    # Estructura de respuesta personalizada
    response = {
        "mensaje": "Cartelera Cinepolis Perisur - Funciones para el día de hoy",
        "peliculas": peliculas_data
    }
    
    return JSONResponse(content=response)
