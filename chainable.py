from functools import reduce


class Chainable(object):
    def __init__(self, data):
        self.data = data

    def map(self, fn):
        self.data = list(map(fn, self.data))
        return self

    def filter(self, fn):
        self.data = list(filter(fn, self.data))
        return self

    def reduce(self, fn):
        self.data = reduce(fn, self.data)
        return self
