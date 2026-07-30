def search_product(store, term):
    return [p for p in store.all() if term.lower() in p.name.lower()]
