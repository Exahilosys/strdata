
from . import abstract


__all__ = ()


def pair(argument, add = '-and', set = '-set'):

    entries = abstract.pair(add, set, argument)

    stores = ([], [])

    for entry in entries:

        key, *values = entry

        organise = bool(values)

        stores[organise].append(entry)

    return stores


def find(values, argument):

    return abstract.find(values, argument)


class Error(Exception):

    __slots__ = ('field',)

    def __init__(self, field):

        self.field = field


def move(assets, argument, get, find = find):

    return abstract.move(find, Error, assets, argument, get)
