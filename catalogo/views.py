from django.shortcuts import get_object_or_404, render
from .models import Libro, Autor, Editorial

# Create your views here.

def principal(request):
    libro = Libro.objects.all().filter(id=1).update(titulo="El Principito", autor="Antoine de Saint-Exupéry")
    
    #libro.titulo = libro.titulo.upper()
    #libro.titulo = libro.titulo.replace('a', '4')
    #libro.save()
    
    return render(request, 'catalogo/principal.html')
    

def lista_libros(request):
    libros = Libro.objects.order_by("titulo")
    return render(request, "catalogo/lista_libros.html", {"libros": libros})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, "catalogo/detalle_libro.html", {"libro": libro})