class Fraction:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"Numaratorul este {self.numarator} si numitorul este {self.numitor}."

    def __add__(self, other):
        comun = self.numitor * other.numitor
        suma_numaratorilor = (self.numarator * other.numitor) + (other.numarator * self.numitor)
        return Fraction(suma_numaratorilor, comun)

    def __sub__(self, other):
        comun1 = self.numitor * other.numitor
        scaderea_numaratorilor = (self.numarator * other.numitor) - (other.numarator * self.numitor)
        return Fraction(scaderea_numaratorilor, comun1)

    def inverse(self):
        return 1 / (self.numarator * self.numitor)


if __name__ == '__main__':
    number1 = Fraction(40, 10, )
    print(number1)
    number2 = Fraction(30, 12, )
    result = number1 + number2
    print(result)
    result1 = number1 - number2
    print(result1)
    print(number1.inverse())
