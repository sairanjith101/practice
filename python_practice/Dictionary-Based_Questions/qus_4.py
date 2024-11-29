# Write a program to count the occurrences of each word in a file and store the result in a dictionary.

from collections import Counter

with open('input.txt','r+') as file1:
    lines = file1.readlines()
    for l in lines:
        words = l.lower().split()
        print(Counter(words))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from collections import Counter

with open('input.txt', 'r') as file1:
    # Read all lines from the file
    lines = file1.readlines()
    
    # Initialize an empty Counter
    word_count = Counter()
    
    for line in lines:
        # Split the line into words, convert to lowercase, and update the Counter
        words = line.lower().split()
        word_count.update(words)

print(word_count)
