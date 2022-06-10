class ProductDiscountError(Exception):
    pass


class Product:

    # float = 0.0 => sin descuento por default.
    def __init__(self, name: str, price: float, discount: float = 0.0) -> None:
        self.name = name
        self.price = price
        
        if discount > price:
            raise ProductDiscountError('Lo sentimos, el descuento no puede ser mayor al precio.')
        # Se puede usar assert, pero este nos devuelve un assertionError
        # es interesante trabajar con nuestros errores.

        self.discount = discount
    
    @property
    def code(self):
        return f'code-{self.name}'
