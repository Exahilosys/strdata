import stroke
import functools

from . import abstract


__all__ = ()


class Error(Exception):

    __slots__ = ('code', 'info')

    def __init__(self, code, *info):

        self.code = code

        self.info = info


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

        value = abstract.string(*args)

        return value

    return execute


@functools.lru_cache(maxsize = None)
def integer(code = 'integer'):

    error = functools.partial(Error, code)

    @safe
    def execute(*args):

        value = abstract.integer(error, *args)

        return value

    return execute


@functools.lru_cache(maxsize = None)
def decimal(code = 'decimal', point = 3):

    error = functools.partial(Error, code)

    @safe
    def execute(*args):

        value = abstract.decimal(error, *args)

        if not point is None:

            value = round(value, point)

        return value

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

        value = abstract.boolean(options, error, *args)

        return value

    return execute


def _split(value, add = '-add', pop = '-pop'):

    keys = (add, pop)

    junk, *stores = stroke.parse.group(value, *keys)

    return map(stroke.parse.clean, stores)


@functools.lru_cache(maxsize = None)
def array(sub, split = _split):

    @safe
    def execute(*args):

        value = abstract.array(split, sub, *args)

        return value

    return execute
