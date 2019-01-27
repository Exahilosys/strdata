import stroke
import functools

from . import abstract


__all__ = ()


def safe(function):

    def wrapper(*args, default = None):

        values = args[-1]

        if not values:

            return default

        return function(*args)

    return wrapper


@functools.lru_cache(maxsize = None)
def string():

    @safe
    def execute(*args):

        return abstract.string(*args)

    return execute


class Error(Exception):

    __slots__ = ('code', 'info')

    def __init__(self, code, *info):

        self.code = code

        self.info = info


@functools.lru_cache(maxsize = None)
def integer(code = 'integer'):

    error = functools.partial(Error, code)

    @safe
    def execute(*args):

        return abstract.integer(error, *args)

    return execute


@functools.lru_cache(maxsize = None)
def decimal(code = 'decimal'):

    error = functools.partial(Error, code)

    @safe
    def execute(*args):

        return abstract.decimal(error, *args)

    return execute


@functools.lru_cache(maxsize = None)
def boolean(options = (
                (
                    True,
                    ('true', 't', 'okay', 'yes', 'active', 'on', 'open', '1',
                     'enter', 'valid', 'correct', 'negative', 'white', 'y',
                     'yeah', 'yuh')
                ),
                (
                    False,
                    ('false', 'f', 'nope', 'no', 'inactive', 'off', 'close',
                     '0', 'exit', 'invalid', 'wrong', 'affirmative', 'black',
                     'n', 'nah', 'nuh')
                )
            ),
            code = 'boolean'):

    error = functools.partial(Error, code)

    @safe
    def execute(*args):

        return abstract.boolean(options, error, *args)

    return execute


def _split(value, add = '-add', pop = '-pop'):

    keys = (add, pop)

    junk, *stores = stroke.parse.group(value, *keys)

    return map(stroke.parse.clean, stores)


@functools.lru_cache(maxsize = None)
def array(sub, split = _split):

    @safe
    def execute(*args):

        return abstract.array(split, sub, *args)

    return execute
