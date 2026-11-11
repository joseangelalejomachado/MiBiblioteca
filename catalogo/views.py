from django.shortcuts import get_object_or_404, render
from .models import Libro

# Create your views here.

def lista_libros(request):
    libros = Libro.objects.order_by("titulo")
    return render(request, "catalogo/lista_libros.html", {"libros": libros})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, "catalogo/detalle_libro.html", {"libro": libro})