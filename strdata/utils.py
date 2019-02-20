import asyncio
import functools

from . import parsers


__all__ = ()


reject = (None,)


skip = reject.__contains__


def apply(first, *checks, skip = skip):

    def execute(*args):

        value = first(*args)

        if not skip or not skip(value):

            for check in checks:

                check(value)

        return value

    return execute
