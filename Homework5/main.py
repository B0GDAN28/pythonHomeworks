class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f"Numaratorul este {self.numerator} si numitorul este {self.denominator}."

    def __add__(self, other):
        comun = self.denominator * other.denominator
        sum_numerators = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        return Fraction(sum_numerators, comun)

    def __sub__(self, other):
        comun1 = self.denominator * other.denominator
        down_numerators = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        return Fraction(down_numerators, comun1)

    def inverse(self):
        return 1 / (self.numerator * self.denominator)


if __name__ == '__main__':
    number1 = Fraction(40, 10, )
    print(number1)
    number2 = Fraction(30, 12, )
    result = number1 + number2
    print(result)
    result1 = number1 - number2
    print(result1)
    print(number1.inverse())
