A = "Internet"
B = "Learning from Internet"

# A = "apple banana mango"
# B = "banana fruits mango"

A = A.split()
B = B.split()

output = []

for x in A:
    if x not in B:
        output.append(x)
for y in B:
    if y not in A:
        output.append(y)

print(output)