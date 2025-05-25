from typing import Dict, List

from test_dictflat.common_fct_test import clean_ids

from dictflat import DictFlat


def test_dictflat__empty() -> None:
    assert DictFlat().flat({}) == {}


def test_dictflat__non_empty() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk'
    ).flat(
        {
            'a': 1
        }
    )
    clean_ids(df)
    assert df == {
        'rk': [
            {
                '__id': 'i_1',
                'a': 1
            }
        ]
    }


def test_dictflat__2_fields() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk'
    ).flat(
        d={
            "name": "John",
            "birthdate": "10/06/1976 01:10:35"
        }
    )
    clean_ids(df)
    assert df == {
        'rk': [
            {
                '__id': 'i_1',
                'birthdate': '10/06/1976 01:10:35',
                'name': 'John'
            }
        ]
    }
