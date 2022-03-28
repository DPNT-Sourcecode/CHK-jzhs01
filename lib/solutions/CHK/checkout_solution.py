from lib.solutions.CHK.Models.product import Product
from lib.solutions.CHK.current_stock import current_stock

# noinspection PyUnusedLocal
# skus = unicode string
"""
PLEASE READ explanation.txt
"""

def checkout(skus: str) -> int:
    """
    Arguments:
    --------------
    skus: str
        A string of all skus in the basket

    Returns:
    --------------
    @return: int
        total value of all items in the basket.
        It will be an int and not a float since the price of every item is a whole number
    """

    total = 0

    # Grouping count by item TC, SC = O(n), O(n)
    basket = dict()
    for sku in skus:

        if sku in current_stock:
            basket[sku] = basket.get(sku, 0) + 1
        else:
            return -1

    for sku, quantity in basket.items(): # TC, SC = O(n), O(n)
        if current_stock[sku].offer:
            return True

    # for sku, quantity in basket.items():  # <SC, TC> = O(n), O(n)
    #
    #     # Accounting for the characters that are not stock
    #     if sku not in prices:
    #         return -1
    #
    #     # Get total value for the deal
    #     if sku in deals:
    #         deal_quantity, price = deals[sku]
    #         total += quantity // deal_quantity * price
    #         quantity %= deal_quantity
    #
    #     # Get value for the items that we have a record for SKU
    #     if sku in prices:
    #         total += quantity * prices[sku]
    #
    # return total
    #
    # from lib.solutions.CHK.product import Product
    # return Product(sku="Z") in Stock().stock






