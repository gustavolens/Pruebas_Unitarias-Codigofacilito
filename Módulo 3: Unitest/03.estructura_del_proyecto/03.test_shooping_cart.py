import unittest
from product import Product


class TestShoopingCart(unittest.TestCase):
    def test_product_object(self):
        name = 'Manzana'
        price = 1.70

        product = Product(name, price)

        # assert product.name == name
        # assert product.price == price, 'Lo sentimos, el precio no es el mismo.'
        self.assertEqual(product.name, name)
        self.assertEqual(product.price, 10, 'Lo sentimos, el precio no es el mismo.')


if __name__ == '__main__':
    unittest.main()
