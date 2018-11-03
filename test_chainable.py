from chainable import Chainable


def add_1(x):
    return x + 1


def is_odd(x):
    return x % 2 != 0


def multiply(x, y):
    return x * y


def test_map():
    chainable = Chainable([1, 2, 3])
    assert [2, 3, 4] == chainable.map(lambda x: x + 1).data


def test_map_using_function():
    chainable = Chainable([1, 2, 3])
    assert [2, 3, 4] == chainable.map(add_1).data


def test_filter():
    chainable = Chainable([1, 2, 3])
    assert [1, 3] == chainable.filter(lambda x: x % 2 != 0).data


def test_filter_with_function():
    chainable = Chainable([1, 2, 3])
    assert [1, 3] == chainable.filter(is_odd).data


def test_it_can_chain_map_and_filter():
    chainable = Chainable([1, 2, 3])
    assert [3] == chainable.map(add_1).filter(is_odd).data


def test_reduce():
    chainable = Chainable([1, 2, 3])
    assert 6 == chainable.reduce(lambda x, acc: x + acc).data


def test_reduce_with_function():
    chainable = Chainable([1, 2, 3])
    assert 6 == chainable.reduce(multiply).data


def test_map_should_not_mutate_the_instance():
    chainable = Chainable([1, 2, 3])
    chainable.map(lambda x: x + 1)
    assert [1, 2, 3] == chainable.data
    chainable = chainable.map(lambda x: x + 1)
    assert [2, 3, 4] == chainable.data


def test_filter_should_not_mutate_the_instance():
    chainable = Chainable([1, 2, 3])
    chainable.filter(lambda x: x % 2 != 0)
    assert [1, 2, 3] == chainable.data
    chainable = chainable.filter(lambda x: x % 2 != 0)
    assert [1, 3] == chainable.data


def test_reduce_should_not_mutate_the_instance():
    chainable = Chainable([1, 2, 3])
    chainable.reduce(lambda x, acc: x + acc)
    assert [1, 2, 3] == chainable.data
    chainable = chainable.reduce(lambda x, acc: x + acc)
    assert 6 == chainable.data
