# Sort a dictionary by its keys and values.

from typing import Dict, List, Tuple


d = {'z': 3, 'y': 2, 'x': 5}

def sort_dict_by_keys_values(d: Dict[str, int]) -> List[Tuple[str, int]]:
    return sorted(d.items())

print(sort_dict_by_keys_values(d))