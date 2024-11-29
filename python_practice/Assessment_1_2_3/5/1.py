arr = [1, 2, 'a', 'b', '3', 'c', '4', 'd', 5]

integer = []


for elements in arr:
    if isinstance(elements,int):
        integer.append(elements)

print(integer)