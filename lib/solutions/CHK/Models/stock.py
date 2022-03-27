from dataclasses import dataclass


from lib.solutions.CHK.Models.product import Product


@dataclass
class Stock:
    stock: set(Product)

    def check_item_in_stock(self, product: Product):
        return product in self.stock




