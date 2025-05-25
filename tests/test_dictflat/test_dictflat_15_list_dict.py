from typing import Dict, List

from test_dictflat.common_fct_test import date2dict, fct_build_id

from dictflat import DictFlat


def test_dictflat__list() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        change={
            'rk.birth.date_dict': date2dict,
        },
        rename={
            'rk.birth.date': 'rk.birth.date_dict',
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
                {'type': 'home', 'number': '555-1234'},
                {'type': 'work', 'number': '555-5678'},
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
        'rk.Phone_Numbers': [
            {
                '__id': '5d1765d47e80b6d3',
                '__ref__rk': '2a02485bc672ee47',
                'type': 'home',
                'number': '555-1234'
            },
            {
                '__id': '87d897df197fbdc7',
                '__ref__rk': '2a02485bc672ee47',
                'type': 'work',
                'number': '555-5678'
            },
        ],
    }


def test_dictflat__list_counter() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        change={
            'rk.birth.date_dict': date2dict,
        },
        rename={
            'rk.birth.date': 'rk.birth.date_dict',
        },
        list_2_object={
            'rk.Phone_Numbers': {
                'starts_at': 0
            }
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
                {'type': 'home', 'number': '555-1234'},
                {'type': 'work', 'number': '555-5678'},
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
        'rk.Phone_Numbers': [
            {
                '__id': '30fb5bc71274e531',
                '__ref__rk': '2a02485bc672ee47',
                'idx': 0,
                'type': 'home',
                'number': '555-1234'
            },
            {
                '__id': '6b74835b56e08367',
                '__ref__rk': '2a02485bc672ee47',
                'idx': 1,
                'type': 'work',
                'number': '555-5678'
            },
        ],
    }


def test_dictflat__list_counter_field() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        change={
            'rk.birth.date_dict': date2dict,
        },
        rename={
            'rk.birth.date': 'rk.birth.date_dict',
        },
        list_2_object={
            'rk.Phone_Numbers': {
                'counter_field': 'count',
                'starts_at': 1
            }
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
                {'type': 'home', 'number': '555-1234'},
                {'type': 'work', 'number': '555-5678'},
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
        'rk.Phone_Numbers': [
            {
                '__id': '2849245103fcc026',
                '__ref__rk': '2a02485bc672ee47',
                'count': 1,
                'type': 'home',
                'number': '555-1234'
            },
            {
                '__id': 'e1e98b582d437ee4',
                '__ref__rk': '2a02485bc672ee47',
                'count': 2,
                'type': 'work',
                'number': '555-5678'
            },
        ],
    }
