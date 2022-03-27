from dataclasses import dataclass

from lib.solutions.CHK.product import Product


@dataclass
class Offer:
    product_count: int


class PriceReduction(Offer):
    new_price: int


class FreeItem(Offer):
    item: Product
    count: int = 1


