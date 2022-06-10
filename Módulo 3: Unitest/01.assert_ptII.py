
def suma_nros_positivos(n1: int, n2: int) -> int:
    """Permite sumar dos números enteros positivos.

    Args:
        n1 (int): 
        n2 (int): 

    Returns:
        int: 
    """

    """ A veces no se tienen en cuenta todos los casos y se crea un bug, se puede condidionar:
    if n1 < 0 or n2 > 0:
        return None
    Pero ya dijimos que es mejor trabajar con los errores...
    """
    assert n1 > 0 and n2 > 0, 'Lo sentimos, solo es posible sumar números positivos.'  # si está todo ok, se sigue.
    # Delegamos la responsabilidad a quien llamó la función, en este caso al bloque de abajo.
    return n1 + n2


if __name__ == '__main__':
    r = suma_nros_positivos(-10, 20)
    print(r)
