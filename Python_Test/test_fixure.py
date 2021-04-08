import pytest
#py.test test_fixure.py
@pytest.fixture
def x_y_compare():
    return [5,5]
def test_method(x_y_compare):

    assert x_y_compare[0]==x_y_compare[1],"x not equal to y fixure"
    #assert x+1==y, "x equal to y 1 inside learn_test"
    #assert x == y, "x not equal to y"
    #assert x+1 == y+1, "x not equal to y 2"
    #x = x +1
    #assert x_y_compare(x,y),"x not equal to y"
