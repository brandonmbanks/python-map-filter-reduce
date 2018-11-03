# python-map-filter-reduce
---
The goal is to make map, filter, and reduce easier to write and use in Python.

Currently `map`, `filter`, and `reduce` syntax can be messy and is difficult to chain.

```python
>>> list(map(lambda x: x + 2, list(filter(lambda x: x % 2 != 0, [1, 2, 3]))))
[3, 5]
```

### `Chainable`
---
By passing a `list` to the `Chainable` constructor you can call `map`, `filter`, and `reduce` on the `Chainable` instance.
The list can be accessed through the `data` property on the `Chainable` instance.
```
chainable = Chainable([1, 2, 3])
chainable.data # [1, 2, 3]
```
All `Chainable` functions return a `Chainable` instance. This allows the calls to be chained.
```python
chainable = Chainable([1, 2, 3])

ch = chainable.filter(lambda x: x % 2 != 0)
ch.data # [1, 3]

ch = chainable.filter(lambda x: x % 2 != 0).map(lambda x: x * 2)
ch.data # [2, 6]
```

You can also pass defined functions to `Chainable` functions.
```python
def add_1(x):
    return x + 1

chainable = Chainable([1, 2, 3])
chainable = chainable.map(add_1)
chainable.data # [2, 3, 4]
```

**Note**
`Chainable` functions do not mutate the instance but return a new `Chainable` instance.

### Install
---
[Pipenv](https://github.com/pypa/pipenv) is used to manage dependencies.
Install using `homebrew` on Mac
```bash
brew install pipenv
```
Or refer to [Pipenv docs](https://pipenv.readthedocs.io/en/latest/install) if you don't want to use `homebrew` or aren't on MacOS.

**Install dependencies**
```bash
pipenv install
```

**Run tests**
```bash
pipenv run pytest
```

### Todos
---
- install through pip
- add more functionality

### License
---
This project is licensed under the MIT License

