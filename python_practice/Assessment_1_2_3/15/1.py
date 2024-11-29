def compoundinterest(P,R,T):
    formula = P*(1+(R/100))**T
    return formula

P = float(input("Principle amount : "))
R = float(input("Rate : "))
T = float(input("Time : "))

if __name__ == "__main__":
    compint = compoundinterest(P,R,T)
    print("Compound Inetrest : ", compint)