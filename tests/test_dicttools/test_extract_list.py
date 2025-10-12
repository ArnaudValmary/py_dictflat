# test_dicttools.py
import pytest

from dictflat.dicttools import extract_list


@pytest.mark.parametrize("input_dict, expected_lists, expected_others", [
    # Test case 1: Dictionary with list values
    (
        {'a': [1, 2], 'b': 3, 'c': ['x', 'y']},
        {'a': [1, 2], 'c': ['x', 'y']},
        {'b': 3}
    ),
    # Test case 2: Dictionary with no list values
    (
        {'a': 1, 'b': 2, 'c': 3},
        {},
        {'a': 1, 'b': 2, 'c': 3}
    ),
    # Test case 3: Empty dictionary
    (
        {},
        {},
        {}
    ),
    # Test case 4: None input
    (
        None,
        {},
        {}
    ),
    # Test case 5: Dictionary with mixed types including lists
    (
        {'a': [1, 2], 'b': 'string', 'c': {'key': 'value'}, 'd': [4, 5]},
        {'a': [1, 2], 'd': [4, 5]},
        {'b': 'string', 'c': {'key': 'value'}}
    ),
])
def test_extract_list(input_dict, expected_lists, expected_others):
    lists, others = extract_list(input_dict)
    assert lists == expected_lists
    assert others == expected_others
