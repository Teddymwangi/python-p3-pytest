from lib.not_none_functions import add_one

def test_add_one():
    assert add_one(1) == 2

def test_add_one_with_none():
    assert add_one(None) is None
