# Actividad de clase 2

## 7. Actividad 2. Creación de modelos Django

**Objetivo:** crear modelos con tipos de campos y restricciones adecuados.

En la aplicación `catalogo`, definir **tres modelos independientes**, todavía sin relaciones.

### Modelo Autor

| Campo            | Tipo        | Restricciones                      |
| ---------------- | ----------- | ---------------------------------- |
| nombre           | `CharField` | Máximo 100 caracteres              |
| apellidos        | `CharField` | Máximo 150 caracteres              |
| fecha_nacimiento | `DateField` | Opcional (`null=True, blank=True`) |
| nacionalidad     | `CharField` | Máximo 50 caracteres               |
| biografia        | `TextField` | Opcional (`blank=True`)            |

### Modelo Editorial

| Campo     | Tipo           | Restricciones                |
| --------- | -------------- | ---------------------------- |
| nombre    | `CharField`    | Máximo 150 caracteres, único |
| email     | `EmailField`   | Opcional (`blank=True`)      |
| sitio_web | `URLField`     | Opcional (`blank=True`)      |
| activa    | `BooleanField` | `default=True`               |

### Modelo Libro

| Campo             | Tipo                   | Restricciones                                                                              |
| ----------------- | ---------------------- | ------------------------------------------------------------------------------------------ |
| titulo            | `CharField`            | Máximo 200 caracteres                                                                      |
| isbn              | `CharField`            | Máximo 13 caracteres, único                                                                |
| sinopsis          | `TextField`            | Opcional (`blank=True`)                                                                    |
| fecha_publicacion | `DateField`            | Obligatorio                                                                                |
| paginas           | `PositiveIntegerField` | Obligatorio                                                                                |
| precio            | `DecimalField`         | `max_digits=8`, `decimal_places=2`                                                         |
| disponible        | `BooleanField`         | `default=True`                                                                             |
| genero            | `CharField`            | `choices` mediante clase interna `Genero(TextChoices)`, valor predeterminado Novela        |
| dificultad        | `IntegerField`         | `choices` mediante clase interna `Dificultad(IntegerChoices)`, valor predeterminado Básica |

**Tareas adicionales:**

1. Incorporar `__str__()` a los tres modelos.
2. Configurar el orden predeterminado de libros y autores mediante `Meta`.
3. Definir en `Libro` una clase interna `Genero(models.TextChoices)` con Novela, Poesía, Teatro, Ensayo y Cómic, utilizando códigos de tres caracteres.
4. Definir una clase interna `Dificultad(models.IntegerChoices)` con Básica (1), Intermedia (2) y Avanzada (3).
5. Incorporar ambos campos al modelo con sus `choices` y valores predeterminados.
6. Explicar por qué se ha elegido cada tipo de campo y distinguir el valor almacenado de la etiqueta visible.
7. Explicar por qué `choices` no sustituye siempre a una relación `ForeignKey`.

**Entrega:** archivo `catalogo/models.py` con las tres clases. No crear todavía relaciones entre modelos; se estudiarán más adelante.

## Resultado esperado

Tres modelos Django definidos con campos, restricciones, opciones predefinidas y representación legible, preparados para generar sus migraciones en el bloque 3. No es necesario ejecutar todavía consultas ni migraciones.
