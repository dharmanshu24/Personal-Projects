class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        max = self.__elements[0]
        min = self.__elements[0]
        for num in self.__elements:
            if num > max:
                max = num
            if num < min:
                min = num
        self.maximumDifference = max - min   


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)