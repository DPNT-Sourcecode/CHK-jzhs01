class Product:
    def __init__(self, sku: str, price: int = None, offer: dict = None):
        self.sku = sku
        self.price = price
        self.offer = offer

