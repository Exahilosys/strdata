import math


__all__ = ()


def string(join, state, values):

    final = join(values)

    return final


def integer(error, state, values):

    value = values[0]

    try:

        final = int(value)

    except ValueError:

        raise error(value)

    return final


def decimal(error, state, values):

    value = values[0]

    try:

        final = float(value)

    except ValueError:

        raise error(value)

    if not math.isfinite(final):

        raise error(value)

    return final


def boolean(options, error, state, values):

    value = values[0].lower()

    for final, option in options:

        if not value in option:

            continue

        break

    else:

        raise error(value)

    return final


def array(split, sub, state, values):

    state = set(state)

    stores = split(values)

    handles = (state.add, state.remove)

    for store, handle in zip(stores, handles):

        for values in store:

            value = sub(values)

            try:

                handle(value)

            except KeyError:

                continue

    final = list(state)

    return final
