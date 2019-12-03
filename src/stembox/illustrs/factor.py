"""
Module for factors
"""
from dataclasses import dataclass
from enum import Enum
from typing import Union
from .expression import Expression


__all__ = [
    'Sign', 'Factor', 'Variable', 'Brackets',
    'Number', 'Fraction', 'Power', 'Root'
]


class Sign(Enum):
    POSITIVE = '+'
    NEGATIVE = '-'

    def __str__(self):
        return self.value


@dataclass
class Factor(Expression):
    """An abstract factor representation, i.e. an element of a term."""
    sign: Sign = Sign.POSITIVE


class Variable(Factor):
    """A variable, e.g. x, y or z."""
    def __init__(self, symbol: str, **kwargs):
        super().__init__(**kwargs)
        self.symbol = symbol


class Brackets(Factor):
    """An expression contained inside brackets."""
    def __init__(self, content: Expression, **kwargs):
        super().__init__(**kwargs)
        self.content = content


class Number(Factor):
    """
    A number, i.e. an int or float
    """

    def __init__(self, value: Union[int, float], **kwargs):
        super().__init__(**kwargs)
        self.absvalue = abs(value)
        self.sign = Sign.POSITIVE if value >= 0 else Sign.NEGATIVE

    @property
    def value(self):
        return (self.absvalue if self.sign == Sign.POSITIVE
                else -self.absvalue)


class Fraction(Factor):
    """
    A fraction with a numerator and a denominator, e.g. x / 3.
    """
    def __init__(self, numerator: Expression, denominator: Expression,
                 **kwargs):
        super().__init__(**kwargs)
        self.numerator = numerator
        self.denominator = denominator


class Power(Factor):
    """
    A power with a base and an exponent, e.g. 2^x.
    """
    def __init__(self, base: Expression, exponent: Expression,
                 **kwargs):
        super().__init__(**kwargs)
        self.base = base
        self.exponent = exponent


class Root(Factor):
    """
    An nth root of a certain expression, e.g. $\\sqrt(x - 3)$.
    """
    def __init__(self, radicand: Expression, index: Number,
                 **kwargs):
        super().__init__(**kwargs)
        self.radicand = radicand
        self.index = index
