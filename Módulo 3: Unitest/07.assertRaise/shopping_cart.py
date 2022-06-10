# MIRAR PRODUCT
from product import Product

class ShoppingCart:

    def __init__(self) -> None:
        #self.__products = list()
        #__ => atributo privado

        #Utilizando anotaciones:
        Lista = 0
        self.__products: Lista[Product] = []

    @property 
    def products(self):
        # Muestra el lista de productos
        return self.__products.copy() # Copy para evitar que se puede modificar desde afuera.

    def add_product(self, product: Product) -> None:
        self.__products.append(product)

    def empty(self) -> bool:
        return len(self.__products) == 0

    def has_products(self):
        return not self.empty()
    
    # Para eliminar
    def remove_product(self, product: Product) -> None:
        self.__products.remove(product)
