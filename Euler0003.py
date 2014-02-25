## The prime factors of 13195 are 5, 7, 13 and 29.

## What is the largest prime factor of the number 600851475143 ?


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


def maxPrimeFactor(value):
    #if isPrime(value):
        #return(str(value) + " is a prime")
    #else:
        maxFactor = None
        i = 2
        while i < (value + 1):
            if isPrime(i):
                if value % i == 0:
                    maxFactor = i
                    value = value / i
                    print(maxFactor)
            i += 1
        return(maxFactor)


print(maxPrimeFactor(600851475143))


## Testing
#print(isPrime(0))
#print(isPrime(1))
#print(isPrime(2))
#print(isPrime(3))
#print(isPrime(4))
#print(isPrime(5))
#print(isPrime(6))
#print(isPrime(7))
#print(isPrime(8))
#print(isPrime(9))
#print(primeFactors(1))
#print(primeFactors(2))
#print(primeFactors(3))
#print(primeFactors(4))
#print(primeFactors(5))
#print(primeFactors(6))
#print(primeFactors(7))
#print(primeFactors(8))
#print(primeFactors(9))
#print(primeFactors(10))