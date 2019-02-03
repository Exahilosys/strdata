import math


__all__ = ()


def string(value):

    final = value

    return final


def integer(error, value):

    try:

        final = int(value)

    except ValueError:

        raise error(value)

    return final


def decimal(error, value):

    try:

        final = float(value)

    except ValueError:

        raise error(value)

    if not math.isfinite(final):

        raise error(value)

    return final


def boolean(options, error, value):

    value = value.lower()

    for final, option in options:

        if not value in option:

            continue

        break

    else:

        raise error(value)

    return final


def array(split, sub, state, value):

    state = set(state)

    stores = split(value)

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
