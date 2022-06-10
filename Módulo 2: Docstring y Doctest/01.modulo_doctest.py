# Docstring: podemos probar nuestro código a través de los comentarios con el módulo doctest
# "python3 -m doctest nombre-del-archivo.py -v" => cuidado con poner 01. en el nombre que da error de módulo (no sé por qué)
# El Docstring es más para documentar, por lo que no es necesario colocar muchos llamados o pruebas (max: 3).
# En realidad, no es buena práctica hacer las pruebas por DocString.

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
