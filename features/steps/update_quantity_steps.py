from behave import when, then
from core.update_quantity import update_quantity


@when('the user updates product "{product}" to quantity "{quantity}"')
def step_update_quantity(context, product, quantity):
    success, msg = update_quantity(context.store, product, int(quantity))
    context.output = msg


@then('the inventory should show product "{product}" with quantity "{quantity}"')
def step_inventory_should_show_qty(context, product, quantity):
    p = context.store.get(product)
    assert p is not None, f'Product "{product}" not found'
    assert str(p.quantity) == quantity, \
        f'Expected quantity {quantity}, got {p.quantity}'
