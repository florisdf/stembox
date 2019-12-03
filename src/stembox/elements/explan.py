from dataclasses import dataclass
from .illustr import Illustration


__all__ = [
    'Explanation'
]


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

    def __init__(self, description: str = None, short: str = None,
                 illustration: Illustration = None):
        if description is None:
            description = '![]($)'

        self.description = description
        self.short = short
        self.illustration = illustration
