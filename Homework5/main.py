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



if __name__ == '__main__':
    number1 = Fraction(12, 10,)
    number2 = Fraction(30, 12,)
    result = number1 + number2
    print(result)
    # # number2=Fraction(10,30)
    # # result=number1 __add__number2
    # print(result)
