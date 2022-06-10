import unittest
from product import Product


class TestShoopingCart(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print('>>> El método de clase setUpClass se ejecuta antes que todas las pruebas')
    # Por ejemplo, se usa para comprobar algún camnbio en la base de datos
    @classmethod
    def tearDownClass(cls): # se puede reiniciar los valores establecidos en setUpClass
        print('>>> El método de clase tearDownClass se ejecuta después que todas las pruebas')
    
    # Crear objeto de tipo Product (se puede utilizar en cualquie método o prueba):
    def setUp(self):
        self.name = 'iPhone'
        self.price = 500.00

        self.smartphone = Product(self.name, self.price)

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

if __name__ == '__main__':
    unittest.main()
