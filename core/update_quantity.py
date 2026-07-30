def update_quantity(store, name, new_quantity):
    product = store.get(name)
    if product is None:
        return False, f"Product '{name}' was not found"
    product.quantity = new_quantity
    return True, f"Product '{name}' quantity updated to {new_quantity}"
