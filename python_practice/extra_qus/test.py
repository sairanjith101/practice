def find_primes(lower: int, upper: int) -> list:
    for num in range(lower, upper+1):
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                print(num)

lower = 10  
upper = 20

find_primes(lower,upper)