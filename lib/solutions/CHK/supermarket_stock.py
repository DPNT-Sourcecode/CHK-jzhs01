from lib.solutions.CHK.product import Product


class Stock(Product):

    def __init__(self, stock):
        stock = [
             Product(sku="A", price=50, offer={3: 130}),
            Product(sku="B", price=30, offer={3: 130}),
                 ]
