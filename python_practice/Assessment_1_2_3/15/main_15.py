def compoundinterest(p,r,t):
    compint = p*(1+(r/100))**t
    return compint
p = float(input("Principle amount : "))
t = float(input("Time : "))
r = float(input("Rate : "))
compint = compoundinterest(p,r,t)
print("Compound Interest : ", compint)
