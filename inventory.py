from core.store import Store
from core.add_product import add_product
from core.list_products import list_products
from core.update_quantity import update_quantity
from core.remove_product import remove_product
from core.search_product import search_product


def main():
    store = Store()
    while True:
        print("\n--- Inventory Manager ---")
        print("1. Add product")
        print("2. List products")
        print("3. Update quantity")
        print("4. Remove product")
        print("5. Search product")
        print("6. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            name = input("Product name: ").strip()
            qty = int(input("Quantity: ").strip())
            price = float(input("Price: ").strip())
            cat = input("Category: ").strip() or "General"
            success, msg = add_product(store, name, qty, price, cat)
            print(msg)
        elif choice == "2":
            print(list_products(store))
        elif choice == "3":
            name = input("Product name: ").strip()
            qty = int(input("New quantity: ").strip())
            success, msg = update_quantity(store, name, qty)
            print(msg)
        elif choice == "4":
            name = input("Product name: ").strip()
            success, msg = remove_product(store, name)
            print(msg)
        elif choice == "5":
            term = input("Search term: ").strip()
            results = search_product(store, term)
            if not results:
                print(f"No products found matching '{term}'")
            else:
                print("Results:")
                for p in results:
                    print(f"- {p.name} (Qty: {p.quantity}, Price: ${p.price:.2f}, Category: {p.category})")
        elif choice == "6":
            break


if __name__ == "__main__":
    main()
