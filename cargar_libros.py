from datetime import date
from decimal import Decimal

from catalogo.models import Libro

# Datos de ejemplo. Los ISBN, fechas completas, páginas y precios son ficticios.
libros = [
    {
        "titulo": "Don Quijote de la Mancha",
        "autor": "Miguel de Cervantes",
        "genero": Libro.Genero.NOVELA,
        "anio_publicacion": 1605,
        "disponible": True,
        "isbn": "9780000000011",
        "fecha_publicacion": date(1605, 1, 16),
        "paginas": 1200,
        "precio": Decimal("19.90"),
    },
    {
        "titulo": "Veinte poemas de amor y una canción desesperada",
        "autor": "Pablo Neruda",
        "genero": Libro.Genero.POESIA,
        "anio_publicacion": 1924,
        "disponible": True,
        "isbn": "9780000000028",
        "fecha_publicacion": date(1924, 6, 1),
        "paginas": 96,
        "precio": Decimal("9.50"),
    },
    {
        "titulo": "Bodas de sangre",
        "autor": "Federico García Lorca",
        "genero": Libro.Genero.TEATRO,
        "anio_publicacion": 1933,
        "disponible": False,
        "isbn": "9780000000035",
        "fecha_publicacion": date(1933, 3, 8),
        "paginas": 112,
        "precio": Decimal("8.75"),
    },
    {
        "titulo": "Meditaciones del Quijote",
        "autor": "José Ortega y Gasset",
        "genero": Libro.Genero.ENSAYO,
        "anio_publicacion": 1914,
        "disponible": True,
        "isbn": "9780000000042",
        "fecha_publicacion": date(1914, 1, 1),
        "paginas": 180,
        "precio": Decimal("12.00"),
        "dificultad": Libro.Dificultad.AVANZADA,
    },
    {
        "titulo": "Persépolis",
        "autor": "Marjane Satrapi",
        "genero": Libro.Genero.COMIC,
        "anio_publicacion": 2000,
        "disponible": True,
        "isbn": "9780000000059",
        "fecha_publicacion": date(2000, 10, 1),
        "paginas": 160,
        "precio": Decimal("17.50"),
        "dificultad": Libro.Dificultad.INTERMEDIA,
    },
]

for datos in libros:
    titulo = datos.pop("titulo")
    Libro.objects.get_or_create(titulo=titulo, defaults=datos)

print("Libros en la base de datos:", Libro.objects.count())