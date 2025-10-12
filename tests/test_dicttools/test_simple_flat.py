from typing import Dict

import pytest

from dictflat.dicttools import simple_flat


@pytest.mark.parametrize("input_dict, expected_output, process_lists", [
    # Test case 1: Simple nested dictionary
    (
        {'aa': {'b': 1, 'c': 2}, 'd': 3},
        {'aa.b': 1, 'aa.c': 2, 'd': 3},
        True
    ),
    # Test case 2: Dictionary with nested lists and dictionaries
    (
        {'ba': {'b': {'c': 1}}, 'd': [1, {'e': 2}]},
        {'ba.b.c': 1, 'd': [1, {'e': 2}]},
        True
    ),
    # Test case 3: Dictionary with lists containing dictionaries
    (
        {'users': [{'name': 'Alice', 'info': {'age': 30}}, {'name': 'Bob'}]},
        {'users': [{'name': 'Alice', 'info.age': 30}, {'name': 'Bob'}]},
        True
    ),
    # Test case 4: Dictionary with lists containing dictionaries, process_lists=False
    (
        {'users': [{'name': 'Alice', 'info': {'age': 30}}]},
        {'users': [{'name': 'Alice', 'info': {'age': 30}}]},
        False
    ),
    # Test case 5: Empty dictionary
    (
        {},
        {},
        True
    ),
    # Test case 6: None input
    (
        None,
        {},
        True
    ),
])
def test_simple_flat(input_dict, expected_output, process_lists) -> None:
    result: Dict = simple_flat(input_dict, process_lists=process_lists)
    assert result == expected_output
