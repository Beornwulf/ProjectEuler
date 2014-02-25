## 2520 is the smallest number that can be divided by each of the numbers
## from 1 to 10 without any remainder.

##What is the smallest positive number that is evenly divisible
## by all of the numbers from 1 to 20?


def isPrime(value):
    # all primes are integers
    if not type(value) is int:
        return False
    # all primes are greater than 1
    elif value < 2:
        return False
    # 2 is a prime
    elif value == 2:
        return True
    # other even numbers are not
    elif value % 2 == 0:
        return False
    # a prime must only divide by itself and one
    else:
        for i in range(2, (value)):
            if value % i == 0:
                return False
    return True


def primeFactors(value):
    factors = []
    i = 2
    while i < (value + 1):
        if isPrime(i):
            while value % i == 0:
                factors.append(i)
                value = value / i
        i += 1
    return(factors)


def euler0005(size):
    answer = 1
    divisors = [x for x in range(1, (size + 1))]
    primeDivisors = []
    for i in divisors:
        primes = primeFactors(i)
        for j in primes:
            while primes.count(j) > primeDivisors.count(j):
                primeDivisors.append(j)
    for i in primeDivisors:
        answer *= i
    return answer


print(euler0005(20))
#print(primeFactors(2520))