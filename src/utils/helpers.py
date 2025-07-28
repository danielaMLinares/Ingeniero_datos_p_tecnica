import logging
import os

def conf_logging (log_archivo:str) ->logging.Logger:#conf_logging (log_archivo):
    """
    La función 'conf_logging' configura el registro de logs para la trasabilida del proceso en un archivo y
    imprimirlos en la consola.

    :param log_archivo: Es la ruta del archivo donde se guardarán los mensajes de log.

    :return: Un objeto logger que está configurado para registrar
    mensajes en un archivo 'log_archivo' y también en la consola.
    
    """
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..','logs'))

    logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(os.path.join(base_dir,log_archivo), mode='a',encoding="utf-8"),  # Guardar log en archivo
        logging.StreamHandler(),  # También quiero imprimir log en la consola
    ],
    )
    logger = logging.getLogger()
    return logger