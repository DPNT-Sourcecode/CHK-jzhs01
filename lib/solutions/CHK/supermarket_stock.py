from lib.solutions.CHK.approach_2.product import Product


class Stock:

    def __init__(self):
        self.prices = {"A": 50, "B": 30, "C": 20, "D": 15}
        self.deals = {"A": [3, 130], "B": [2, 45]}

    def get_prices(self):
        return self.prices

    def get_deals(self):
        return self.deals
