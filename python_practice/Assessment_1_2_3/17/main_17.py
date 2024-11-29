arr = ('sun', 'mon', 'tue', 'sun', 'mon', 'tue', 'mon', 'tue', 'thu')
word_count = {}

for word in arr:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

print(word_count)
