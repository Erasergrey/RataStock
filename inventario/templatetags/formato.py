"""Formatos de presentación; no alteran los valores almacenados."""

from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

from django import template

register = template.Library()


@register.filter
def clp(valor):
    """Muestra pesos enteros con punto de miles y redondeo de medio hacia arriba."""
    try:
        numero = Decimal(str(valor))
        if not numero.is_finite():
            return "—"
        pesos = numero.quantize(Decimal("1"), rounding=ROUND_HALF_UP)
    except (InvalidOperation, TypeError, ValueError):
        return "—"
    return f"${pesos:,.0f}".replace(",", ".")
