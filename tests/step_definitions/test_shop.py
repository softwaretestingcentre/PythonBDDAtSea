import pytest

from pytest_bdd import scenarios, given, then, parsers

from tests.ui_layer import shopping

from pytest_check import check

scenarios('../features/shop.feature')

@pytest.fixture
def basket():
    return {"contents": []}

@given("Betty adds items to her basket")
def add_to_basket(basket, datatable):
    basket["contents"] = []
    for row in datatable[1:]:
        basket["contents"].append(row[0])


@then(parsers.parse("she can see her basket contains only {string}"))
def confirm_basket(basket, string):
    items = [string[1:-1]]
    check.equal(items, basket["contents"])
