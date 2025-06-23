import pytest

from pytest_bdd import scenarios, given, then

from tests.ui_layer import shopping

from pytest_check import check

scenarios('../features/shop.feature')

@pytest.fixture
def basket():
    return "Unusable Security"

def test_shop():
    pass

@given("Betty adds items to her basket")
def _(datatable):
    for row in datatable:
        shopping.add_to_basket(row)


@then("she can see her basket contains only her chosen items")
def confirm_basket(item):
    return check.equal(item, shopping.get_basket_contents())