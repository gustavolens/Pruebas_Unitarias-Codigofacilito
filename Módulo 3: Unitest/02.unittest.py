# Líbrearía Unitest = excelente para pruebas unitarias.
# Librearía estándar de Python, no hace falta instalar nada. Est

import unittest

# Algo recomendable es llamar a las clases con "Test..."


class TestExample(unittest.TestCase):  # Clase TestCase
    # Definir las pruebas unitarias a través de métodos.
    def test_suma_numeros(self):
        n1 = 10
        n2 = 20

        result = n1 + n2

        # Comparar que dos objetos tengan el mismo valor.
        self.assertEqual(result, 30)
        # Lo anterior es equivalente a 'assert result == 30'.

    def test_resta_numeros(self):
        self.assertEqual(30 - 20, 10)


if __name__ == '__main__':
    # La función .main() ejecutará todos los métodos que posean el prefijo "test_"
    unittest.main()
    # que se encuentren en las clases que hereden de TestCase.
