# dictflat

## Documentation

### Rename/Change field names

How: Use init function "`rename`" parameter.

`rename` parameter signature:

```python
Optional[Dict[str, Union[str, Callable]]]
```

By default, no field names values are modified.

The dictionnary key is the first version of the future field name.
The dictionnary value is the final field name or a function to genrate the new field name.

If the dictionnary key is a "`Callable`", the signature is:

```python
def fct_name(s: str) -> str
```

**IMPORTANT**
**If you use  "`change`" parameter and "`rename`" parameter, use the final field name in "`rename`" dictionnary value as "`change`" dictionnary key**.

#### Rename field name by name

Example:

```python
DictFlat(
    root_key="rk",
    fct_build_id=fct_build_id,
    change={
        "rk.birth.date_dict": date2dict,
    },
    rename={
        "rk.birth.date": "rk.birth.date_dict",
        "PersId": "pers_id",
    }
).flat(
    d={
        "name": "John",
        "PersId": 12,
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
        }
    ],
    "rk.birth.date_dict": [
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

#### Rename ALL field names

You could rename all fields using the "`RENAME_ALL`" special key and un function to do this.

The "`Callable`" dictionnary key function signature is:

```python
def fct_name(s: str) -> str
```

**IMPORTANT**
**You could use "`RENAME_ALL`" key and field name keys. "`RENAME_ALL`" key is allway use BEFORE field name keys**

In this example, the function "[`str_2_snakecase`](https://github.com/ArnaudValmary/py_dictflat/blob/main/src/dictflat/tool_functions.py#L10)" is called before the other rename key.

Example:

```python
DictFlat(
    root_key="rk",
    fct_build_id=fct_build_id,
    change={
        "rk.birth.date_dict": date2dict,
    },
    rename={
        RENAME_ALL: str_2_snakecase,
        "rk.birth.date": "rk.birth.date_dict",
    }
).flat(
    d={
        "Name": "John",
        "PersId": 12,
        "Birth": {
            "Address": {
                "Street": "123 Main St",
                "City": "Anytown",
                "State": "CA"
            },
            "Date": "10/06/1976 01:10:35"
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
        }
    ],
    "rk.birth.date_dict": [
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

#### Use context in your own function to rename fields

How: Same first example, use init function "`rename`" parameter.

If the dictionnary key is a "`Callable`", the signature is:

```python
def fct_name(s: str, context: Dict) -> str
```

The `context` parameter is a dictionnary who contains three keys:

* `CONTEXT_DEPTH: Final[str] = '__depth'`
  * The depth of the current dictionnary in the global original dictionnary
* `CONTEXT_PATH: Final[str] = '__path'`
  * The path of the current dictionnary in the global original dictionnary
* `CONTEXT_ELEMENT: Final[str] = '__element'`
  * The current field name in the current dictionnary in the global original dictionnary

You could add any other keys during init step with optional `context` parameter.

You could use `context` for one field renaing or for all fields (with special key `RENAME_ALL`).

An example:

With `rename_date` function example:

```python
def rename_date(s: str, context: Dict) -> str:
    if context[CONTEXT_DEPTH] == 2 and context[CONTEXT_PATH] == 'rk.birth' and context[CONTEXT_ELEMENT] == 'date':
        return 'rk.birth.date_dict'
    return str_2_snakecase(s) # For other fields
```

The code :

```python
DictFlat(
    root_key='rk',
    fct_build_id=fct_build_id,
    change={
        'rk.birth.date_dict': date2dict,
    },
    rename={
        RENAME_ALL: rename_all,
        'rk.birth.date': rename_date,
    }
).flat(
    d={
        'name': 'John',
        'PersId': 12,
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
            "firstname": "John"
        }
    ],
    "rk.birth": [
        {
            "__id": "034b3cd2487b9d17",
            "__ref__rk": "2a02485bc672ee47",
        }
    ],
    "rk.birth.date_dict": [
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
