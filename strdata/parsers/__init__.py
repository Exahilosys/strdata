
from . import simple


__all__ = ()


class Error(Exception):

    __slots__ = ('field',)

    def __init__(self, field):

        self.field = field


def pair(argument, add = '-and', set = '-set'):

    entries = simple.pair(add, set, argument)

    stores = ([], [])

    for entry in entries:

        key, *values = entry

        organise = bool(values)

        stores[organise].append(entry)

    return stores


def find(values, argument):

    return simple.find(values, argument)


def move(assets, argument, get, find = find):

    return simple.move(find, Error, assets, argument, get)
