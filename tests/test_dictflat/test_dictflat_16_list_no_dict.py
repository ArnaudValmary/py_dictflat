from typing import Dict, List

from dictflat import DictFlat
from dictflat.dictflat import RENAME_ALL
from dictflat.tool_functions import str_2_snakecase
from tests.test_dictflat.common_fct_test import date2dict, fct_build_id


def test_dictflat__list_no_dict() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        change={
            'rk.birth.date_dict': date2dict,
        },
        rename={
            RENAME_ALL: str_2_snakecase,
            'rk.birth.date': 'rk.birth.date_dict',
            'rk.phone_numbers.__inner': 'number',
        }
    ).flat(
        d={
            'name': 'John',
            'pers_id': 12,
            'birth': {
                'address': {
                    'street': '123 Main St',
                    'city': 'Anytown',
                    'state': 'CA'
                },
                'date': '10/06/1976 01:10:35'
            },
            'Phone_Numbers': [
                '555-1234',
                '555-5678',
            ],
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
        ],
        'rk.phone_numbers': [
            {
                '__id': '24886b1e9942f612',
                '__ref__rk': '2a02485bc672ee47',
                'number': '555-1234'
            },
            {
                '__id': 'a98b1c4fa2e2a2b5',
                '__ref__rk': '2a02485bc672ee47',
                'number': '555-5678'
            },
        ],
    }
