import functools

from . import simple


__all__ = ()


def check_any(args):

    return args[0] is None


def safe(check = check_any):

    def decorator(function):

        def wrapper(*args, default = '-'):

            if check(args):

                return default

            return function(*args)

        return wrapper

    return decorator


@functools.lru_cache(maxsize = None)
def string():

    @safe()
    def execute(*args):

        return simple.string(*args)

    return execute


@functools.lru_cache(maxsize = None)
def integer():

    @safe()
    def execute(*args):

        return simple.integer(*args)

    return execute


@functools.lru_cache(maxsize = None)
def decimal(point = 3):

    @safe()
    def execute(*args):

        return simple.decimal(point, *args)

    return execute


@functools.lru_cache(maxsize = None)
def boolean(options = ('inactive', 'active')):

    @safe()
    def execute(*args):

        return simple.boolean(options, *args)

    return execute


def check_array(args):

    return not args[0]


@functools.lru_cache(maxsize = None)
def array(sub, join = ', '.join):

    @safe(check_array)
    def execute(*args):

        return simple.array(join, sub, *args)

    return execute
