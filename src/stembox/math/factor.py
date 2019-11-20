"""
Module for factors
"""
from dataclasses import dataclass
from enum import Enum
from typing import Union
from ..math.expression import Expression


class Sign(Enum):
    POSITIVE = '+'
    NEGATIVE = '-'

    def __str__(self):
        return self.value


@dataclass
class Factor(Expression):
    """An abstract factor representation, i.e. an element of a term."""
    sign: Sign = Sign.POSITIVE


@dataclass
class Variable(Factor):
    """
    A variable, e.g. x, y or z.
    """
    symbol: str

    def __eq__(self, other):
        return self.symbol == other.symbol


@dataclass
class Brackets(Factor):
    """
    An expression contained inside brackets.
    """
    content: Expression


@dataclass
class Number(Factor):
    """
    A number, i.e. an int or float
    """

    def __init__(self, value: Union[int, float]):
        self.value = abs(value)
        self.sign = Sign.POSITIVE if value >= 0 else Sign.NEGATIVE

    @property
    def tex(self):
        """The TeX representation of the number."""
        if self.sign == Sign.NEGATIVE:
            return f'{self.sign}{self.value}'
        else:
            return f'{self.value}'


@dataclass
class Fraction(Factor):
    """
    A fraction with a numerator and a denominator, e.g. x / 3.
    """
    numerator: Expression
    denominator: Expression

    @property
    def tex(self):
        """The TeX representation of the fraction."""
        return f'\\frac{{{self.numerator.tex}}}{{{self.denominator.tex}}}'


@dataclass
class Power(Factor):
    """
    A power with a base and an exponent, e.g. 2^x.
    """
    base: Factor
    exponent: Expression

    @property
    def tex(self):
        """The TeX representation of the power."""
        if (self.base.sign == Sign.NEGATIVE
                or isinstance(self.base, Power)
                or isinstance(self.base, Fraction)):
            return f'{{{Brackets(self.base).tex}}}^{{{self.exponent.tex}}}'
        else:
            return f'{{{Brackets(self.base).tex}}}^{{{self.exponent.tex}}}'


@dataclass
class Root(Factor):
    """
    An nth root of a certain expression, e.g. $\\sqrt(x - 3)$.
    """
    radicand: Expression
    index: Number

    @property
    def tex(self):
        """The TeX representation of the root."""
        if self.index.value == 2:
            return f'\\sqrt{{{self.radicand.tex}}}'
        else:
            return f'\\sqrt[{self.index.tex}]{{{self.radicand.tex}}}'
