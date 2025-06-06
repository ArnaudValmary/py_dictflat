from typing import Dict, List

from test_dictflat.common_fct_test import clean_ids

from dictflat import DictFlat


def test_dictflat__nested_simple_key() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        simple_keys=True
    ).flat(
        d={
            'name': 'John',
            'birth': {
                'address': {
                    'street': {
                        'number': '123',
                        'road': 'Main St'
                    },
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
        'birth': [
            {
                '__id': 'i_2',
                '__ref__rk': 'r_3',
                'date': '10/06/1976 01:10:35',
            }
        ],
        'address': [
            {
                '__id': 'i_4',
                '__ref__birth': 'r_5',
                'city': 'Anytown',
                'state': 'CA'
            }
        ],
        'street': [
            {
                '__id': 'i_6',
                '__ref__address': 'r_7',
                'number': '123',
                'road': 'Main St',
            },
        ]
    }
