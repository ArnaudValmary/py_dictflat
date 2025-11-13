# test_dicttools.py
from typing import Dict

import pytest

from dictflat.dicttools import get_dict


@pytest.mark.parametrize("input_dict, expected", [
    (None, {}),  # Test with None input
    ({}, {}),  # Test with empty dict
    ({"key": "value"}, {"key": "value"}),  # Test with a valid dictionary
    ("not a dict", {}),  # Test with non-dictionary input
    (123, {}),  # Test with integer input
    ([1, 2, 3], {}),  # Test with list input
])
def test_get_dict(input_dict, expected):
    """
    Test the get_dict function with various inputs to ensure it returns a valid dictionary.
    """
    result: Dict = get_dict(input_dict)
    assert result == expected
