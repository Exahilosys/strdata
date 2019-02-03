

__all__ = ()


def string(value):

    final = value

    return final


def integer(value):

    final = str(value)

    return final


def decimal(precision, value):

    elegant = round(value, precision)

    final = str(elegant)

    return final


def boolean(options, value):

    final = options[value]

    return final


def array(join, sub, value):

    elegant = map(sub, value)

    final = join(elegant)

    return final
