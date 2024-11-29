arr = ('sun', 'mon', 'tue', 'sun', 'mon', 'tue', 'mon', 'tue', 'thu')

dic = {}

for word in arr:
    if word in dic:
        dic[word] += 1
    else:
        dic[word] = 1

print(dic)