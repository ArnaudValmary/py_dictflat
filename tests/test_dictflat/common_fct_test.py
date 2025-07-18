from datetime import datetime
from hashlib import sha256
from typing import Any, Dict, List

from dictflat.dictflat import CONTEXT_DEPTH, CONTEXT_ELEMENT, CONTEXT_PATH
from dictflat.tool_functions import str_2_snakecase


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


def fct_build_id_with_context(d: Dict, path: str, context: Dict) -> str:
    if context[CONTEXT_DEPTH] == 1:
        id: str = context['root_id_format'] % d
    else:
        id: str = fct_build_id(d=d, path=path)
    return id


def rename_all(s: str, context: Dict) -> str:
    if context[CONTEXT_DEPTH] == 1 and s == 'name':
        return 'firstname'
    return str_2_snakecase(s)


def rename_date(s: str, context: Dict) -> str:
    if context[CONTEXT_DEPTH] == 2 and context[CONTEXT_PATH] == 'rk.birth' and context[CONTEXT_ELEMENT] == 'date':
        return 'rk.birth.date_dict'
    return str_2_snakecase(s)


# 'rk.birth.date_dict'

def fix_date(fieldname: str, value: str) -> str:
    return datetime.strptime(value, '%d/%m/%Y %H:%M:%S').strftime('%Y-%m-%dT%H:%M:%S')


def fix_street(fieldname: str, value: str, context: Dict) -> str:
    for k in context['street']:
        value = value.replace(k, context['street'][k])
    return value


def str2list(fieldname: str, value: Dict) -> Dict:
    value['elements'] = [x.strip() for x in value.get('elements', '').split(',')]
    return value


def date2dict(fieldname: str, value: str) -> Dict:
    lst: List[str] = fix_date(fieldname, value).split('T')
    return {
        'date': lst[0],
        'time': lst[1],
    }
