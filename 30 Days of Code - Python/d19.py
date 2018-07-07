class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError


class Calculator(AdvancedArithmetic):
    def divisorGenerator(self, n):
        for i in range(1, int(n/2) + 1):
            if n%i == 0: yield i
        yield n


    def divisorSum(self, n):
        sum = 0
        for i in self.divisorGenerator(n):
            sum += i
        return sum


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)