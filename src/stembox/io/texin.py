"""Module for parsing a string into an Expression object."""
from ..elements import Expression


def parse(string: str) -> Expression:
    """Parse the given string into an Expression

    :param str string: the string to parse
    :returns: an Expression with the parsed Expression
    :rtype: Expression
    """
    # Group
