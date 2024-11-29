import cart

from S37_Unittesting_Python.shopping_cart.cart import ShoppingCart
import pytest
cart = ShoppingCart()
def test_add_items():

    cart.add_items("apple",2)
    assert  cart.get_item_count("apple") == 2
    assert  cart.get_total_items() ==2


def test_remove_items():
    cart = ShoppingCart()
    cart.add_items("apple",3)
    cart.remove_items("apple",2)
    assert  cart.get_item_count("apple") == 1
    assert  cart.get_total_items() ==1

def test_get_cart_items():

    cart.add_items("apple",3)
    cart.add_items("mango",4)
    items = cart.get_cart_items()
    assert "apple" in items
    assert "mango" in items
def test_clear_cart():
    cart.add_items("banana",3)
    cart.clear_cart()
    assert cart.get_total_items()==0
    assert cart.get_cart_items()  ==[]
