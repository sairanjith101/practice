import math

def lcm_and_gcd(a,b):
    gcd = math.gcd(a,b)
    lcm = (a*b) // gcd
    return [lcm, gcd]

a = 5
b = 10

print(lcm_and_gcd(a,b))