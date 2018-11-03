from functools import reduce


class Chainable(object):
    def __init__(self, data):
        self.data = data

    def map(self, fn):
        self.data = list(map(lambda x: fn(x), self.data))
        return self

    def filter(self, fn):
        self.data = list(filter(lambda x: fn(x), self.data))
        return self

    def reduce(self, fn):
        self.data = reduce(lambda x, acc: fn(x, acc), self.data)
        return self
