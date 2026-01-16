from src.math_operations import add, sub, mul, div

def test_add():
    assert add(2,3) == 5
    assert add(5,5) == 10

def test_sub():
        assert sub(2,3) == -1
        assert sub(5,5) == 0
        assert sub(10,3) == 7

def test_mul():
    assert mul(2,3) == 6
    assert mul(5,5) == 25
    assert mul(0,10) == 0   

def test_div():
    assert div(6,3) == 2
    assert div(10,2) == 5
    try:
        div(5,0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."