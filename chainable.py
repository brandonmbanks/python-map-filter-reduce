from functools import reduce


class Chainable(object):
    def __init__(self, data):
        self.data = data

    def _map(self, fn):
        self.data = list(map(lambda x: fn(x), self.data))
        return self

    def _filter(self, fn):
        self.data = list(filter(lambda x: fn(x), self.data))
        return self

    def _reduce(self, fn):
        self.data = reduce(lambda x, acc: fn(x, acc), self.data)
        return self
