# Create a set of all vowels present in a given string.

s = "hello world"

def find_vowels(s: str) -> set:
    vowels = {'a','e','i','o','u'}
    result = set()

    for char in s.lower():
        if char in vowels:
            result.add(char)
    
    return result

print(find_vowels(s))