class Fraction:
    def __init__(self, numarator, numitor):
        self.numarator = numarator
        self.numitor = numitor

    def __str__(self):
        return f"Numaratorul este {self.numarator} si numitorul este {self.numitor}."


if __name__ == '__main__':
    result = Fraction(10, 10)
    print(result)
