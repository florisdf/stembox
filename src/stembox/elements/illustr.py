from dataclasses import dataclass


__all__ = [
    'Illustration', 'ListIllustration'
]


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


class ListIllustration(list, Illustration):
    """An `Illustration` composed of multiple `Illustration`s
    """
