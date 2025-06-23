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


@then(parsers.parse('she can see her basket contains only "{item}"'))
def confirm_basket(basket, item):
    items = [item]
    return check.equal(items, basket["contents"])
