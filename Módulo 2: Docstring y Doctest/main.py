"""Este el Docstring del módulo main"""

# El módulo test no es un framework de testing porque carece de herramientas para hacer
# las pruebas unitarias (hacer ciclos, asignando valores).
# Se puede hacer dentro del Docstring, pero lo correcto es hacerlo en un archivo externo .txt.
# Todos deben empezar con "test_" ejemplo: "test_main.txt"


class User:
    """Permite representar un usuario"""

    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto tipo User.

        Args:
            username (str): El nombre del usuario.
            password (str): La contraseña del usuario.
        """
        self.username = username
        self.password = password


def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es un palíndromo.

    Args:
        sentence (str): String por evaluar

    Returns:
        bool: True or False

    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]
