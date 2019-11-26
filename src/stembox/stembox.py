"""The fundamental stembox elements."""
from dataclasses import dataclass
from typing import List


@dataclass
class Description:
    """
    A `Description` describes verbally what happens in a certain part of a
    step. It can contain links to urls or to the elements of any
    `Illustration` that is contained in the same series of steps. Note that a
    referenced `Illustration` need not have the same *level* as the
    `Description`. It can also be an `Illustration` in a *substep* or a
    *superstep*.
    """
    def __init__(self, text: str):
        # Compile the text
        raise NotImplementedError


@dataclass
class Illustration:
    """
    An `Illustration` illustrates a verbal description. It could be a figure,
    but also an equation or a mathematical expression.
    """


@dataclass
class Explanation:
    """
    An abstract explanation with a description and an illustration.
    """
    descr: Description = None
    illus: Illustration = None


class Purpose(Explanation):
    """
    Explains which problem a step aims to solve
    """


@dataclass
class Execution(Explanation):
    """
    Shows how the step-level problem can be solved.
    """
    steps: List[Step] = None


@dataclass
class Result(Explanation):
    """
    Shows the final solution of the step-level problem.
    """


@dataclass
class Step:
    """
    A `Step` consists of three parts:
        1. A `Purpose` that explains which problem the step aims to solve;
        2. One or more `Execution`s that show and execute methods to solve the
        problem;
        3. One or more `Result`s that show the final solution(s).
    """
    purpose: Purpose
    execution: Execution
    result: Result
