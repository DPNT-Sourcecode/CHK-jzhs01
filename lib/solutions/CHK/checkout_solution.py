from collections import Counter
from lib.solutions.CHK.stock import Stock
from lib.solutions.CHK.product import Product
# noinspection PyUnusedLocal
# skus = unicode string
"""
    NOTE: I will denote time complexity as TC, and space complexity as SC 
    Initial thoughts:
     - Given a string, we can use collections.Counter to build a hash map of count of every
       item in the basket TC = O(n) and SC = O(n)
     - For every key (product name) we can check for the price and whether there is a promo.

     This is where I think of two approaches (without setting up a DB):

     1. We could build a separate class for "stock" where init would have two dictionaries.
        Dict 1 = prices<sku, price>
        Dict 2 = deals<sku,deal<count, price>>
     Pros:
     - Quick access time: O(1) to access both the the deals and the prices for every SKU
     Cons:
     - Not very OOP

     2. Build a class of "Product" consisting of Product(sku:str, price:int, deal:dict<quantity, price>) 
        Build an additional class "Stock" that would store all of the stock as a list of "Product" classes
     Pros:
     - Very OOP
     - Item can be later reused as a model when DB will be used
     Cons:
     - Runtime for the current question, O(n) to find the product in stock

     I will implement the first approach now for the runtime consideration
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
    for item in skus:
        product = Product(item=item)
        if Stock().check_item_in_stock(product=product):
            basket[product] = basket.get(product, 0) + 1
        else:
            return -1


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