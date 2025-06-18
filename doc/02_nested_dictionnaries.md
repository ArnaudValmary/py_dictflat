# dictflat

## Documentation

### Nested dictionnaries

#### 2 levels

Example:

```python
DictFlat(
    root_key="rk"
).flat(
    d={
        "name": "John",
        "address": {
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA"
        },
        "birthdate": "10/06/1976 01:10:35"
    }
)
```

Result:

```json
{
    "rk": [
        {
            "__id": "i_1",
            "birthdate": "10/06/1976 01:10:35",
            "name": "John"
        }
    ],
    "rk.address": [
        {
            "__id": "i_2",
            "__ref__rk": "r_3",
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA"
        }
    ]
}
```

#### 3 levels

Example:

```python
DictFlat(
    root_key="rk"
).flat(
    d={
        "name": "John",
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
            "__id": "i_1",
            "name": "John"
        }
    ],
    "rk.birth": [
        {
            "__id": "i_2",
            "__ref__rk": "r_3",
            "date": "10/06/1976 01:10:35",
        }
    ],
    "rk.birth.address": [
        {
            "__id": "i_4",
            "__ref__rk.birth": "r_5",
            "street": "123 Main St",
            "city": "Anytown",
            "state": "CA"
        }
    ]
}
```
