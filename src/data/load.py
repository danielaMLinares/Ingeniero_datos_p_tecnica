import pandas as pd
import os
import sys


directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(directorio_raiz)

from utils.helpers import conf_logging
from data.conexion import conexion_db

logger=conf_logging("load_log")

class carga_data(object):
    """
    La clase 'carga_data' se encarga de generar la tabla dinamicamente.
    """
    def __init__(self, nombre_archivo: str):
        self.conn=conexion_db()

    def mapeo_tipo_dato(self,tipos, muestra=None):
        if pd.api.types.is_integer_dtype(tipos):
            return 'INTEGER'
        elif pd.api.types.is_float_dtype(tipos):
            return 'FLOAT'
        elif pd.api.types.is_bool_dtype(tipos):
            return "BOOLEAN"
        elif pd.api.types.is_datetime64_any_dtype(tipos):
            return "TIMESTAMP"
        elif pd.api.types.is_object_dtype(tipos) and isinstance(muestra, list):
            return "TEXT"
        elif pd.api.types.is_object_dtype(tipos) and isinstance(muestra, dict):
            return "JSONB"
        elif pd.api.types.is_string_dtype(tipos):
            return "VARCHAR(255)"
        else:
            return "TEXT"

    def crear_tabla_dinamica(self,df, tabla):
        cursor = self.conn.cursor()
        columnas = []
        
        for col in df.columns:
            tipo_pg = self.mapeo_tipo_dato(df[col].dtype, df[col].dropna().iloc[0] if not df[col].dropna().empty else None)
            col_limpio = col.lower().strip().replace(" ", "_")
            columnas.append(f'"{col_limpio}" {tipo_pg}')
        
        columnas_sql = ", ".join(columnas)
        sql = f"""
            CREATE TABLE IF NOT EXISTS {tabla} (
                {columnas_sql}
            );
        """
        cursor.execute(sql)
        self.conn.commit()


def crear_auxiliar(df_data):
    """
    La función 'crear auxiliar' crea una tabla auxiliar par acargar los datos del csv crudo. 
    """
    try:
        
    except Exception as e:
        logger.error(f"Error al cargar el archivo: {e}")
        raise
    return df_data



