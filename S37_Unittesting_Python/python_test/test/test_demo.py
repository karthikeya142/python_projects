from S37_Unittesting_Python.python_test.app.demo import add,sub,mul,div,discount_season
import pytest

@pytest.mark.skip("skipping this task for some reasion")
def test_add():
    assert add(10,20) == 30
#writing multiple tests
@pytest.mark.skipif(discount_season(),reason ="skipping this because discount season is on")
def test_mul():
    assert mul(10, 20) == 200
def test_sub():
    assert sub(10, 20) == -10
def test_div():
    assert div(100, 20) == 5

    #case for asserting exception
    with pytest.raises(ValueError):
        div(4,0)
