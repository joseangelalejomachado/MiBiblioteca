# MiBiblioteca

Práctica de Django de la unidad *Persistencia y ORM* (UT4): proyecto `biblioteca` con la aplicación `catalogo`, modelos `Libro`, `Editorial` y `Autor`, migraciones, operaciones CRUD y consultas con el ORM. Base de datos SQLite.

## Requisitos

- Python 3.12 o superior
- Django 6.1.3 (se instala con `requirements.txt`)

## Instalar

```bash
git clone <url-del-repositorio>
cd MiBiblioteca

python -m venv .venv
# Windows (PowerShell):  .venv\Scripts\Activate.ps1
# Linux / macOS:         source .venv/bin/activate

pip install -r requirements.txt
```

## Migrar

La base de datos `db.sqlite3` no se versiona: se crea al aplicar las migraciones.

```bash
python manage.py migrate
```

Para comprobar el estado de las migraciones:

```bash
python manage.py showmigrations catalogo
```

## Cargar datos de ejemplo

`cargar_libros.py` carga diez libros de ejemplo. Con `REINICIAR = True` (variable al principio del archivo) vacía antes la tabla de libros y reinicia sus IDs; con `False` conserva los existentes.

```bash
python manage.py shell < cargar_libros.py
```

> **Windows:** el operador `<` no está disponible en PowerShell, así que ejecuta estos comandos desde CMD o Git Bash. Antes, define `PYTHONUTF8=1` para que las tildes se guarden bien en la base de datos (`set PYTHONUTF8=1` en CMD, `export PYTHONUTF8=1` en Git Bash). En PowerShell: `$env:PYTHONUTF8 = "1"` y después `cmd /c "python manage.py shell < cargar_libros.py"`.

## Ejecutar

```bash
python manage.py runserver
```

| Ruta           | Contenido               |
| -------------- | ----------------------- |
| `/`            | Listado de libros       |
| `/libro/<id>/` | Detalle de un libro     |
| `/admin/`      | Panel de administración |

Para entrar en el panel hay que crear antes un superusuario:

```bash
python manage.py createsuperuser
```

Desde el panel se pueden gestionar `Libro`, `Autor` y `Editorial`.

## Actividades de la UT4

Cada actividad tiene su etiqueta (`ut4-act1` a `ut4-act5`) para localizar el estado exacto del proyecto en ese momento.

| Actividad                          | Contenido                                      | Archivos                                   |
| ---------------------------------- | ---------------------------------------------- | ------------------------------------------ |
| 1. Exploración de la base de datos | Proyecto, aplicación y migraciones iniciales   | `biblioteca/settings.py`                   |
| 2. Creación de modelos             | `Autor`, `Editorial` y `Libro`                 | `catalogo/models.py`, `Actividad2.md`      |
| 3. Gestión de migraciones          | Migraciones 0001 a 0005                        | `catalogo/migrations/`, `Actividad3.md`    |
| 4. CRUD del catálogo               | Crear, leer, actualizar y borrar con el ORM    | `actividad4_crud.py`, `Actividad4.md`      |
| 5. Boletín de consultas ORM        | 15 consultas con filtros, orden y agregaciones | `actividad5_consultas.py`, `Actividad5.md` |

Los scripts de las actividades 4 y 5 se ejecutan igual que la carga de datos (en Windows, con `PYTHONUTF8=1`, como se explica arriba):

```bash
python manage.py shell < actividad4_crud.py
python manage.py shell < actividad5_consultas.py
```

### Consultas ORM y resultados

Las 15 consultas de la Actividad 5, con sus resultados y las respuestas a las preguntas, están en [`Actividad5.md`](Actividad5.md). El script [`actividad5_consultas.py`](actividad5_consultas.py) las ejecuta e imprime los resultados. Para obtener los mismos datos, hay que partir de los diez libros de `cargar_libros.py` con `REINICIAR = True`.

## Migraciones

| Migración                 | Cambio                                                                              |
| ------------------------- | ----------------------------------------------------------------------------------- |
| `0001_initial`            | Tablas de `Autor`, `Editorial` y `Libro`                                            |
| `0002_libro_idioma`       | Campo `Libro.idioma`                                                                |
| `0003_libro_recomendado`  | Campo `Libro.recomendado`                                                           |
| `0004_editorial_pais`     | Campo `Editorial.pais`                                                              |
| `0005_ajustes_actividad2` | `isbn` y `Editorial.nombre` únicos, `Editorial.activa` y `titulo` de 200 caracteres |

## Configuración de la base de datos

La configuración de `DATABASES` está en `biblioteca/settings.py`.

### SQLite (configuración actual)

```python
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
```

### PostgreSQL (ejemplo)

Requiere el controlador `psycopg` (`pip install "psycopg[binary]"`) y un servidor PostgreSQL con la base de datos ya creada. Las credenciales se leen de variables de entorno y **nunca** se escriben en el código ni se suben al repositorio.

```python
import os

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.environ.get("DB_NAME", "biblioteca"),
        "USER": os.environ.get("DB_USER", ""),
        "PASSWORD": os.environ.get("DB_PASSWORD", ""),
        "HOST": os.environ.get("DB_HOST", "localhost"),
        "PORT": os.environ.get("DB_PORT", "5432"),
    }
}
```

Después de cambiar de gestor hay que volver a ejecutar `python manage.py migrate`.

## Qué no se versiona

El entorno virtual (`.venv/`), la base de datos local (`db.sqlite3`), los archivos de entorno (`.env`) y los temporales (`*.old`, `*.bk`, `shell*.txt`) están en `.gitignore`.

## Estructura

```txt
MiBiblioteca/
├── biblioteca/            # configuración del proyecto
├── catalogo/              # aplicación: modelos, vistas, plantillas, migraciones
├── actividad4_crud.py
├── actividad5_consultas.py
├── cargar_libros.py
├── Actividad2.md ... Actividad5.md
├── manage.py
└── requirements.txt
```
