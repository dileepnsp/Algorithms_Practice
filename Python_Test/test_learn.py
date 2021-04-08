import pytest
#py.test -m
# py.test -m set1
# py.test -m set2
@pytest.mark.set1
def test_method1():
    x=5
    y=6
    assert x+1==y, "x equal to y 1 inside test_learn in set1"
    #assert x == y, "x not equal to y"
    #assert x+1 == y+1, "x not equal to y 2"
    #x = x +1
    #assert x_y_compare(x,y),"x not equal to y"
@pytest.mark.set2
def test_method2():
    x=5
    y=6
    assert x+1==y, "x equal to y 1 inside test_learn in set2"