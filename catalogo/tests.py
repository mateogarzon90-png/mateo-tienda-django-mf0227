from django.test import TestCase
from .dominio import ProductoOferta

class CatalogoTests(TestCase):
    def test_calculo_descuento(self):
        # 1. Verificar que un producto de 100 € con un descuento del 20% devuelve 80 €
        producto = ProductoOferta("Test", 100.0, 20)
        self.assertEqual(producto.precio_final(), 80.0)

    def test_pagina_productos_status_200(self):
        # 2. Verificar que la página /productos/ responde con el código HTTP 200
        response = self.client.get('/productos/')
        self.assertEqual(response.status_code, 200)