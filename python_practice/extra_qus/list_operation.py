nums = [5, 3, 8, 3, 1, 8, 2]

new_nums = []

for n in nums:
    if n not in new_nums:
        new_nums.append(n)

new_nums.sort()

print(new_nums)
print("minimum num: ", min(new_nums))
print("max num: ", max(new_nums))


mylist = list(dict.fromkeys(new_nums))
print(mylist)