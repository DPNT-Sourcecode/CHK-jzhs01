from dataclasses import dataclass


@dataclass
class Offer:
    product_count: int



class PriceReduction(Offer):
    def __init__(self, new_price: int):
        self.new_price = new_price


# class FreeItem(Offer):
#     product: Product
#     count: int = 1


