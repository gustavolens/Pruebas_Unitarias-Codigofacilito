from product import Product

class ShoppingCart:

    def __init__(self) -> None:
        #self.__products = list()
        #__ => atributo privado

        #Utilizando anotaciones:
        List = 0
        self.__products: List[Product] = []

    def add_product(self, product: Product) -> None:
        # TAREA: Verificar que el objeto pasado como arg sea de tipo product.
        # También hacer una prueba unitaria.
        self.__products.append(product)

    def empty(self) -> bool:
        return len(self.__products) == 0

    def has_products(self):
        return not self.empty()