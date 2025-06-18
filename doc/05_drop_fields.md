# dictflat

## Documentation

### Drop fields (by name)

How: Use init function "`drop`" parameter.

`drop` parameter signature:

```python
Optional[List[str]]
```

By default, no values are dropped.

Elements list are the future field names.

Example:

```python
DictFlat(
    root_key="rk",
    fct_build_id=fct_build_id,
    change={
        "rk.birth.date": fix_date,
    },
    drop=[
        "rk.birth.address.state",
    ]
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
            "city": "Anytown"
        }
    ]
}
```
