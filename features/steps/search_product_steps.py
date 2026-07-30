from behave import when, then
from core.search_product import search_product


@when('the user searches for "{term}"')
def step_search_product(context, term):
    context.search_results = search_product(context.store, term)


@then('the search results should contain "{product}"')
def step_search_results_contain(context, product):
    names = [p.name for p in context.search_results]
    assert product in names, \
        f'Search results should contain "{product}" but got {names}'


@then('the search results should not contain "{product}"')
def step_search_results_not_contain(context, product):
    names = [p.name for p in context.search_results]
    assert product not in names, \
        f'Search results should not contain "{product}" but got {names}'
