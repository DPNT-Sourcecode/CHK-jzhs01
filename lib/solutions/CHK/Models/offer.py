from dataclasses import dataclass

from lib.solutions.CHK.Models.product import Product


@dataclass
class Offer:
    product_count: int


class PriceReduction(Offer):
    new_price: int



class FreeItem(Offer):
    product: Product
    count: int = 1
