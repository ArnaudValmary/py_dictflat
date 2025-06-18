# dictflat

## Documentation

### Nested dictionnaries with simple key names

When you don't want long key names.

How: Use init function "`simple_keys`" parameter.

`simple_keys` parameter signature:

```python
bool
```

Default value is `False`.

**!Warning!**
If you use this parameter with `True` value. The result may contains some unexpected values. If you have input with two or more sub-dictionnaries with the same name but in different paths, the output contains only one general key. See second example

#### Simple case

Example:

```python
DictFlat(
    root_key="rk",
    simple_keys=True
).flat(
    d={
        "name": "John",
        "birth": {
            "address": {
                "street": {
                    "number": "123",
                    "road": "Main St"
                },
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
            "__id": "i_1",
            "name": "John"
        }
    ],
    "birth": [
        {
            "__id": "i_2",
            "__ref__rk": "r_3",
            "date": "10/06/1976 01:10:35",
        }
    ],
    "address": [
        {
            "__id": "i_4",
            "__ref__birth": "r_5",
            "city": "Anytown",
            "state": "CA"
        }
    ],
    "street": [
        {
            "__id": "i_6",
            "__ref__address": "r_7",
            "number": "123",
            "road": "Main St",
        },
    ]
}
```

#### Unexpected result ?

Example:

```python
DictFlat(
    root_key="rk",
    simple_keys=True
).flat(
    d={
        "name": "John",
        "birth": {
            "address": {
                "street": {
                    "number": "123",
                    "road": "Main St"
                },
                "city": "Anytown",
                "state": "CA"
            },
            "date": "10/06/1976 01:10:35"
        },
        "street": {
            "other": "abc"
        }
    }
)
```

Result:

```json
{
    "rk": [
        {
            "__id": "i_1",
            "name": "John"
        }
    ],
    "birth": [
        {
            "__id": "i_2",
            "__ref__rk": "r_3",
            "date": "10/06/1976 01:10:35",
        }
    ],
    "address": [
        {
            "__id": "i_4",
            "__ref__birth": "r_5",
            "city": "Anytown",
            "state": "CA"
        }
    ],
    "street": [
        {
            "__id": "i_6",
            "__ref__address": "r_7",
            "number": "123",
            "road": "Main St",
        },
        {
            "__id": "i_8",
            "__ref__rk": "r_9",
            "other": "abc",
        },

    ]
}
```
