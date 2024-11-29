# Use OrderedDict to maintain the order of keys while sorting a dictionary.

from collections import OrderedDict
from typing import Dict

d = {"apple": 4, "banana": 2, "cherry": 4, "date": 1}

def sort_dict_by_value(d: Dict[str, int]) -> Dict[str, int]:
    od = OrderedDict(d)
    for key,value in od.items():
        key = sorted(key)
        od.update(key)
    return od.items()

print(sort_dict_by_value(d))