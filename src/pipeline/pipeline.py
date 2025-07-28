import os
import sys

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(directorio_raiz)

from utils.helpers import conf_logging
from data.extract import carga_raw
from data.conexion import conexion_db

logger = conf_logging("Pipeline_log")

if __name__ == "__main__":

    logger.info("Inicio del proceso de extracción del csv.")
    try:
        df = carga_raw("data_jobs")
        logger.info("Archivo cargado correctamente.")
    except Exception as e:
        logger.error(f"Error al cargar el archivo: {e}")
        sys.exit(1)

# CONEXION BASE DE DATOS

    try:
        conexion_db()
    except Exception as e:
        logger.error(f"Error en la conexión a la base de datos: {e}")
        sys.exit(1)
    else:
        logger.info("Proceso de conexión a la base de datos finalizado correctamente.")