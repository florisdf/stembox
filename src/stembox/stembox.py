"""The fundamental stembox elements."""
from dataclasses import dataclass
from typing import List


@dataclass
class Illustration:
    """Illustrates a verbal description.

    It could be a figure, but also an equation or a mathematical expression.

    Args:
        label (str): (optional) a label that provides some extra information
        mark (int): (optional) a global mark id that allows e.g. to give the
        same color to two occurences of the same variable or to show which
        terms have changed during a calculation.
    """
    label: str = None
    mark: int = None

    def get_at_path(self, path: str):
        """Return the illustration element that corresponds to the given path.

        Args:
            path (str): the path to the illustration element, e.g.
            `"$.factors[0]"`. The root `Illustration` object is represented
            with `$`.
        """
        return eval(f'self{path[1:]}', {'self': self})

    def set_at_path(self, path: str, val):
        """Put the object in the given illustration path.

        Args:
            path (str): the path where to put the `val`, e.g. `"$.factors[0]"`.
            The root `Illustration` object is represented with `$`.
            val (Illustration): the object to put at the `path`
        """
        eval(f'self{path[1:]} = val', {'self': self})


@dataclass
class Explanation:
    """An abstract explanation with a description and an illustration.

    Args:
        description (str): (optional) Describes what happens in a certain part
        of a step by using a Markdown syntax. The description can contain
        elements of the given illustration by using the Markdown image syntax,
        e.g.  `'![alt text]($.factors[0] "Title Text")'`. Note that the url
        part is replaced by Python code that leads to the element of the
        illustration.  The root `Illustration` object is represented with `$`.

        If `description` is `None`, the whole illustration will be used. This
        is equivalent to passing `'!()[$]'` as `description`.
        short (str): (optional) An abbreviated version of the description
        illustration (Illustration): (optional) the illustration to which the
        explanation can refer
    """
    description: str = None
    short: str = None
    illustration: Illustration = None


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
    def __init__(self, steps=[]):
        self.steps = steps

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
