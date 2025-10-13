import pytest

from dictflat.dicttools import get_nested_value


@pytest.mark.parametrize(
    "d, path, sep, default, expected",
    [
        (None, 'a.b.c', '.', None, None),
        ({}, 'a.b.c', '.', None, None),
        ({'a': 1}, 'b', '.', 3, 3),
        ({'a': 1}, 'a', '.', None, 1),
        ({'a': 1}, 'a.b', '.', 2, 2),
        ({'a': {'b': 2}}, 'a.b', '.', 3, 2),
        ({'a': {'b': 0}}, 'a.b', '.', 3, 0),
        ({'a': {'b': {'c': 4}}}, 'a.b', '.', 3, {'c': 4}),
        ({'a': {'b': {'c': 1}}}, 'a.b.c', '.', None, 1),
        ({'a': {'b': {'c': {'d': 2}}}}, ['a', 'b', 'c', 'd'], '.', None, 2),
        ({'a': {'b': 1}}, 'a.c', '.', 0, 0),
        ({'a': {'b': {'c': {'d': {'e': 5}}}}}, 'a.b.c.d.e', '.', None, 5),
        ({'a': {'b': {'c': 1}}}, 'a.b.c.d', '.', None, None),
    ]
)
def test_get_nested_value(d, path, sep, default, expected):
    assert get_nested_value(d, path, sep, default) == expected
