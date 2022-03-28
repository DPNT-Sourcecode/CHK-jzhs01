from dataclasses import dataclass
from lib.solutions.CHK.Models.product import Product


class Stock:
    def __init__(self, stock: set() = None):
        self.stock = stock

    @classmethod
    def check_if_item_in_stock(cls, product: Product):
        return product in cls

