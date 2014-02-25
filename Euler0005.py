## 2520 is the smallest number that can be divided by each of the numbers
## from 1 to 10 without any remainder.

##What is the smallest positive number that is evenly divisible
## by all of the numbers from 1 to 20?

## DOESN'T WORK


def euler0005():
    isValid = False
    i = 0
    divisors = [x for x in range(1, 21)]
    print(divisors)
    while not isValid:
        i += 20
        isValid = True
        for j in divisors:
            if not i % j == 0:
                isValid = False
        print(i, isValid)
    return(i)


print(euler0005())
