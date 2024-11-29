# Implement a defaultdict to group elements by a certain criterion.
# Example: Group words by their lengths.

from collections import defaultdict
from typing import Dict, List

words = ["hello", "world", "hi", "python", "code"]

def group_words_by_length(words: List[str]) -> Dict[int, List[str]]:
    d = defaultdict(list)

    for word in words:
        d[len(word)].append(word)      

    return d

print(group_words_by_length(words))

