# dictflat

## Documentation

### Basic usages

#### Empty dictionnary

```python
>>> DictFlat().flat({})
```

Result:

```json
{}
```

#### Simple dictionnary

How: Use init function "`root_key`" parameter.

`root_key` parameter signature:

```python
str
```

Example:

```python
DictFlat(
    root_key="rk"
).flat(
    {
        "a": 1
    }
)
```

Result:

```json
{
    "rk": [
        {
            "__id": "i_1",
            "a": 1
        }
    ]
}
```
