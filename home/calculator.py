class Calculator:
    def __init__(self, result=0):
        self.result = result

    def __add__(self, other):
        self.result += other
        return self.result

    def __sub__(self, other):
        self.result -= other
        return self.result

    def __mul__(self, other):
        self.result *= other
        return self.result

    def __truediv__(self, other):
        self.result /= other
        return self.result

    def __str__(self):
        return self.result


c1 = Calculator(20)
c1 += 10
print(c1)
c1 -= 15
print(c1)
c1 *= 3
print(c1)
c1 /= 0
print(c1)