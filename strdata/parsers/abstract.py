import stroke


__all__ = ()


def pair(add, set, argument, parse = tuple):

    bundles = stroke.parse.split(argument, add)

    for bundle in bundles:

        key, values = stroke.parse.group(bundle, set)

        against = values[:1]

        entry = (key, *against)

        yield entry


def find(values, argument, lenient = True):

    key = str.lower if lenient else None

    if key:

        argument = key(argument)

    bundles = stroke.search.specific(values, argument, key = key)

    value = stroke.search.lead(bundles)

    return value


def move(find, error, assets, get, arguments):

    fields = assets.keys()

    for argument, *extra in arguments:

        field = find(fields, argument)

        key, identity, parse = assets[field]

        value = get(key)

        try:

            final = parse(value, *extra)

        except Exception as _error:

            raise error(field) from _error

        yield (identity, final)
