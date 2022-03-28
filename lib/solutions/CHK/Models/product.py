from dataclasses import dataclass
from typing import Optional
from lib.solutions.CHK.Models.offer import Offer


@dataclass
class Product:
    sku: str
    price: int = None
    offer: set() = None

    def __hash__(self):
        return hash(self.sku)

    def __eq__(self, product):
        return self.sku == product.sku
