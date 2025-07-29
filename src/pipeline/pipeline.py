import os
import sys

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(directorio_raiz)

from utils.helpers import conf_logging
from data.extract import carga_raw
from data.conexion import conexion_db
from data.load import carga_data

logger = conf_logging("Pipeline_log")


def main():
    logger.info("Inicio del proceso de extracción del csv.")
    try:
        df = carga_raw("data_jobs")
        logger.info("Archivo cargado correctamente.")
    except Exception as e:
        logger.error(f"Error al cargar el archivo: {e}")

    try:
        conn = conexion_db()
    except Exception as e:
        logger.error(f"Error en la conexión a la base de datos: {e}")
    else:
        logger.info("Proceso de conexión a la base de datos finalizado correctamente.")

    try:
        tabla = 'data_jobs_raw'
        carga_data(tabla).bulk_insert_tabla_raw(df, tabla)
        logger.info(f"Datos cargados correctamente en la tabla {tabla}.")
    except Exception as e:
        logger.error(f"Error al insertar los datos: {e}")

# if __name__ == "__main__":

#     logger.info("Inicio del proceso de extracción del csv.")
#     try:
#         df = carga_raw("data_jobs")
#         logger.info("Archivo cargado correctamente.")
#     except Exception as e:
#         logger.error(f"Error al cargar el archivo: {e}")
#         sys.exit(1)

# # CONEXION BASE DE DATOS

#     try:
#         conn=conexion_db()
#     except Exception as e:
#         logger.error(f"Error en la conexión a la base de datos: {e}")
#         sys.exit(1)
#     else:
#         logger.info("Proceso de conexión a la base de datos finalizado correctamente.")


# # CREACION DE TABLA DINAMICA
#     # Ejemplo de uso
#     tabla = 'data_jobs_raw'
    
#     carga_data(tabla).bulk_insert_tabla_raw(df, tabla)
#     print(f"Datos cargados correctamente en la tabla {tabla}")