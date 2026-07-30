from behave import when, then
from core.add_product import add_product


@when('the user adds a product "{product}"')
def step_add_product(context, product):
    success, msg = add_product(context.store, product)
    context.output = msg


@then('the inventory should contain "{product}"')
def step_inventory_should_contain(context, product):
    assert context.store.get(product) is not None, \
        f'Product "{product}" not found in the inventory'
