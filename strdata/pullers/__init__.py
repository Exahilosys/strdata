import functools

from . import abstract


__all__ = ()


def _safe(function):

    def wrapper(*args, default = '-'):

        value = args[-1]

        if value is None:

            return default

        return function(*args)

    return wrapper


@functools.lru_cache(maxsize = None)
def string():

    @_safe
    def execute(*args):

        return abstract.string(*args)

    return execute


@functools.lru_cache(maxsize = None)
def integer():

    @_safe
    def execute(*args):

        return abstract.integer(*args)

    return execute


@functools.lru_cache(maxsize = None)
def decimal(precision = 3):

    @_safe
    def execute(*args):

        return abstract.decimal(precision, *args)

    return execute


@functools.lru_cache(maxsize = None)
def boolean(options = ('inactive', 'active')):

    @_safe
    def execute(*args):

        return abstract.boolean(options, *args)

    return execute


@functools.lru_cache(maxsize = None)
def array(sub, join = ', '.join):

    @_safe
    def execute(*args):

        return abstract.array(join, sub, *args)

    return execute
