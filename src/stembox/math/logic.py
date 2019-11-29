"""Illustrations for logic constructs like equivalences and implications"""
from ..stembox import Illustration
from .expression import Expression
from typing import List


class Implication(Illustration):
    """Expressions where the previous always implies the next.

    Args:
        expressions (List[Expression]): the expressions where the previous
        implies the next
    """
    def __init__(self, expressions: List[Expression], **kwargs):
        super().__init__(**kwargs)
        self.expressions = expressions


class Equivalence(Illustration):
    """Expressions where the previous is always equivalent to the next.

    Args:
        expressions (List[Expression]): the expressions where the previous
        is equivalent to the next
    """
    def __init__(self, expressions: List[Expression], **kwargs):
        super().__init__(**kwargs)
        self.expressions = expressions
