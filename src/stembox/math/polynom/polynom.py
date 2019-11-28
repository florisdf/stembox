"""Representing and solving problems with polynomials."""
from typing import List
from expression import Expression
from copy import deepcopy
from ...stembox import Solution, Step, Explanation
from factor import Factor, Variable, Power, Fraction
from explans import xpl


class Monomial(Expression):
    def __init__(self, factors: List[Factor]):
        self.factors = factors

    def _get_var_paths(self) -> List[str]:
        vars = []
        for i, f in enumerate(self.factors):
            path = '$.factors'
            if isinstance(f, Variable):
                path += f'[{i}]'
            elif isinstance(f, Power) and isinstance(f.base, Variable):
                path += f'[{i}].base'
            elif isinstance(f, Fraction) and isinstance(f.numerator, Variable):
                path += f'[{i}].numerator'
            else:
                continue
            vars.append(path)
        return vars

    def _get_vars(self) -> List[Variable]:
        return [eval(f'self{path[1:]}')
                for path in self._get_var_paths()]

    @property
    def vars(self) -> Solution:
        # PURPOSE
        purp = Explanation(descr=xpl.PURP_SEARCH_MONOM_VARS_DESCR())

        # EXECUTION
        monom_exe = deepcopy(self)

        for i, var in enumerate(monom_exe._get_vars()):
            var.label = xpl.EXEC_SEARCH_MONOM_VARS_LABEL(i + 1)
            var.mark = i

        exe = Explanation(illus=monom_exe)

        # RESULT
        monom_res = deepcopy(monom_exe)
        for var in monom_res._get_vars():
            var.label = None

        res = Explanation(
            descr=xpl.RES_SEARCH_MONOM_VARS_DESCR(monom_res._get_var_paths()),
            illus=monom_res)

        return Solution([Step(purpose=purp, execution=exe, result=res)])

    @property
    def grade(self) -> Solution:
        # Find variables
        # Find exponents of variables
        # Sum exponents
        pass
