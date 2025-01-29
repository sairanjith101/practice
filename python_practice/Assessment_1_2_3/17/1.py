arr = ['sun', 'mon', 'tue', 'sun', 'mon', 'tue', 'mon', 'tue', 'thu']

output = {}

for i in arr:
    if i not in output:
        output[i] = 1
    else:
        output[i] += 1

print(output)