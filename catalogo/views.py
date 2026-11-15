from django.db.models import Avg, Count, Max, Min, Q
from django.shortcuts import get_object_or_404, render

from .models import Libro

# Create your views here.

def principal(request):
    """Resumen del catálogo con ejemplos de Q, aggregate() y annotate()."""
    # Objetos Q: combinaciones lógicas de condiciones (AND, OR y NOT)
    python = Q(titulo__icontains="python")
    django = Q(titulo__icontains="django")
    python_y_django = Libro.objects.filter(python & django)
    python_o_django = Libro.objects.filter(python | django)
    sin_python = Libro.objects.filter(~python)

    # aggregate(): un único resumen de todo el catálogo (devuelve un diccionario)
    resumen = Libro.objects.aggregate(
        total=Count("id"),
        media=Avg("precio"),
        maximo=Max("precio"),
        minimo=Min("precio"),
    )

    # values() + annotate(): un valor calculado por cada grupo
    por_disponibilidad = (
        Libro.objects.values("disponible")
        .annotate(total=Count("id"))
        .order_by("-disponible")
    )
    por_genero = [
        {
            "genero": Libro.Genero(fila["genero"]).label,
            "total": fila["total"],
            "precio_medio": fila["precio_medio"],
        }
        for fila in Libro.objects.values("genero")
        .annotate(total=Count("id"), precio_medio=Avg("precio"))
        .order_by("genero")
    ]

    contexto = {
        "python_y_django": python_y_django,
        "python_o_django": python_o_django,
        "sin_python": sin_python,
        "resumen": resumen,
        "por_disponibilidad": por_disponibilidad,
        "por_genero": por_genero,
    }
    return render(request, "catalogo/principal.html", contexto)


def lista_libros(request):
    libros = Libro.objects.order_by("titulo")
    return render(request, "catalogo/lista_libros.html", {"libros": libros})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, "catalogo/detalle_libro.html", {"libro": libro})