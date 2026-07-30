def remove_product(store, name):
    if name not in store:
        return False, f"Product '{name}' was not found"
    store.remove(name)
    return True, f"Product '{name}' was removed"
