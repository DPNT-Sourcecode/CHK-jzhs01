class Product:
    def __init__(self, sku: str, price: int = None, offer: dict = None):
        self.sku = sku
        self.price = price
        self.offer = offer

    def __hash__(self):
        return hash((self.sku, self.price, self.offer))

    def __eq__(self, product):
        return self.sku == product.sku
