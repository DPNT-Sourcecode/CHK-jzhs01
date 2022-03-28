from lib.solutions.CHK.Models.offer import PriceReduction, FreeItem
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

    for sku, quantity in basket.items():  # TC, SC = O(n), O(n)
        # Offer Available
        product = current_stock[sku]
        if product.offer:
            for offer in product.offer:

                # Case when price reduction offer
                if offer is isinstance(offer, PriceReduction):
                    product_count, new_price = offer.product_count, offer.new_price
                    total += quantity // product_count * new_price
                    quantity %= product_count

                # Case when free item offer
                if offer is isinstance(offer, FreeItem):
                    product_count, free_product, count = offer.product_count, offer.product, count
                    skus.append([free_product.sku] * quantity // product_count * count)

        total += quantity * product.price

    return total

