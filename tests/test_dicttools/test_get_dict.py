# test_dicttools.py
from typing import Dict

import pytest

from dictflat.dicttools import get_dict


@pytest.mark.parametrize(
    "input_dict, key, expected",
    [
        (None, None, {}),  # Test with None input
        ({}, None, {}),  # Test with empty dict
        ({"key": "value"}, None, {"key": "value"}),  # Test with a valid dictionary
        ("not a dict", None, {}),  # Test with non-dictionary input
        (123, None, {}),  # Test with integer input
        ([1, 2, 3], None, {}),  # Test with list input

        (None, 'Z', {}),  # Test with None input and key
        ({}, 'Z', {}),  # Test with empty dict and key
        ({"key": "value"}, 'Z', {"key": "value"}),  # Test with a valid dictionary and key
        ("not a dict", 'A', {'A': 'not a dict'}),  # Test with non-dictionary input and key
        (123, 'B', {'B': 123}),  # Test with integer input and key
        ([1, 2, 3], 'C', {'C': [1, 2, 3]}),  # Test with list input and key
    ]
)
def test_get_dict(input_dict, key, expected):
    """
    Test the get_dict function with various inputs to ensure it returns a valid dictionary.
    """
    result: Dict = get_dict(d=input_dict, key=key)
    assert result == expected
