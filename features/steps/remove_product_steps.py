from behave import when, then
from core.remove_product import remove_product


@when('the user removes the product "{product}"')
def step_remove_product(context, product):
    success, msg = remove_product(context.store, product)
    context.output = msg


@then('the inventory should not contain "{product}"')
def step_inventory_should_not_contain(context, product):
    assert context.store.get(product) is None, \
        f'Product "{product}" was found in the inventory but should not be'


@then('the output should be "{message}"')
def step_output_should_be(context, message):
    assert context.output == message, \
        f'Expected "{message}" but got "{context.output}"'
