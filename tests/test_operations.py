from src.math_operations import add, sub

def test_dd():
    assert add(2,3) == 5
    assert add(-1, 1) == 0

def test_sub():
    assert sub(-1, 5) == 4
    assert sub(5, -2) == 3