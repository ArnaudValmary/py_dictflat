from typing import Dict, List

from test_dictflat.common_fct_test import date2dict, fct_build_id

from dictflat import DictFlat
from dictflat.tool_functions import str_2_snakecase


def test_dictflat__rename() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        change={
            'rk.birth.date_dict': date2dict,
        },
        rename={
            'rk.birth.date': 'rk.birth.date_dict',
            'PersId': 'pers_id',
        }
    ).flat(
        d={
            'name': 'John',
            'PersId': 12,
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
    assert df == {
        'rk': [
            {
                '__id': '2a02485bc672ee47',
                'pers_id': 12,
                'name': 'John'
            }
        ],
        'rk.birth': [
            {
                '__id': '034b3cd2487b9d17',
                '__ref__rk': '2a02485bc672ee47',
            }
        ],
        'rk.birth.date_dict': [
            {
                '__id': '71d9d6cb90bcd168',
                '__ref__rk.birth': '034b3cd2487b9d17',
                'date': '1976-06-10',
                'time': '01:10:35',
            }
        ],
        'rk.birth.address': [
            {
                '__id': '4f49da4f0b4df789',
                '__ref__rk.birth': '034b3cd2487b9d17',
                'street': '123 Main St',
                'city': 'Anytown',
                'state': 'CA'
            }
        ]
    }


def test_dictflat__rename_with_fct() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        change={
            'rk.birth.date_dict': date2dict,
        },
        rename={
            'rk.birth.date': 'rk.birth.date_dict',
            'PersId': str_2_snakecase,
        }
    ).flat(
        d={
            'name': 'John',
            'PersId': 12,
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
    assert df == {
        'rk': [
            {
                '__id': '2a02485bc672ee47',
                'pers_id': 12,
                'name': 'John'
            }
        ],
        'rk.birth': [
            {
                '__id': '034b3cd2487b9d17',
                '__ref__rk': '2a02485bc672ee47',
            }
        ],
        'rk.birth.date_dict': [
            {
                '__id': '71d9d6cb90bcd168',
                '__ref__rk.birth': '034b3cd2487b9d17',
                'date': '1976-06-10',
                'time': '01:10:35',
            }
        ],
        'rk.birth.address': [
            {
                '__id': '4f49da4f0b4df789',
                '__ref__rk.birth': '034b3cd2487b9d17',
                'street': '123 Main St',
                'city': 'Anytown',
                'state': 'CA'
            }
        ]
    }
