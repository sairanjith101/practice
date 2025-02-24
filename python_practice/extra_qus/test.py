from collections import Counter

nums = [10, 20, 10, 20, 30, 10]
new_num = Counter(nums)

max_num = max(new_num.values())

most_freq_num = []

for key,value in new_num.items():
    if value == max_num:
        most_freq_num.append(key)

print(min(most_freq_num))
