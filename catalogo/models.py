from django.db import models

# Create your models here.

class Libro(models.Model):
    # Clases intermedias
    class Genero(models.TextChoices):
        NOVELA = "NOV", "Novela"
        POESIA = "POE", "Poesía"
        TEATRO = "TEA", "Teatro"
        ENSAYO = "ENS", "Ensayo"
        COMIC = "COM", "Cómic"
    class Dificultad(models.IntegerChoices):
        BASICA = 1, "Básica"
        INTERMEDIA = 2, "Intermedia"
        AVANZADA = 3, "Avanzada"
    # DECLARACIÓN DE ATRIBUTOS
    titulo = models.CharField(max_length=150)
    autor = models.CharField(max_length=100)
    isbn = models.CharField(max_length=13)
    sinopsis = models.TextField(blank=True)
    fecha_publicacion = models.DateField()
    anio_publicacion = models.IntegerField("año de publicación")
    paginas = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=8, decimal_places=2)
    disponible = models.BooleanField(default=True)
    idioma = models.CharField(max_length=30, default="Español") # Si definimos un campo obligatorio sin declarar valor por defecto, si hay tablas con Datos al hacer makemigrations python pedirá un valor por defecto
    genero = models.CharField(
        max_length=50,
        choices=Genero.choices,
        default=Genero.NOVELA,
    )
    dificultad = models.IntegerField(
        choices=Dificultad.choices,
        default=Dificultad.BASICA,
    )
    def __str__(self):
        return self.titulo
    

    class Meta:
        ordering = ["titulo"]
        verbose_name = "Libro"
        verbose_name_plural = "Libros"
    
class Editorial(models.Model):
    nombre = models.CharField(max_length=150)
    email = models.EmailField(blank=True)
    sitio_web = models.URLField(
        max_length=500,
        null=True,
        blank=True,
    )   # Defino como null=True y blank=True para permitir que el campo esté vacío
    
    def __str__(self):
        return self.nombre

class Autor(models.Model):
    nombre = models.CharField(max_length=100)
    apellidos = models.CharField(max_length=150)
    fecha_nacimiento = models.DateField(null=True, blank=True)
    nacionalidad = models.CharField(max_length=50)
    biografia = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellidos}"
    class Meta:
        ordering = ["apellidos", "nombre"]
        verbose_name = "Autor"
        verbose_name_plural = "Autores"
        
# Choices no siempre sustituye una relación ForeignKey porque no 
# permite almacenar información adicional sobre la relación.
# Si quisiera almacenar la fecha en que un autor escribió un libro, no podríamos hacerlo con un campo de tipo Choice.
# Sería más adecuado utilizar una relación ManyToMany(N:M) con un modelo intermedio que por normalización almacene la información adicional.