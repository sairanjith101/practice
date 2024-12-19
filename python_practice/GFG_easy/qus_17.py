# 17. LCM And GCD 

import math
from typing import List

a = 5
b = 10

class Solution:
    def lcmAndGcd(self, a : int, b : int) -> List[int]:
        gcd = math.gcd(a,b)
        lcm = (a * b) // gcd
        return [lcm, gcd]

sol = Solution()
print(sol.lcmAndGcd(a,b))