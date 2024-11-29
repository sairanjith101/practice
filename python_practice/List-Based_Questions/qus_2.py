# Flatten a nested list into a single list.

from typing import List


# nested_list = [[1, 2], [3, 4], [5]]
nested_list = [[10, 20], [30], [], [40, 50]]

def flatten_list(nested_list: List[List[int]]) -> List[int]:
    output = []
    for i in nested_list:
        for j in i:
            output.append(j)
    return output

print(flatten_list(nested_list))