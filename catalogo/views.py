from django.shortcuts import get_object_or_404, render
from .models import Libro, Autor, Editorial
from django.db.models import Q

# Create your views here.

def principal(request):
    #libro = Libro.objects.all().filter(id=1).update(titulo="El Principito", autor="Antoine de Saint-Exupéry")
    #libro.titulo = libro.titulo.upper()
    #libro.titulo = libro.titulo.replace('a', '4')
    #libro.save()
    print("\n--- Consulta1 ---")
    consulta = Libro.objects.filter(Q(titulo__startswith = "Python") & Q(titulo__icontains="Django"))
    for libro in consulta:
        print(libro.titulo)
    print("\n--- Consulta2 ---")
    consulta2 = Libro.objects.filter(Q(titulo__startswith = "Python") | Q(titulo__icontains="a"))
    for libro in consulta2:
        print(libro.titulo)
        
    print("\n--- Consulta3 ---")
    consulta3 = Libro.objects.filter(Q(titulo__startswith = "Python") | Q(paginas__lte=100))
    for libro in consulta3:
        print(libro.titulo)
    return render(request, 'catalogo/principal.html')
    

def lista_libros(request):
    libros = Libro.objects.order_by("titulo")
    return render(request, "catalogo/lista_libros.html", {"libros": libros})

def detalle_libro(request, pk):
    libro = get_object_or_404(Libro, pk=pk)
    return render(request, "catalogo/detalle_libro.html", {"libro": libro})