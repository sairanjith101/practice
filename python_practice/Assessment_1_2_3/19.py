# A = "apple banana mango"
# B = "banana fruits mango"

A = "Internet"
B = "Learning from Internet"

str_a = A.split()
str_b = B.split()

word = []

for a in str_a:
    if a not in str_b:
        word.append(a)

for b in str_b:
    if b not in str_a:
        word.append(b)

print(word)