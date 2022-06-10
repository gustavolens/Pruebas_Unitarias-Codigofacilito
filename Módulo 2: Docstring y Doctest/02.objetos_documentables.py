"""Este el Docstring del módulo main"""

# Objetos documentables = todos aquellos objetos que se pueden documentar a través del Docstring
# Estos objetos tienen el atributo .__doc__
# Módulos, clases, métodos y funciones.


class User:
    """Permite representar un usuario"""

    def __init__(self, username: str, password: str) -> None:
        """Permite instanciar un objeto tipo User.

        Args:
            username (str): El nombre del usuario.
            password (str): La contraseña del usuario.
        """


def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es un palíndromo.

    Args:
        sentence (str): String por evaluar

    Returns:
        bool: True or False

    Examples: #Cualquier nombre (ejemplos, pruebas unitarias, etc...)

    >>> palindromo('Anita lava la tina') #esto se prueba en el shell con "python3 -m doctest nombre-del-archivo.py -v"
    True

    >>> palindromo('Codigo facilito')
    False

    >>> sentence = 'oso'
    >>> palindromo(sentence)
    True

    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]
