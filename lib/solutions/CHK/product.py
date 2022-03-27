from dataclasses import dataclass

from lib.solutions.CHK.offer import Offer


@dataclass
class Product(Offer):
    sku: str
    price: int = None
    offer: dict = None

    def __hash__(self):
        return hash(self.sku)

    def __eq__(self, product):
        return self.sku == product.sku
