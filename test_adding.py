import pytest

from adding import add, add_with_exception

def test_simple_add():
    assert add(1, 2) == 3
    assert add(1, 1) == 2
    assert add(105, 321) == 426

def test_invalid_add():
    assert add(-5, 5) is None

def test_invalid_add_exception():
    with pytest.raises(ValueError):
        assert add_with_exception(-5, 5)
