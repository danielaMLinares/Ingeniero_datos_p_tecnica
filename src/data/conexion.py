from dotenv import load_dotenv
import os
import pyodbc
import sys
import psycopg2

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(directorio_raiz)

from utils.helpers import conf_logging

logger=conf_logging("extract_log")
load_dotenv()

def conexion_db() -> pyodbc.Connection:
    """
    La función 'conexion_db' establece la conexión a la base de datos utilizando las variables de entorno, esta conexion la uso normalmente para consultas complejas.

    :return conn: Un objeto de conexión a la base de datos.
    """
    try: 
        conn=pyodbc.connect( 
            f"DRIVER={os.getenv('BD_DRIVER')};"
            f"SERVER={os.getenv('BD_HOST')};"
            f"DATABASE={os.getenv('BD_NAME')};"
            f"PORT={os.getenv('BD_PORT')};"
            f"UID={os.getenv('BD_USER')};"
            f"PWD={os.getenv('BD_PASSWORD')};" 
        )
        logger.info("Conexión a la base de datos establecida correctamente.")
    except Exception as e:
        logger.error(f"Error al conectar a la base de datos: {e}")
        raise
    return conn


def conexion_db_psycopg2() -> psycopg2.extensions.connection:
    """
    La función 'conexion_db_psycopg2' establece la conexión a la base de datos utilizando las variables de entorno, esta conexion la uso normalmente para cargar en bulk suele ser mas rapido.

    :return conn: Un objeto de conexión a la base de datos.
    """
    try:
        conn2 = psycopg2.connect(
            host=f"{os.getenv('BD_HOST')}",
            database=f"{os.getenv('BD_NAME')}",
            user=f"{os.getenv('BD_USER')}",
            password=f"{os.getenv('BD_PASSWORD')}",
            port=os.getenv('BD_PORT')
        )
        logger.info("Conexión a la base de datos exitosa.")
    except psycopg2.Error as e:
        logger.error(f"Error al conectar con la base de datos: {e}")
        raise
    return conn2

