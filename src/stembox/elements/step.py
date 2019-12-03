from dataclasses import dataclass
from .explan import Explanation


__all__ = [
    'Step'
]


@dataclass
class Step:
    """A single unit of an algorithm that solves a given problem.

    Args:
        purpose (Explanation): A purpose that explains which problem the step
        aims to solve
        execution (Explanation): An execution that shows and executes the
        method to solve the step;
        result (Explanation): A result that shows the step's solution(s);
        check (Explanation): A check that evaluates if the result is correct.
    """
    purpose: Explanation = None
    execution: Explanation = None
    result: Explanation = None
    check: Explanation = None
