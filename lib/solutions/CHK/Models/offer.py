from dataclasses import dataclass


@dataclass
class Offer:
    product_count: int


class PriceReduction(Offer):
    new_price: int


# class FreeItem(Offer):
#     product: Product
#     count: int = 1

