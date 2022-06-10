import unittest
from product import Product
from shopping_cart import ShoppingCart

class TestShoopingCart(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('>>> El método de clase setUpClass se ejecuta antes que todas las pruebas')
    @classmethod
    def tearDownClass(cls):
        print('>>> El método de clase tearDownClass se ejecuta después que todas las pruebas')
    
    # Crear objeto de tipo Product (se puede utilizar en cualquie método o prueba):
    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)
        self.shopping_cart_1 = ShoppingCart()
        
        self.shopping_cart_2 = ShoppingCart()
        self.shopping_cart_2.add_product(self.smartphone)

    def tearDown(self):
        pass        

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

    def test_shopping_car_empty(self):
        self.assertTrue(self.shopping_cart_1.empty(), 'Lo sentimos, el carrito de compras no se encuentra vacío.')

    def test_shopping_car_has_products(self):
        self.assertTrue(self.shopping_cart_2.has_products)
        self.assertFalse(self.shopping_cart_2.empty())

if __name__ == '__main__':
    unittest.main()
