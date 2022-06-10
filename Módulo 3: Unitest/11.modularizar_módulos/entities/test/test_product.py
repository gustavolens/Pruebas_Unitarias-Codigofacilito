import unittest

from entities.product import Product

class TestProduct(unittest.TestCase):
    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)

        # Primera prueba: 
    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        product = Product(name, price)

        # assert product.name == name
        # assert product.price == price, 'Lo sentimos, el precio no es el mismo.'
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, price, 'Lo sentimos, el precio no es el mismo.')

    # Segunda prueba:
    def test_product_name(self):
        self.assertEqual(self.smartphone.name, self.name)
    
    #Tercera prueba:
    def test_product_price(self):
        self.assertEqual(self.smartphone.price, self.price)

    def test_example(self):
        self.assertEqual(1, 1)