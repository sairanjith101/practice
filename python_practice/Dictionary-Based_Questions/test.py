list_word = ['apple', 'banana', 'cherry', 'apricot']

dict = {}

for word in list_word:
    index_word = word[0:1]
    if index_word == word[0]:
        if index_word not in dict:
            dict[index_word] += word
        else:
            dict[index_word] += word

print(dict)