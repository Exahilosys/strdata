import stroke


__all__ = ()


def pair(add, set, argument):

    bundles = stroke.parse.split(argument, add)

    bundles = stroke.parse.clean(bundles)

    for bundle in bundles:

        assets = stroke.parse.split(bundle, set)

        assets = stroke.parse.clean(assets, empty = False)

        key = next(assets)

        if not key:

            continue

        try:

            value = next(assets)

        except StopIteration:

            entry = (key,)

        else:

            entry = (key, value)

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
