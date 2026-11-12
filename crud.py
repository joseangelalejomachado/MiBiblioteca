# Crear registros (Create) de un libro

# if por si el libro ya existe, para no duplicarlo
if not Libro.objects.filter(isbn="9780000000011").exists():
    from datetime import date
    from decimal import Decimal
    from catalogo.models import Libro, Editorial, Autor
    libro = Libro.objects.create(
        titulo="El ingenioso hidalgo Don Quijote de la Mancha",
        autor="Miguel de Cervantes",
        isbn="9780000000011",
        sinopsis="Novela clásica de la literatura española.",
        fecha_publicacion=date(1605, 1, 16),
        anio_publicacion=1605,
        paginas=1200,
        precio=Decimal("19.90"),
        disponible=True,
        idioma="Español",
        genero=Libro.Genero.NOVELA,
        dificultad=Libro.Dificultad.INTERMEDIA,
    )

    print(libro.pk, libro.titulo)

# If por si la editorial ya existe, para no duplicarla
if not Editorial.objects.filter(nombre="Editorial Planeta").exists():
    editorial = Editorial.objects.create(
        nombre="Editorial Planeta",
        email="contacto@planetadelibros.com",
        sitio_web="https://www.planetadelibros.com",
    )

    print(editorial.pk, editorial.nombre)

# If por si el autor ya existe, para no duplicarlo
if not Autor.objects.filter(nombre="Miguel", apellidos="de Cervantes Saavedra").exists():
    autor = Autor.objects.create(
        nombre="Miguel",
        apellidos="de Cervantes Saavedra",
        fecha_nacimiento=date(1547, 9, 29),
        nacionalidad="Española",
        biografia="Escritor español, autor de Don Quijote de la Mancha.",
    )

    print(autor.pk, autor.nombre, autor.apellidos)

# Recuperar registros (Read) de libros

Libro.objects.all()
Libro.objects.count()
Libro.objects.first()
try:
    encontrado = Libro.objects.get(isbn="9780000000011")
    print(encontrado.titulo)
except Libro.DoesNotExist:
    print("No se ha encontrado el libro")

print(autor.pk, autor)

# Recuperar registros (Read) de libros

Libro.objects.all()
Libro.objects.count()
Libro.objects.first()
try:
    encontrado = Libro.objects.get(isbn="9780000000001")
    print(encontrado.titulo)
except Libro.DoesNotExist:
    print("No se ha encontrado el libro")
    

# Modificar registros (Update) de un libro

libro = Libro.objects.get(isbn="9780000000011")
libro.precio = Decimal("100.90")
libro.disponible = False
libro.save()

# Instrucción para ejecutar en la shell de Django para actualizar un libro -> python manage.py shell < crud.py