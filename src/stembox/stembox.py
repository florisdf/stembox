"""The fundamental stembox elements."""
from dataclasses import dataclass
from typing import List


@dataclass
class Description:
    """Describes verbally what happens in a certain part of a step.

    A `Description` can contain links to urls or to the elements of any
    `Illustration` that is contained in the same series of steps. Note that a
    referenced `Illustration` need not have the same *level* as the
    `Description`. It can also be an `Illustration` in a *substep* or a
    *superstep*.

    Args:
        text (str): the description text
        short (str): (optional) a short version of the description text
    """
    text: str
    short: str = None


@dataclass
class Illustration:
    """Illustrates a verbal description.

    It could be a figure, but also an equation or a mathematical expression.
    """


@dataclass
class Explanation:
    """An abstract explanation with a description and an illustration."""
    descr: Description = None
    illus: Illustration = None


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


@dataclass
class Solution:
    """A Directed Acyclic Graph (DAG) of `Step`s solving a given problem."""
    def __init__(self):
        self.steps = []

    def __getitem__(self, idx):
        return self.steps[idx]

    def __iter__(self):
        return iter(self.steps)

    def __len__(self):
        return len(self.steps)

    @property
    def steps(self) -> List[Step]:
        return self._steps

    @steps.setter
    def steps(self, value):
        self._steps = value

    def clear(self):
        self.steps.clear()

    def append(self, step):
        self.steps.append(step)

    def __str__(self):
        if len(self.steps) == 0:
            return ''

        return self.steps[-1].result.descr.short
