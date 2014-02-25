## 2520 is the smallest number that can be divided by each of the numbers
## from 1 to 10 without any remainder.

##What is the smallest positive number that is evenly divisible
## by all of the numbers from 1 to 20?

## DOESN'T WORK


class euler0005():
    def __init__(self, size):
        self.size = size
        self.divisors = [x for x in range(1, (size + 1))]
        self.maximum = self.maximum()

    def maximum(self):
        maximum = 1
        for i in self.divisors:
            maximum = maximum * i
        return maximum

    def isFactor(self, factor, value):
        if value % factor == 0:
            return True
        else:
            return False

    def isAnswer(self, value):
        answer = True
        for i in self.divisors:
            if not self.isFactor(i, value):
                answer = False
        return answer

    def findAnswer(self):
        answers = []
        localDivisors = [x for x in range(2, (self.size + 1))]
        for i in localDivisors:
            print("i is: " + str(i))
            j = self.maximum
            while j > 1:
                if self.isAnswer(j):
                    answers.append(j)
                j = int(j / i)
                print("j is: " + str(j))
        return min(answers)

euler = euler0005(10)
print(euler.findAnswer())