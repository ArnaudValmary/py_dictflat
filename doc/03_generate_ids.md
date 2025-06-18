# dictflat

## Documentation

### Use your own function to generate ids

How: Use init function "`fct_build_id`" parameter.

`fct_build_id` parameter signature:

```python
def fct_name(d: Dict, path: str) -> str
```

By default, the "[`uuid4`](https://docs.python.org/3/library/uuid.html#uuid.uuid4)" function from "[`uuid`](https://docs.python.org/3/library/uuid.html)" Python standard module is used.

In this example the function [`fct_build_id`](https://github.com/ArnaudValmary/py_dictflat/blob/main/tests/test_dictflat/common_fct_test.py#L18) is used to generate ids.

Example:

```python
DictFlat(
    root_key="rk",
    fct_build_id=fct_build_id
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
            "date": "10/06/1976 01:10:35",
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

### Use context in your own function to generate ids

How: Same previous example, use init function "`fct_build_id`" parameter.

`fct_build_id` parameter signature contains a `context` parameter:

```python
def fct_name(d: Dict, path: str, context:Dict) -> str
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

With `fct_build_id_with_context` function example:

```python
def fct_build_id_with_context(d: Dict, path: str, context: Dict) -> str:
    if context[CONTEXT_DEPTH] == 1:
        id: str = context['root_id_format'] % d
    else:
        id: str = fct_build_id(d=d, path=path) # call another global function
    return id
```

The code :

```python
DictFlat(
    root_key='rk',
    fct_build_id=fct_build_id_with_context,
    context={
        'root_id_format': 'id#%(pers_id)s_%(name)s'
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
            "__id": "id#12_John",
            "pers_id": 12,
            "name": "John"
        }
    ],
    "rk.birth": [
        {
            "__id": "034b3cd2487b9d17",
            "__ref__rk": "id#12_John",
            "date": "10/06/1976 01:10:35",
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
