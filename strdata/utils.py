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


def aiodata(value, name, cache = True):

    if cache:

        async def get(key):

            data = value.cache[name].get(*key)

            return data.__get__

    else:

        async def get(key):

            (data, *junk) = await value.get(name, *key)

            return data.__get__

    async def update(key, data):

        (data, *junk) = await value.update(name, *key, **data)

        return data.__get__

    return get, update
