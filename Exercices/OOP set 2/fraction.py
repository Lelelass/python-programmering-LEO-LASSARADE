"""
simplify(self, value = None) # simplifies to most simple form unless value is given 

__str__(self) # represent the fraction in a neat way for printing

mixed(self) # represent the fraction in mixed terms 

__eq__(self, other) # checks equality by overloading ==
"""


class Fraction:
    def __init__(self, numerator :int, denominator: int) -> None:
        if not isinstance(numerator, int):
            raise TypeError(f"numerator, must be an int, not {type(numerator)}")
        if not isinstance(denominator, int):
            raise TypeError(f"numerator, must be an int, not {type(denominator)}")
        self.numerator = numerator
        self.denominator = denominator

    def simplify(self, value = None):
        if value == None:
            for prime in [2,3,5,7]:
                if self.numerator % prime == 0 and self.denominator % prime == 0:
                    self.numerator = int(self.numerator / prime)
                    self.denominator = int(self.denominator / prime)

        else:
            self.numerator = self.numerator / value
            self.denominator = self.denominator / value

    def __repr__(self)-> str:
        return f"{self.numerator} / {self.denominator}"

    def __eq__(self, other: "Fraction")-> bool:
        if Fraction.simplify(self) == Fraction.simplify(other):
            return True
        else:
            return False

    def __add__(self, other: "Fraction")-> "Fraction":
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        fraction = Fraction(numerator, denominator)
        print(f"{fraction} ->")
        fraction.simplify()
        return fraction

    def __sub__(self, other: "Fraction")-> "Fraction":
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        fraction = Fraction(numerator, denominator)
        print(f"{fraction} ->")
        fraction.simplify()
        return fraction

    def __mul__(self, other: "Fraction")-> "Fraction":
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        fraction = Fraction(numerator, denominator)
        print(f"{fraction} ->")
        fraction.simplify()
        return fraction

    def __rmul__(self, value:float):
        return self*value