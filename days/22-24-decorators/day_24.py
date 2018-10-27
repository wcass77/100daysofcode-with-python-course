"""
Uses a decorator to create a very general cache: It creates a tuple from the arguments
and stores the results of each run in a dictionary.
"""

from functools import wraps


def cache(func):
    cache_ = {}

    @wraps(func)
    def wrapped(*args, **kwargs):
        param = (args, tuple(kwargs.items()))
        if param not in cache_:
            cache_[param] = func(*args, **kwargs)
        return cache_[param]

    return wrapped


@cache
def add_2(x, y):
    return x + y


if __name__ == "__main__":
    print(add_2(1, 1))
    print(add_2(1, 1))
    print(add_2(2, 2))
