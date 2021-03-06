## Usage
```py
import strdata
import functools

reject = (None,)

skip = reject.__contains__

types = ('feline', 'canis')

pushers = {
    # what the asset is going to be looked up by
    'name': (
        # what the unparsed value will be requested as
        'name',
        # what the parsed value will be set against
        'name',
        # the function used for transforming;
        # utils.apply uses the result of the first
        # function in the succeeding ones for validating it
        strdata.utils.apply(
            strdata.pushers.string(),
            strdata.utils.apply(
                len,
                strdata.checks.range(2, 32, left = False)
            )
        )
    ),
    'alive': (
        'alive',
        'alive',
        # raw pushers for no validation
        strdata.pushers.boolean()
    ),
    'gold coins': (
        'gold_coins',
        'gold_coins',
        strdata.utils.apply(
            strdata.pushers.decimal(),
            strdata.checks.range(0, 6.5)
        )
    ),
    'interests': (
        'likes',
        'likes',
        strdata.utils.apply(
            strdata.pushers.array(
                strdata.utils.apply(
                    functools.partial(
                        strdata.pushers.string(),
                        # we have to do this because
                        # pushers require to know the
                        # previous state of the value
                        # they parse (even if sometimes
                        # it's not really used for anything);
                        # since we can't schemanticaly derive
                        # this value from an array, we have
                        # to explicitely pass it; (pushers.string
                        # doesn't use the state like most pushers)
                        None
                    ),
                    strdata.utils.apply(
                        len,
                        strdata.checks.range(4, 16)
                    )
                )
            ),
            strdata.utils.apply(
                len,
                strdata.checks.range(1, 6)
            )
        )
    ),
    'type': (
        'type',
        'type',
        strdata.utils.apply(
            strdata.pushers.string(),
            strdata.checks.include(types)
        )
    ),
    'status': (
        'status',
        'status',
        strdata.utils.apply(
            strdata.pushers.string(),
            strdata.utils.apply(
                len,
                strdata.checks.range(4, 16)
            )
        )
    )
}

pullers = {
    'name': (
        'name',
        'nick',
        # pullers need no validation;
        # their job is to convert any data type to str
        strdata.pullers.string(),
    ),
    'gold coins': (
        'gold_coins',
        'gold coins',
        strdata.pullers.decimal(point = 2)
    ),
    'type': (
        'type',
        'kind',
        strdata.pullers.string()
    ),
    'alive': (
        'alive',
        'alive',
        strdata.pullers.boolean(options = ('negative', 'positive'))
    ),
    'likes': (
        'likes',
        'interests',
        strdata.pullers.array(strdata.pullers.string())
    ),
    'status': (
        'status',
        'status',
        strdata.pullers.string()
    )
}

data = {
    'name': 'kitty',
    'type': 'canis',
    'alive': True,
    'gold_coins': 4.234381,
    'likes': ['pats', 'meows'],
    'status': 'angry'
}

test = (
    'name '
    '-and alive -set f '
    '-and type -set feline '
    '-and interests -set -add purrs -pop meows -add yarn '
    '-and gold coins -set 5.234 '
    '-and status -set '
)

print(test)

# single is for display; pairs is for update
single, pairs = strdata.parsers.pair(test)

extras, junk = zip(*pairs)

# here we "pretend" our pair's keys have
# also been passed with no -set to let the
# program know we are also seeking to view
# those (ie. let pullers parse and return)
single.extend((extra,) for extra in extras)

# need a getter
get = data.__getitem__

# this is our new data
result = strdata.parsers.move(pushers, get, pairs)

print('old: ', data)

# update our store with it
data.update(result)

print('new: ', data)

# this is our new data, but all values are strings
result = strdata.parsers.move(pullers, get, single)

# most results are generators
# yielding key-value tuple pairs
final = dict(result)

print('show:', final)
```
Play around with the test and checks values.  
There are push and check errors that can be raised!
## Installing
```
python3 -m pip install strdata
```
