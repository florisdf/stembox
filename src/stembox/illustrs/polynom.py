"""Representing and solving problems with polynomials."""
from typing import List
from .expression import Expression
from .factor import Factor


__all__ = [
    'Monomial', 'Polynomial'
]


class Monomial(Expression):
    def __init__(self, factors: List[Factor], **kwargs):
        super().__init__(**kwargs)
        self.factors = factors


class Polynomial(Expression):
    def __init__(self, terms: List[Monomial], **kwargs):
        super().__init__(**kwargs)
        self.terms = terms
