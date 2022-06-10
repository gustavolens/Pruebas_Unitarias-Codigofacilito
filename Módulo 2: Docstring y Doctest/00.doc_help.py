# Docstring: diseñado para documentar obj. Debe estar en la primera línea del bloque.
# Recordar: TODO es un objeto

# En el shell => python3 => from *nombre-del-archivo* (Da error con los nombres '01...') import *nombre-de-función*
# palindromo.__doc__ => Se visualiza lo escrito en los comentarios """...."""
# MEJOR CON: help(palindromo)

def palindromo(sentence: str) -> bool:
    """Permite conocer si un string es un palíndromo.

    Args:
        sentence (str): String por evaluar

    Returns:
        bool: True or False
    """
    sentence = sentence.lower().replace(' ', '')
    return sentence == sentence[::-1]
