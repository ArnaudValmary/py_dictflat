from typing import Dict, List

from test_dictflat.common_fct_test import fct_build_id, fct_build_id_with_context

from dictflat import DictFlat


def test_dictflat__fct_id() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id
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
                'date': '10/06/1976 01:10:35',
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


def test_dictflat__fct_id_with_context() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id_with_context,
        context={
            'root_id_format': 'id#%(pers_id)s_%(name)s'
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
            }
        }
    )
    assert df == {
        'rk': [
            {
                '__id': 'id#12_John',
                'pers_id': 12,
                'name': 'John'
            }
        ],
        'rk.birth': [
            {
                '__id': '034b3cd2487b9d17',
                '__ref__rk': 'id#12_John',
                'date': '10/06/1976 01:10:35',
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
