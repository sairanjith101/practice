# Group a list of words by their first letter into a dictionary

from typing import List, Dict

def group_words_by_first_letter(words: List[str]) -> Dict[str, List[str]]:
    word_dict = {}  # Initialize an empty dictionary
    
    for word in words:
        first_letter = word[0]  # Get the first letter of the word
        if first_letter not in word_dict:
            word_dict[first_letter] = [word]  # Create a new list with the word
        else:
            word_dict[first_letter].append(word)  # Append the word to the existing list
    
    return word_dict

# Test case
words = ['apple', 'banana', 'cherry', 'apricot']
output = group_words_by_first_letter(words)
print(output)

