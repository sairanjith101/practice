lower = 100
upper = 1000

# lower = 1000
# upper = 10000

# lower = 10000
# upper = 100000

output = []

for i in range(lower,upper+1):
    n = len(str(i))

    split_num = list(str(i))

    total = []
    
    for j in split_num:
        mul_num = int(j) ** n
        total.append(mul_num)
    
    if sum(total) == i:
        output.append(i)

print(output)