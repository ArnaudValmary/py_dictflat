from datetime import datetime
from hashlib import sha256
from typing import Any, Dict, List


def clean_ids(d: Dict) -> None:
    n: int = 0
    for k in d:
        for elt in d[k]:
            n += 1
            elt['__id'] = 'i_%d' % n
            for k_elt in elt:
                if k_elt.startswith('__ref_'):
                    n += 1
                    elt[k_elt] = 'r_%d' % n


def fct_build_id(d: Dict, path: str) -> str:
    id: Any = None
    id = sha256(
        '#'.join(
            [
                str(d.get(k, '?%s?' % k))
                for k in d
                if not k.startswith('_') and not isinstance(d.get(k, []), (dict, list, tuple))
            ]
        ).encode()
    ).hexdigest()[:16]
    return id


def fix_date(fieldname: str, value: str) -> str:
    return datetime.strptime(value, '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S')


def date2dict(fieldname: str, value: str) -> Dict:
    lst: List[str] = fix_date(fieldname, value).split('T')
    return {
        'date': lst[0],
        'time': lst[1],
    }
