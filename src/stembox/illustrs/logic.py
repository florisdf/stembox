"""Illustrations for logic constructs like equivalences and implications"""
from .expression import Expression
from typing import List


__all__ = [
    'Implication', 'Equivalence'
]


class Implication(Expression):
    """Expressions where the previous always implies the next.

    Args:
        expressions (List[Expression]): the expressions where the previous
        implies the next
    """
    def __init__(self, expressions: List[Expression], **kwargs):
        super().__init__(**kwargs)
        self.expressions = expressions


class Equivalence(Expression):
    """Expressions where the previous is always equivalent to the next.

    Args:
        expressions (List[Expression]): the expressions where the previous
        is equivalent to the next
    """
    def __init__(self, expressions: List[Expression], **kwargs):
        super().__init__(**kwargs)
        self.expressions = expressions
