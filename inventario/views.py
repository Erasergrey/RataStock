from django.shortcuts import get_object_or_404, redirect, render

from .forms import ProductoForm
from .models import Producto


def lista_productos(request):
    productos = Producto.objects.all().order_by("nombre")
    return render(
        request,
        "inventario/lista_productos.html",
        {"productos": productos},
    )


def crear_producto(request):
    if request.method == "POST":
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("inventario:lista_productos")
    else:
        form = ProductoForm()

    return render(
        request,
        "inventario/formulario_producto.html",
        {"form": form, "titulo": "Nuevo producto"},
    )


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        form = ProductoForm(request.POST, instance=producto)
        if form.is_valid():
            form.save()
            return redirect("inventario:lista_productos")
    else:
        form = ProductoForm(instance=producto)

    return render(
        request,
        "inventario/formulario_producto.html",
        {"form": form, "titulo": "Editar producto"},
    )


def eliminar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == "POST":
        producto.delete()
        return redirect("inventario:lista_productos")

    return render(
        request,
        "inventario/confirmar_eliminar.html",
        {"producto": producto},
    )
