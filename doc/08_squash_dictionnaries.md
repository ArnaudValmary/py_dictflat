# dictflat

## Documentation

### Squash dictionnaries

When you have a dictionary of dictionaries and want to have just one.

How: Use init function "`dict_of_dicts_2_dict`" parameter.

`dict_of_dicts_2_dict` parameter signature:

```python
Optional[Dict[str, Dict]]
```

The key is the future dictionnary name
The value is the definition of treatment:

* "`sep`": The separator between the key of first data dictionnary and the key of second data dictionnary (default value is a dot "`.`")
  * You could change the default value for all separators with "`sep`" init function.
* "`reverse`": To change the order of the keys on each side of the separator (default value is `False`)

Example:

From:

```text
{
    "miracles": {
        "first": {
            "k": "one",
            "e": "e-one"
        },
        "second": {
            "k": "two"
        },
        "third": "three"
    }
}
```

To:

```txt
{
    "rk.miracles": [
        {
            "__id": "041102055056a3a8",
            "__ref__rk": "2a02485bc672ee47",
            "first/k": "one",
            "first/e": "e-one",
            "second/k": "two",
            "third": "three",
        },
    ]
}
```

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
    dict_of_dicts_2_dict={
        "rk.miracles": {
            "reverse": False,
            "sep": "/"
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
        "miracles": {
            "first": {
                "k": "one",
                "e": "e-one"
            },
            "second": {
                "k": "two"
            },
            "third": "three"
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
    ],
    "rk.miracles": [
        {
            "__id": "041102055056a3a8",
            "__ref__rk": "2a02485bc672ee47",
            "first/k": "one",
            "first/e": "e-one",
            "second/k": "two",
            "third": "three",
        },
    ],
}
```
