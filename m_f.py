import math
def factors(n):
    factors=set()
    for i in range(1,int(math.sqrt(n))+1):
        if(n%i==0):
            factors.add(i)
            factors.add(n//i)
        return sorted(factors)
def prime_factors(n):
    factors = []
    # Remove all factors of 2 first
    while n % 2 == 0:
        factors.append(2)
        n //= 2

    # Check for odd factors from 3 up to the square root of n
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i

    # If n is a prime number greater than 2, it will be the remaining n
    if n > 2:
        factors.append(n)

    return factors



