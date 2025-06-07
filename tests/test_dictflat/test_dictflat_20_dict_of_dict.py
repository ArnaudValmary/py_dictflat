from typing import Dict, List

from test_dictflat.common_fct_test import date2dict, fct_build_id

from dictflat import DictFlat


def test_dictflat__dict_of_dict() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        change={
            'rk.birth.date_dict': date2dict,
        },
        rename={
            'rk.birth.date': 'rk.birth.date_dict',
        },
        dict_of_dicts_2_dict={
            'rk.miracles': {
                'reverse': False,
                'sep': '/'
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
            "miracles": {
                "first": {
                    "k": "one",
                    "e": "e-one"
                },
                "second": {
                    "k": "two"
                },
                "third": "three"
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
        ],
        'rk.miracles': [
            {
                '__id': '041102055056a3a8',
                '__ref__rk': '2a02485bc672ee47',
                'first/k': 'one',
                'first/e': 'e-one',
                'second/k': 'two',
                'third': 'three',
            },
        ],
    }


def test_dictflat__dict_of_dict_reverse() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        change={
            'rk.birth.date_dict': date2dict,
        },
        rename={
            'rk.birth.date': 'rk.birth.date_dict',
        },
        dict_of_dicts_2_dict={
            'rk.miracles': {
                'reverse': True,
                'sep': '#'
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
            "miracles": {
                "first": {
                    "k": "one",
                    "e": "e-one"
                },
                "second": {
                    "k": "two"
                },
                "third": "three"
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
        ],
        'rk.miracles': [
            {
                '__id': '041102055056a3a8',
                '__ref__rk': '2a02485bc672ee47',
                'k#first': 'one',
                'e#first': 'e-one',
                'k#second': 'two',
                'third': 'three',
            },
        ],
    }
