from catalogo.models import Libro

libros = [
    ("Don Quijote de la Mancha", "Miguel de Cervantes", "Novela", 1605, True),
    ("Cien años de soledad", "Gabriel García Márquez", "Realismo mágico", 1967, True),
    ("1984", "George Orwell", "Distopía", 1949, False),
    ("El Hobbit", "J. R. R. Tolkien", "Fantasía", 1937, True),
    ("La sombra del viento", "Carlos Ruiz Zafón", "Misterio", 2001, True),
]

for titulo, autor, genero, anio, disponible in libros:
    Libro.objects.get_or_create(
        titulo=titulo,
        defaults={
            "autor": autor,
            "genero": genero,
            "anio_publicacion": anio,
            "disponible": disponible,
        },
    )

print("Libros en la base de datos:", Libro.objects.count())