from dataclasses import dataclass
from lib.solutions.CHK.product import Product


@dataclass
class Stock(Product):
    current_stock: dict

    def check_item_in_stock(self, product: Product):
        return product in self.stock


