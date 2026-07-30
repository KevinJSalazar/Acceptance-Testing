class Product:
    def __init__(self, name, quantity=0, price=0.0, category="General"):
        self.name = name
        self.quantity = quantity
        self.price = price
        self.category = category


class Store:
    def __init__(self):
        self._products = {}

    def add(self, product):
        self._products[product.name] = product

    def get(self, name):
        return self._products.get(name)

    def remove(self, name):
        return self._products.pop(name, None)

    def all(self):
        return list(self._products.values())

    def __contains__(self, name):
        return name in self._products

    def __len__(self):
        return len(self._products)
