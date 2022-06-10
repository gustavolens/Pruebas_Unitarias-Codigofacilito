# MIRAR PRODUCT
import unittest
from product import Product
from product import ProductDiscountError
from shopping_cart import ShoppingCart

# Para el skilIf
def is_available_to_skip():
    return False
def is_connected():
    return False

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
    
    # Probar si está dentro
    def test_product_in_shopping_cart(self):
        product = Product('Nuevo producto', 10) # nuevo producto
        self.shopping_cart_2.add_product(product) # se añade al carrito
       
        self.assertIn(product, self.shopping_cart_2.products)
        self.assertIn(self.smartphone, self.shopping_cart_2.products) # Verifica si el objeto está dentro de la colección.

    
    # Probar la eliminación un producto.
    def test_product_not_in_shopping_cart(self):
        self.shopping_cart_2.remove_product(self.smartphone) # se borra

        self.assertNotIn(self.smartphone, self.shopping_cart_2.products)

    # Probar el objeto error. Caso descuento más alto que precio.
    def test_discount_error(self):
        with self.assertRaises(ProductDiscountError):
            Product(name='Example', price=10.0, discount=11.0) # Creamos un obj con descuento>precio

    #Probar el total 
    def test_total_shopping_cart(self):
        self.shopping_cart_1.add_product(Product(name='Libro', price = 15.0))
        self.shopping_cart_1.add_product(Product(name='Cámara', price = 700, discount = 70))
        self.shopping_cart_1.add_product(Product(name='PC', price = 1000, discount = 0.0))
        
        self.assertGreater(self.shopping_cart_1.total, 0) # >
        self.assertLess(self.shopping_cart_1.total, 2000) # <
        self.assertEqual(self.shopping_cart_1.total, 1645.00)
        
        # assertGreaterEqual
        # assertLessEqual
   
    # Probar el total del carrito 1 que por defecto está vacío.  
    def test_total_empty_shopping_cart(self):
        self.assertEqual(self.shopping_cart_1.total, 0)
    
    #Saltar prueba
    @unittest.skip('Escribimos las razones de saltar.')
    def test_skip_example(self):
        self.assertEqual(1, 1)

    # Dos funciones
    # skipIf -> si es True, se salta
    # skipUnless -> si es False, se salta
    @unittest.skipUnless(is_connected(), 'Las posibles razones de saltar.')
    def test_skip_example_two(self):
        pass
    
    #Expresiones regulares
    def test_code_product(self):
        self.assertRegex(self.smartphone.code, self.smartphone.name) #Regex 

if __name__ == '__main__':
    unittest.main()
