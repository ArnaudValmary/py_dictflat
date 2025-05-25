from typing import Dict, List

from test_dictflat.common_fct_test import clean_ids

from dictflat import DictFlat


def test_dictflat__nested_1() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk'
    ).flat(
        d={
            'name': 'John',
            'address': {
                'street': '123 Main St',
                'city': 'Anytown',
                'state': 'CA'
            },
            'birthdate': '10/06/1976 01:10:35'
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
        ],
        'rk.address': [
            {
                '__id': 'i_2',
                '__ref__rk': 'r_3',
                'street': '123 Main St',
                'city': 'Anytown',
                'state': 'CA'
            }
        ]
    }


def test_dictflat__nested_2() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk'
    ).flat(
        d={
            'name': 'John',
            'birth': {
                'address': {
                    'street': '123 Main St',
                    'city': 'Anytown',
                    'state': 'CA'
                },
                'date': '10/06/1976 01:10:35'
            }
        }
    )
    clean_ids(df)
    assert df == {
        'rk': [
            {
                '__id': 'i_1',
                'name': 'John'
            }
        ],
        'rk.birth': [
            {
                '__id': 'i_2',
                '__ref__rk': 'r_3',
                'date': '10/06/1976 01:10:35',
            }
        ],
        'rk.birth.address': [
            {
                '__id': 'i_4',
                '__ref__rk.birth': 'r_5',
                'street': '123 Main St',
                'city': 'Anytown',
                'state': 'CA'
            }
        ]
    }
