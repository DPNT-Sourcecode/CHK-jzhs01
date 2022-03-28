from dataclasses import dataclass

from lib.solutions.CHK.Models.product import Product


class Offer:
    def __init__(self, product_count):
        self.product_count = product_count


class PriceReduction(Offer):
    def __init__(self, product_count, new_price: int):
        super().__init__(product_count)
        self.new_price = new_price


class FreeItem(Offer):
    def __init__(self, product_count, product: Product, count: int = 1):
        super().__init__(product_count)
        self.product = product
        self.count = count
