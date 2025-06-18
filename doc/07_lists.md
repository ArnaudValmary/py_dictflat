# dictflat

## Documentation

### Lists

Each element of a list a transformed as a dictionnary of a same type.

#### List of dictionaries

By default, no element are added in each dictionnary.

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
        },
        "Phone_Numbers": [
            {"type": "home", "number": "555-1234"},
            {"type": "work", "number": "555-5678"},
        ],
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
    ],
    "rk.Phone_Numbers": [
        {
            "__id": "5d1765d47e80b6d3",
            "__ref__rk": "2a02485bc672ee47",
            "type": "home",
            "number": "555-1234"
        },
        {
            "__id": "87d897df197fbdc7",
            "__ref__rk": "2a02485bc672ee47",
            "type": "work",
            "number": "555-5678"
        },
    ],
}
```

#### Add counter field in each list element

How: Use init function "`list_2_object`" parameter.

`list_2_object` parameter signature:

```python
Optional[Dict[str, Dict]]
```

By default, no fields are added.

The dictionnary key is the first version of the future field name.
The dictionnary value is sub-dictionnary for parametrize the job:

* The key "`counter_field`" contains the field name (a "`str`") for the counter;
  * Default value is "`idx`".
* The key "`starts_at`" contains the counter start value (a "`int`").
  * Default value is `1`.

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
    },
    list_2_object={
        "rk.Phone_Numbers": {
            "counter_field": "count",
            "starts_at": 0
        }
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
        },
        "Phone_Numbers": [
            {"type": "home", "number": "555-1234"},
            {"type": "work", "number": "555-5678"},
        ],
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
    ],
    "rk.Phone_Numbers": [
        {
            "__id": "30fb5bc71274e531",
            "__ref__rk": "2a02485bc672ee47",
            "count": 0,
            "type": "home",
            "number": "555-1234"
        },
        {
            "__id": "6b74835b56e08367",
            "__ref__rk": "2a02485bc672ee47",
            "count": 1,
            "type": "work",
            "number": "555-5678"
        },
    ],
}
```

#### List of non-dictionary elements

If the list do not contains dictionnary elements, you could specify the name of the future key with the suffix "`.__inner`".

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
        "rk.phone_numbers.__inner": "number",
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
        },
        "Phone_Numbers": [
            "555-1234",
            "555-5678",
        ],
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
    ],
    "rk.phone_numbers": [
        {
            "__id": "24886b1e9942f612",
            "__ref__rk": "2a02485bc672ee47",
            "number": "555-1234"
        },
        {
            "__id": "a98b1c4fa2e2a2b5",
            "__ref__rk": "2a02485bc672ee47",
            "number": "555-5678"
        },
    ],
}
```
