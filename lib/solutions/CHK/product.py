from dataclasses import dataclass
from typing import Optional
from lib.solutions.CHK.offer import Offer


@dataclass
class Product:
    sku: str
    price: int = None
    # offer: Optional[set(Offer)] = None

    def __hash__(self):
        return hash(self.sku)

    def __eq__(self, product):
        return self.sku == product.sku

