# Job Listings Normalization Project

Este proyecto consiste en la normalización y modelado de datos de vacantes de empleo a partir de un archivo CSV. El objetivo es crear un modelo relacional normalizado (3NF) e implementar un pipeline para extraer, transformar y cargar la información a una base de datos PostgreSQL.

---

## Estructura del Proyecto
.
├── data/
│ └── raw/
│ └── data_jobs.csv # Archivo original debera agregarse en esta carpeta
├── docker/
│ └── docker-compose.yml # Contenedor para PostgreSQL
├── logs
├── notebook
├── src/
│ ├── extract.py # Código para leer y limpiar el CSV
│ ├── transform.py # Normalización y relaciones
│ ├── load.py # Inserción a PostgreSQL
│ └── config.py # Parámetros de conexión
├── tests/
│ └── test_transform.py # Validaciones con pytest
├── pyproject.toml # Dependencias
└── README.md

---

## Tecnologías Usadas

- Python
- Pandas
- PostgreSQL
- Poetry
- Docker & Docker Compose
- Git + GitHub

---

## Cómo ejecutar el proyecto

### 1. Clonar el repositorio

```bash
git https://github.com/danielaMLinares/Ingeniero_datos_p_tecnica.git
cd Ingeniero_datos_p_tecnica
```

## poetry 
### insatalación de poetry - windows
```bash
(Invoke-WebRequest -Uri https://install.python-poetry.org -UseBasicParsing).Content | python -
```
### instalación de poetry - linux
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

### instala dependencias
```bash
poetry install
```
### entorno 
```bash
poetry shell
```
### levatamiento de docker
```bash
docker-compose up -d
```

## ejecución
 ```bash
python main.py
```


Esto hará lo siguiente:

Cargar el archivo data_jobs.csv desde la carpeta data/raw/.
Insertar los datos en las tablas correspondientes en la base de datos PostgreSQL alojada en Docker. (raw)


