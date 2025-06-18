# dictflat

## Documentation

### Change/Replace value

How: Use init function "`change`" parameter.

`change` parameter signature:

```python
Optional[Dict[str, Callable]]
```

By default, no values are modified.

The dictionnary key is the future field name.

The `Callable` dictionnary value signature is:

```python
def fct_name(fieldname: str, value: Any) -> Any:
```

#### Change a string by another string

Example with a date in a string to another string:

```python
DictFlat(
    root_key="rk",
    fct_build_id=fct_build_id,
    change={
        "rk.birth.date": fix_date,
    }
).flat(
    d={
        "name": "John",
        "pers_id": 12,
        "birth": {
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA"
            },
            "date": "10/06/1976 01:10:35"
        }
    }
)
```

Result:

```json
{
    "rk": [
        {
            "__id": "2a02485bc672ee47",
            "pers_id": 12,
            "name": "John"
        }
    ],
    "rk.birth": [
        {
            "__id": "034b3cd2487b9d17",
            "__ref__rk": "2a02485bc672ee47",
            "date": "1976-06-10T01:10:35",
        }
    ],
    "rk.birth.address": [
        {
            "__id": "4f49da4f0b4df789",
            "__ref__rk.birth": "034b3cd2487b9d17",
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA"
        }
    ]
}
```

#### Change a string by a dictionnary

Example with a date in a string to a dictionnary where date and time are separated:

```python
DictFlat(
    root_key="rk",
    fct_build_id=fct_build_id,
    change={
        "rk.birth.date": date2dict,
    }
).flat(
    d={
        "name": "John",
        "pers_id": 12,
        "birth": {
            "address": {
                "street": "123 Main St",
                "city": "Anytown",
                "state": "CA"
            },
            "date": "10/06/1976 01:10:35"
        }
    }
)
```

Result:

```json
assert df == {
    "rk": [
        {
            "__id": "2a02485bc672ee47",
            "pers_id": 12,
            "name": "John"
        }
    ],
    "rk.birth": [
        {
            "__id": "034b3cd2487b9d17",
            "__ref__rk": "2a02485bc672ee47",
        }
    ],
    "rk.birth.date": [
        {
            "__id": "71d9d6cb90bcd168",
            "__ref__rk.birth": "034b3cd2487b9d17",
            "date": "1976-06-10",
            "time": "01:10:35",
        }
    ],
    "rk.birth.address": [
        {
            "__id": "4f49da4f0b4df789",
            "__ref__rk.birth": "034b3cd2487b9d17",
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA"
        }
    ]
}
```

#### Use context in your own function to change values

How: Same first example, use init function "`change`" parameter.

The `Callable` dictionnary value signature is:

```python
def fct_name(fieldname: str, value: Any, context:Dict) -> Any:
```

The `context` parameter is a dictionnary who contains three keys:

* `CONTEXT_DEPTH: Final[str] = '__depth'`
  * The depth of the current dictionnary in the global original dictionnary
* `CONTEXT_PATH: Final[str] = '__path'`
  * The path of the current dictionnary in the global original dictionnary
* `CONTEXT_ELEMENT: Final[str] = '__element'`
  * The current field name in the current dictionnary in the global original dictionnary

You could add any other keys during init step with optional `context` parameter.

An example:

With `fix_street` function example:

```python
def fix_street(fieldname: str, value: str, context: Dict) -> str:
    for k in context['street']:
        value = value.replace(k, context['street'][k])
    return value
```

The code :

```python
DictFlat(
    root_key='rk',
    fct_build_id=fct_build_id,
    change={
        'rk.birth.date': fix_date,
        'rk.birth.address.street': fix_street,
    },
    context={
        'street': {
            "St": "Street"
        }
    }
).flat(
    d={
        'name': 'John',
        'pers_id': 12,
        'birth': {
            'address': {
                'street': '123 Main St',
                'city': 'Anytown',
                'state': 'CA'
            },
            'date': '10/06/1976 01:10:35'
        }
    }
)
```

Result:

```json
{
    "rk": [
        {
            "__id": "2a02485bc672ee47",
            "pers_id": 12,
            "name": "John"
        }
    ],
    "rk.birth": [
        {
            "__id": "034b3cd2487b9d17",
            "__ref__rk": "2a02485bc672ee47",
            "date": "1976-06-10T01:10:35",
        }
    ],
    "rk.birth.address": [
        {
            "__id": "4f49da4f0b4df789",
            "__ref__rk.birth": "034b3cd2487b9d17",
            "street": "123 Main Street",
            "city": "Anytown",
            "state": "CA"
        }
    ]
}
```
