from dataclasses import dataclass
from typing import List
from .step import Step


__all__ = [
    'Solution'
]


@dataclass
class Solution:
    """A Directed Acyclic Graph (DAG) of `Step`s solving a given problem.

    Args:
        steps (List[Step]): a list of steps that lead to the solution
        value: a python object that contains the value of the solution. This is
        useful for when the value of the solution is needed for subsequent
        problems.
    """
    def __init__(self, steps: List[Step] = [], value=None):
        self.steps = steps
        self.value = value

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

        return self.steps[-1].result.description.short
