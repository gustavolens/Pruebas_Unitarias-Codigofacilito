# Líbrearía Unitest = excelente para pruebas unitarias.
# assert = palabra reservada para evaluar una condición
# Si es True, continúa con su ejecución.
# Si es False, AsserstionError

if __name__ == '__main__':
    # assert 5 == 10, 'Lo sentimos, cinco no es igual a diez.'
    # Con la línea anterior se muestra en pantalla más info.
    # print('>>> El programa continúa con su ejercución.')

    try:
        assert 5 == 10, 'Lo sentimos, cinco no es igual a diez.'
        print('>>> El programa continúa con su ejercución')
        # En Python, se recomienda trabajar con error y no, validaciones.
        # "Más vale pedir perdón que permiso." => trabajar con excepciones y no condicionar.

        """Con validaciones:
        if not 5 == 10:
            raise AssertionError('Lo sentimos, cinco no es igual a diez.')
        """
    except AssertionError as error:
        print(error)
    # Se visualiza solo el mensaje de error.
