import json
from typing import Dict, List

from test_dictflat.common_fct_test import fct_build_id

from dictflat import DictFlat
from dictflat.dictflat import ALL


def test_dictflat__dict_of_dict__all() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        dict_of_dicts_2_dict={
            ALL: {
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

    print("DF=%s" % json.dumps(df, indent=2))

    assert df == {
        'rk': [
            {
                '__id': '2a02485bc672ee47',
                'pers_id': 12,
                'name': 'John',
                'birth/date': '10/06/1976 01:10:35',
                'birth/address/street': '123 Main St',
                'birth/address/city': 'Anytown',
                'birth/address/state': 'CA',
                'miracles/first/k': 'one',
                'miracles/first/e': 'e-one',
                'miracles/second/k': 'two',
                'miracles/third': 'three',
            },
        ],
    }


def test_dictflat__dict_of_dict__all_list() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        dict_of_dicts_2_dict={
            ALL: {
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
            },
            "elements": [
                {"a": "b"},
                {"a": "c"},
                {"a": "d"},
            ]
        }
    )

    print("DF=%s" % json.dumps(df, indent=2))

    assert df == {
        'rk': [
            {
                '__id': '2a02485bc672ee47',
                'pers_id': 12,
                'name': 'John',
                'birth/date': '10/06/1976 01:10:35',
                'birth/address/street': '123 Main St',
                'birth/address/city': 'Anytown',
                'birth/address/state': 'CA',
                'miracles/first/k': 'one',
                'miracles/first/e': 'e-one',
                'miracles/second/k': 'two',
                'miracles/third': 'three',
            },
        ],
        'rk.elements': [
            {
                '__id': '3e23e8160039594a',
                '__ref__rk': '2a02485bc672ee47',
                'a': 'b',
            },
            {
                '__id': '2e7d2c03a9507ae2',
                '__ref__rk': '2a02485bc672ee47',
                'a': 'c',
            },
            {
                '__id': '18ac3e7343f01689',
                '__ref__rk': '2a02485bc672ee47',
                'a': 'd',
            },
        ]
    }


def test_dictflat__dict_of_dict__all_list_of_dd() -> None:
    df: Dict[str, List] = DictFlat(
        root_key='rk',
        fct_build_id=fct_build_id,
        dict_of_dicts_2_dict={
            ALL: {
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
            },
            "elements": [
                {
                    "a": "b",
                    "b": {
                        "e": "k"
                    }
                },
                {
                    "a": "c",
                    "c": {
                        "g": {
                            "h": "i"
                        },
                        "f": "l"
                    }
                },
                {"a": "d"},
            ]
        }
    )

    print("DF=%s" % json.dumps(df, indent=2))

    assert df == {
        'rk': [
            {
                '__id': '2a02485bc672ee47',
                'pers_id': 12,
                'name': 'John',
                'birth/date': '10/06/1976 01:10:35',
                'birth/address/street': '123 Main St',
                'birth/address/city': 'Anytown',
                'birth/address/state': 'CA',
                'miracles/first/k': 'one',
                'miracles/first/e': 'e-one',
                'miracles/second/k': 'two',
                'miracles/third': 'three',
            },
        ],
        'rk.elements': [
            {
                '__id': '3e23e8160039594a',
                '__ref__rk': '2a02485bc672ee47',
                'a': 'b',
                "b/e": "k",
            },
            {
                '__id': '2e7d2c03a9507ae2',
                '__ref__rk': '2a02485bc672ee47',
                'a': 'c',
                'c/f': 'l',
                'c/g/h': 'i',
            },
            {
                '__id': '18ac3e7343f01689',
                '__ref__rk': '2a02485bc672ee47',
                'a': 'd',
            },
        ]
    }
