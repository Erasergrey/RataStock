from django import forms

from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ("nombre", "descripcion", "stock", "precio", "activo")
        widgets = {
            "descripcion": forms.Textarea(attrs={"rows": 4}),
        }
