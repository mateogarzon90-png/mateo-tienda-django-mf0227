class ProductoBase:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        # Validación para que el precio no sea negativo
        if precio < 0:
            raise ValueError("El precio no puede ser negativo.")
        self.precio = precio

    # Método que devuelve el precio original[cite: 3]
    def precio_final(self):
        return self.precio


class ProductoOferta(ProductoBase): # Hereda de ProductoBase
    def __init__(self, nombre, precio, descuento):
        super().__init__(nombre, precio)
        # Añade el atributo descuento[cite: 3]
        self.descuento = descuento

    # Sobrescribe el método aplicando el descuento
    def precio_final(self):
        # Ejemplo: 100 - (100 * 20 / 100) = 80
        descuento_aplicado = self.precio * (self.descuento / 100)
        return self.precio - descuento_aplicado