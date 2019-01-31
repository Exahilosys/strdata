import functools

from . import abstract


__all__ = ()


class Error(Exception):

    __slots__ = ('code', 'info')

    def __init__(self, code, *info):

        self.code = code

        self.info = info


@functools.lru_cache(maxsize = None)
def range(lower, upper, code = 'range', left = True, right = True):

    error = functools.partial(Error, code)

    def execute(*args):

        return abstract.range(error, lower, left, upper, right, *args)

    return execute


def include(store, white = True, code = 'include'):

    error = functools.partial(Error, code)

    def execute(*args):

        return abstract.include(error, white, store, *args)

    return execute
