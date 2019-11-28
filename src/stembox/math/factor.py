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


@dataclass
class Brackets(Factor):
    """
    An expression contained inside brackets.
    """
    content: Expression


class Number(Factor):
    """
    A number, i.e. an int or float
    """

    def __init__(self, value: Union[int, float]):
        self.absvalue = abs(value)
        self.sign = Sign.POSITIVE if value >= 0 else Sign.NEGATIVE


@dataclass
class Fraction(Factor):
    """
    A fraction with a numerator and a denominator, e.g. x / 3.
    """
    numerator: Expression
    denominator: Expression


@dataclass
class Power(Factor):
    """
    A power with a base and an exponent, e.g. 2^x.
    """
    base: Expression
    exponent: Expression


@dataclass
class Root(Factor):
    """
    An nth root of a certain expression, e.g. $\\sqrt(x - 3)$.
    """
    radicand: Expression
    index: Number
