from behave import when, then
from core.list_products import list_products


@when('the user lists all products')
def step_list_products(context):
    context.output = list_products(context.store)


@then('the output should contain:')
def step_output_should_contain(context):
    expected = context.text.strip()
    assert context.output.strip() == expected, \
        f'Expected:\n{expected}\n\nGot:\n{context.output.strip()}'
