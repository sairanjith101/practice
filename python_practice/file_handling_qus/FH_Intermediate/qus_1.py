# Write a program to count the number of words in a file.

word_count = 0

with open('sample.txt', 'r') as file1:
    for line in file1:
        word = line.split()
        word_count += len(word)


print(word_count)