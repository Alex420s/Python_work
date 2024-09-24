from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json

def scrape_cinepolis():
    # Configurar Selenium para usar Chrome 
    chrome_options = Options()
    # Para ejecutar en modo sin interfaz gráfica
    # chrome_options.add_argument("--headless")
    # Path al driver de Chrome 
    driver_path = "/Users/alex420s/Downloads/chromedriver-mac-arm64/chromedriver"
    service = Service(driver_path)
    # Inicializar el navegador
    driver = webdriver.Chrome(service=service, options=chrome_options)

    try:
        # Ir a la URL
        perisur = 'https://cinepolis.com/mx?cinema=cinepolis-perisur-cdmx'
        driver.get(perisur)
        driver.implicitly_wait(20)  # Esperar a que la página cargue

        
        wait = WebDriverWait(driver, 20)  # Espera hasta 10 segundos
        
        # Esperar y volver a buscar el botón hasta que esté disponible
        button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".mf-locations-filter-actions button[type='button']")))
        
        # Usar JavaScript para desplazarse hasta el elemento
        driver.execute_script("arguments[0].scrollIntoView();", button)

        # Hacer clic mediante JavaScript
        driver.execute_script("arguments[0].click();", button)
        
        # Volver a buscar los elementos después del clic
        pelis = wait.until(EC.presence_of_all_elements_located((By.XPATH, '//main/section[3]/div/child::*')))

        # Usar una lambda function para obtener solo el texto de cada WebElement
        pelis_texto = list(map(lambda pelicula: pelicula.text, pelis))

        # Lista para almacenar las películas
        peliculas_guardadas = []

        for pelicula in pelis_texto:
            peliculas_guardadas.append(pelicula)  # Agrega cada película a la lista

        # Procesar la información
        cartelera = []

        for pelicula_info in peliculas_guardadas:
            if pelicula_info.strip():  # Ignorar cadenas vacías
                lineas = pelicula_info.strip().split('\n')
                
                if "Ver detalle" in lineas[0]:
                    # Extraer información
                    titulo = lineas[1].strip()
                    clasificacion = lineas[2].strip()
                    duracion = lineas[3].strip()
                    idioma = lineas[5].strip()  # Ajustar según tu formato
                    cine = lineas[6].strip()
                    horarios = []

                    # Extraer horarios
                    for horario in lineas[7:]:
                        if horario.strip():  # Ignorar líneas vacías
                            horarios.append(horario.strip())

                    # Crear un diccionario para la película
                    pelicula_dict = {
                        "titulo": titulo,
                        "clasificacion": clasificacion,
                        "duracion": duracion,
                        "idioma": idioma,
                        "cine": cine,
                        "horarios": horarios
                    }

                    # Añadir el diccionario a la lista de películas
                    cartelera.append(pelicula_dict)

        # Convertir la lista de diccionarios a JSON
        peliculas_json = json.dumps(cartelera, indent=4, ensure_ascii=False)

        # Guardar el JSON en un archivo
        with open('peliculas_guardadas.json', 'w', encoding='utf-8') as f:
            f.write(peliculas_json)

    except Exception as e:
        print(f"Error durante el scraping: {e}")

    finally:
        # Cerrar el navegador
        driver.quit()
