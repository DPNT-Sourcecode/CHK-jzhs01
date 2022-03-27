class Product:
    def __init__(self, sku: str, price: int, offer: dict = None):
        self.sku = sku
        self.price = price
        self.offer = offer

