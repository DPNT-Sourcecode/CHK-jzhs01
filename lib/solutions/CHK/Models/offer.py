from dataclasses import dataclass

class Offer:
    def __init__(self, product_count):
        self.product_count = product_count


class PriceReduction(Offer):
    def __init__(self, product_count, new_price: int):
        super().__init__(product_count)
        self.new_price = new_price

# class FreeItem(Offer):
#     product: Product
#     count: int = 1




