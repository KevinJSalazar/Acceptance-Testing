def list_products(store):
    products = store.all()
    if not products:
        return "No products in inventory."
    lines = ["Products:"]
    for p in products:
        lines.append(f"- {p.name}")
    return "\n".join(lines)
