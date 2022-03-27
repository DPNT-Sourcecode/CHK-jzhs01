from lib.solutions.CHK.product import Product


class Stock(Product):

    def __init__(self):
        self.stock = {"A": 50, "B": 30, "C": 20, "D": 15}
        self.deals = {"A": [3, 130], "B": [2, 45]}



