from dataclasses import dataclass
from lib.solutions.CHK.product import Product

@dataclass
class Stock(Product):

        stock: dict() = {
            Product(sku="A", price=50, offer={3: 130}),
            Product(sku="B", price=30, offer={2: 45}),
            Product(sku="C", price=20),
            Product(sku="D", price=15)
        }

    def check_item_in_stock(self, product: Product):
        return product in self.stock

