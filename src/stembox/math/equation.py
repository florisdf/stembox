from .expression import Expression


class Equation(Expression):
    def __init__(self, lhs: Expression, rhs: Expression, **kwargs):
        super().__init__(**kwargs)
        self.lhs = lhs
        self.rhs = rhs
