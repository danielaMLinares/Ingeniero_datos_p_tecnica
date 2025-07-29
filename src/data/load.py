import pandas as pd
import os
import sys
import io


directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(directorio_raiz)

from utils.helpers import conf_logging
from data.conexion import conexion_db, conexion_db_psycopg2

logger=conf_logging("load_log")

class carga_data(object):
    """
    La clase 'carga_data' se encarga de generar la tabla dinamicamente, organizar para determinar el tipo de dato y normalizar los nombres.
    """
    def __init__(self, nombre_archivo: str):
        self.conn=conexion_db()
        self.conn2=conexion_db_psycopg2()

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
            return "TEXT"
        else:
            return "TEXT"

    def crear_tabla_dinamica(self,df, tabla):
        cursor = self.conn.cursor()
        columnas = []
        
        try:

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
            logger.info(f"Se crea la tabla: {tabla} con esta estrutura: {sql}")
        except Exception as e:
            logger.error(f"Error al crear la tabla {tabla}: {e}")
            raise



    def bulk_insert_tabla_raw(self,df_data, tabla):
        cursor = self.conn2.cursor()
        self.crear_tabla_dinamica(df_data, tabla)

        df_data = df_data.replace({r'\t': ' ', r'\n': ' ', r'\r': ' '}, regex=True)
        df_data = df_data.applymap(lambda x: str(x).replace('"', '""') if isinstance(x, str) else x)

        output = io.StringIO() #moviendome en la memoria ram...
        df_data.to_csv(output, sep='\t', header=False, index=False, na_rep='\\N')
        output.seek(0)

        try:
            cursor.copy_from(output, tabla, sep='\t', null='\\N')
            self.conn2.commit()
            logger.info(f"Inserción de tabla: {tabla} exitosa")
        except Exception as e:
            logger.error(f"Error en la carga de datos: {e}")
            self.conn2.rollback()
            raise
        finally:
            cursor.close()
