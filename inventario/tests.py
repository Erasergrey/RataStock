from decimal import Decimal

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase
from rest_framework.test import APIClient

from .models import Producto


class ProductoValidacionTests(TestCase):
    def test_precio_negativo_es_invalido(self):
        producto = Producto(nombre="Producto", stock=0, precio=Decimal("-1.00"))

        with self.assertRaises(ValidationError) as error:
            producto.full_clean()

        self.assertIn("precio", error.exception.message_dict)

    def test_stock_negativo_es_invalido(self):
        producto = Producto(nombre="Producto", stock=-1, precio=Decimal("1.00"))

        with self.assertRaises(ValidationError) as error:
            producto.full_clean()

        self.assertIn("stock", error.exception.message_dict)

    def test_nombre_vacio_es_invalido(self):
        producto = Producto(nombre="", stock=0, precio=Decimal("1.00"))

        with self.assertRaises(ValidationError) as error:
            producto.full_clean()

        self.assertIn("nombre", error.exception.message_dict)


class ProductoApiValidacionTests(TestCase):
    def setUp(self):
        self.usuario = get_user_model().objects.create_user(
            username="api-test-user",
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.usuario)

    def test_post_con_precio_negativo_devuelve_400(self):
        respuesta = self.client.post(
            "/api/productos/",
            {
                "nombre": "Producto inválido",
                "descripcion": "",
                "stock": 1,
                "precio": "-1.00",
                "activo": True,
            },
            format="json",
        )

        self.assertEqual(respuesta.status_code, 400)
        self.assertIn("precio", respuesta.data)
