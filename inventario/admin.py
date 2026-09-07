from django.contrib import admin

from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "stock", "precio", "activo", "fecha_creacion")
    search_fields = ("nombre",)
    list_filter = ("activo",)
    ordering = ("nombre",)
