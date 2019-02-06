import stroke
import functools

from . import simple


__all__ = ()


class Error(Exception):

    __slots__ = ('code', 'info')

    def __init__(self, code, *info):

        self.code = code

        self.info = info


def check_any(args):

    return not args[1]


def safe(check = check_any):

    def decorator(function):

        def wrapper(*args, default = None):

            if check(args):

                return default

            return function(*args)

        return wrapper

    return decorator


@functools.lru_cache(maxsize = None)
def string():

    @safe()
    def execute(state, *args):

        value = simple.string(*args)

        return value

    return execute


@functools.lru_cache(maxsize = None)
def integer(code = 'integer'):

    error = functools.partial(Error, code)

    @safe()
    def execute(state, *args):

        value = simple.integer(error, *args)

        return value

    return execute


@functools.lru_cache(maxsize = None)
def decimal(code = 'decimal', point = 3):

    error = functools.partial(Error, code)

    @safe()
    def execute(state, *args):

        value = simple.decimal(error, *args)

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

    @safe()
    def execute(state, *args):

        value = simple.boolean(options, error, *args)

        return value

    return execute


def _split(value, add = '-add', pop = '-pop'):

    keys = (add, pop)

    junk, *stores = stroke.parse.group(value, *keys)

    return map(stroke.parse.clean, stores)


@functools.lru_cache(maxsize = None)
def array(sub, split = _split):

    @safe()
    def execute(*args):

        value = simple.array(split, sub, *args)

        return value

    return execute
