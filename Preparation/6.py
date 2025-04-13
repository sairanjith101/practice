# nums = [3, 1, 4, 5, 2]
nums = [10, 10, 10]


class solution:
    def secondlargest(self, nums):
        n = list(set(sorted(nums)))
        if len(n) < 2:
            return -1
        return n[-2]
    
sol = solution()
print(sol.secondlargest(nums))