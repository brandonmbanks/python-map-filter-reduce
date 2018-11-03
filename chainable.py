from functools import reduce


class Chainable(object):
    def __init__(self, data):
        self.data = data

    def map(self, fn):
        return Chainable(list(map(fn, self.data)))

    def filter(self, fn):
        return Chainable(list(filter(fn, self.data)))

    def reduce(self, fn):
        return Chainable(reduce(fn, self.data))
