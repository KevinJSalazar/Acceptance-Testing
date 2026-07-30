from core.store import Product


def add_product(store, name, quantity=0, price=0.0, category="General"):
    if name in store:
        return False, f"Product '{name}' already exists"
    store.add(Product(name, quantity, price, category))
    return True, f"Product '{name}' added"
