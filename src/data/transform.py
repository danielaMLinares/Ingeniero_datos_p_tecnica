import pandas as pd
import os
import sys

directorio_raiz = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(directorio_raiz)

from utils.helpers import conf_logging

logger = conf_logging("transform_log")

logger.info("Inicio del proceso_2")