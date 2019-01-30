import functools

from . import abstract


__all__ = ()


def safe(function):

    def wrapper(*args, default = '-'):

        if args[0] is None:

            return default

        return function(*args)

    return wrapper


@functools.lru_cache(maxsize = None)
def string():

    @safe
    def execute(*args):

        return abstract.string(*args)

    return execute


@functools.lru_cache(maxsize = None)
def integer():

    @safe
    def execute(*args):

        return abstract.integer(*args)

    return execute


@functools.lru_cache(maxsize = None)
def decimal(point = 3):

    @safe
    def execute(*args):

        return abstract.decimal(point, *args)

    return execute


@functools.lru_cache(maxsize = None)
def boolean(options = ('inactive', 'active')):

    @safe
    def execute(*args):

        return abstract.boolean(options, *args)

    return execute


@functools.lru_cache(maxsize = None)
def array(sub, join = ', '.join):

    @safe
    def execute(*args):

        return abstract.array(join, sub, *args)

    return execute
