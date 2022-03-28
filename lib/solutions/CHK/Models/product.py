from dataclasses import dataclass


@dataclass
class Product:
    sku: str
    price: int = None
    offer: set() = None

    def __hash__(self):
        return hash(self.sku)

    def __eq__(self, product):
        return self.sku == product.sku
