from chainable import Chainable


def add_1(x):
    return x + 1


def is_odd(x):
    return x % 2 != 0


def multiply(x, y):
    return x * y


def test_map_returns_correct_output():
    chainable = Chainable([1, 2, 3])
    assert [2, 3, 4] == chainable.map(add_1).data


def test_filter():
    chainable = Chainable([1, 2, 3])
    assert [1, 3] == chainable.filter(is_odd).data


def test_it_can_chain_map_and_filter():
    chainable = Chainable([1, 2, 3])
    assert [3] == chainable.map(add_1).filter(is_odd).data


def test_reduce():
    chainable = Chainable([1, 2, 3])
    assert 6 == chainable.reduce(multiply).data
