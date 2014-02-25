## A palindromic number reads the same both ways.
## The largest palindrome made from the product of two 2-digit numbers is
## 9009 = 91 × 99.

## Find the largest palindrome made from the product of two 3-digit numbers.

## REALLY SLOW SOLUTION

def isPalindrome(value):
    valStr = str(value)
    strLen = len(valStr)
    if len(valStr) % 2 == 0:
        halfLen = int(strLen / 2)
    else:
        halfLen = int((strLen - 1) / 2)
    firstHalf = valStr[:halfLen]
    secondHalf = valStr[::-1]
    secondHalf = secondHalf[:halfLen]
    for i in range(halfLen):
        if not firstHalf[i] is secondHalf[i]:
            return False
    return True


def products():
    products = []
    batcha = [x for x in range(1000)]
    batcha.reverse()
    batchb = [x for x in range(1000)]
    batchb.reverse()
    for i in batcha:
        for j in batchb:
            product = i * j
            if product not in products:
                products.append(product)
                #print(i, j, product)
        batchb.pop()
    products.sort()
    products.reverse()
    return products


def maxPalindrome():
    productList = products()
    for i in productList:
        if isPalindrome(i):
            return i

print(maxPalindrome())

## Testing:
#print(isPalindrome(1551))
#print(isPalindrome(15351))
#print(isPalindrome(1234))
#print(isPalindrome(1234567))
#print(products())