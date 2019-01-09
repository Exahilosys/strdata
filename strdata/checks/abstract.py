import operator


__all__ = ()


def range(error, lower, left, upper, right, value, bounds = ('([', ')]')):

    sides = (left, right)

    operators = (operator.lt, operator.le)

    former, latter = map(operators.__getitem__, sides)

    if former(lower, value) and latter(value, upper):

        return

    left, right = (bound[side] for side, bound in zip(sides, bounds))

    message = f'{left}{lower}, {upper}{right}'

    raise error(message)


def include(error, white, store, value, types = ('black', 'white')):

    predicate = value in store

    if predicate if white else not predicate:

        return

    message = types[white]

    raise error(message)
