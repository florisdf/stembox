"""
Module for general math expressions
"""


class Expression:
    """A general math expression."""

    @property
    def tex(self):
        """The TeX representation of the `Expression`."""
        raise NotImplementedError
