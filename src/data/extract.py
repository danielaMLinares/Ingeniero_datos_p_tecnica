import pandas as pd
import os
import sys

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(directorio_raiz)

from utils.helpers import conf_logging

logger=conf_logging("extract_log")


def carga_raw(nombre_archivo:str):
    """
    La función 'carga_raw' carga un archivo CSV desde el directorio 'data/raw.

    :param nombre_archivo: Nombre del archivo CSV a cargar (sin la extensión .csv). 
    """

    try:
        df_data=pd.read_csv(f'data/raw/{nombre_archivo}.csv', sep=',',low_memory=False)
    except Exception as e:
        logger.error(f"Error al cargar el archivo: {e}")
        raise
    return df_data


# if __name__ == "__main__":
#     try:
#         df = carga_raw("data_jobs")
#         logger.info("Archivo cargado correctamente.")
#     except Exception as e:
#         logger.error(f"Error al cargar el archivo: {e}")
#         sys.exit(1)