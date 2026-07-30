from behave import given
from core.add_product import add_product


@given('the inventory is empty')
def step_inventory_empty(context):
    pass


@given('the inventory contains products:')
def step_inventory_contains_products(context):
    for row in context.table:
        name = row["Product"]
        qty = int(row.get("Quantity", 0)) if row.get("Quantity") else 0
        add_product(context.store, name, quantity=qty)
