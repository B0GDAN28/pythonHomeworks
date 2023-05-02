import math


class Fraction:
    def __init__(self, numerator, denominator):
        if type(numerator) != int or type(denominator) != int:
            raise TypeError("Numerator and denominator should be integer!")

        if denominator == 0:
            raise ZeroDivisionError

        gcd = math.gcd(numerator, denominator)
        self.__numerator = numerator // gcd
        self.__denominator = denominator // gcd

    def __str__(self):
        return f"{self.__numerator}/{self.__denominator}"

    def __eq__(self, other):
        if type(other) == int:
            other = Fraction(other, 1)
        elif type(other) != Fraction:
            raise TypeError(f"Cannot compare fraction with {type(other).__name__}")

        return self.__numerator == other.__numerator and self.__denominator == other.__denominator

    def __float__(self):
        return self.__numerator / self.__denominator

    def __add__(self, other):
        if type(other) == int:
            other = Fraction(other, 1)
        elif type(other) != Fraction:
            raise TypeError(f"Cannot add fraction with {type(other).__name__}")

        new_numerator = self.__numerator * other.__denominator + other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if type(other) == int:
            other = Fraction(other, 1)
        elif type(other) != Fraction:
            raise TypeError(f"Cannot sub fraction with {type(other).__name__}")

        new_numerator = self.__numerator * other.__denominator - other.__numerator * self.__denominator
        new_denominator = self.__denominator * other.__denominator
        return Fraction(new_numerator, new_denominator)

    def inverse(self):
        if self.__numerator == 0:
            raise TypeError("We cannot create the inverse of this function because numerator is 0.")

        return Fraction(self.__denominator, self.__numerator)


if __name__ == '__main__':
    x = Fraction(8, 4)
    print(x)
