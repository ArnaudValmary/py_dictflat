import pytest

from dictflat.dicttools import set_nested_value


@pytest.mark.parametrize(
    "input_dict, path, value, expected, is_list, uniq, transform_to_list",
    [
        # Test cases for basic nested value setting
        ({'a': {'b': {'c': 1}}}, 'a.b.c', 2, {'a': {'b': {'c': 2}}}, False, False, False),
        ({'a': {'b': {'c': {'d': 2}}}}, ['a', 'b', 'c', 'd'], 3, {'a': {'b': {'c': {'d': 3}}}}, False, False, False),
        ({'a': {'b': 1}}, 'a.c', 0, {'a': {'b': 1, 'c': 0}}, False, False, False),
        ({'a': {'b': {'c': {'d': {'e': 5}}}}}, 'a.b.c.d.e', 6, {'a': {'b': {'c': {'d': {'e': 6}}}}}, False, False, False),

        # Test cases for list operations
        ({'a': None}, 'a.b', 1, {'a': {'b': [1]}}, True, False, False),
        ({'a': {'b': 5}}, 'a.b', 1, {'a': {'b': [1]}}, True, False, False),
        ({'a': {'b': []}}, 'a.b', 1, {'a': {'b': [1]}}, True, False, False),
        ({'a': {'b': [1, 2]}}, 'a.b', 3, {'a': {'b': [1, 2, 3]}}, True, False, False),
        ({'a': {'b': [1, 2]}}, 'a.b', 2, {'a': {'b': [1, 2]}}, True, True, False),
        ({'a': {'b': [1, 2]}}, 'a.b', 2, {'a': {'b': [1, 2, 2]}}, True, False, False),

        # Test cases for transform_to_list
        ({'a': {'b': 1}}, 'a.b', 2, {'a': {'b': [1, 2]}}, True, False, True),
        ({'a': {'b': 1}}, 'a.b', 1, {'a': {'b': [1, 1]}}, True, False, True),
        ({'a': {'b': 1}}, 'a.b', 1, {'a': {'b': [1]}}, True, True, True),

        # Edge cases
        ({}, 'a.b.c', 1, {'a': {'b': {'c': 1}}}, False, False, False),
        ({'a': {'b': {'c': 1}}}, 'a.b.c.d', 2, {'a': {'b': {'c': {'d': 2}}}}, False, False, False),
    ])
def test_set_nested_value(input_dict, path, value, expected, is_list, uniq, transform_to_list):
    result = set_nested_value(input_dict, path, value, is_list=is_list, uniq=uniq, transform_to_list=transform_to_list)
    assert result == expected


def test_set_nested_value_invalid_input():
    with pytest.raises(ValueError):
        set_nested_value("not a dict", 'a.b.c', 1)
