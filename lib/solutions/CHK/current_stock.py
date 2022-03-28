from lib.solutions.CHK.Models.offer import PriceReduction  # , FreeItem
from lib.solutions.CHK.Models.product import Product
from lib.solutions.CHK.Models.stock import Stock

# Offers
productA_offer_1 = PriceReduction(product_count=5, new_price=200)
productA_offer_2 = PriceReduction(product_count=3, new_price=130)
productB_offer_1 = PriceReduction(product_count=2, new_price=45)
# Products
productA = Product(sku="A", price=50, offer={productA_offer_1, productA_offer_2})
productB = Product(sku="B", price=30,
                   offer={productB_offer_1})
productC = Product(sku="C", price=20)
productD = Product(sku="D", price=15)
productE = Product(sku="E", price=40,
                   # offer={FreeItem(product_count=2, product=productB, count=1)}
                   )

current_stock = {productA, productB, productC, productD, productE}

