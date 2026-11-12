from django.urls import path

from . import views

urlpatterns = [
    path("", views.lista_libros, name="lista_libros"),
    path("libro/<int:pk>/", views.detalle_libro, name="detalle_libro"),
    path("principal", views.principal, name="principal"),
]