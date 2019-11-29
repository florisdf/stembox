"""Representing and solving problems with polynomials."""
from typing import List
from ..expression import Expression
from copy import deepcopy
from ...stembox import Solution, Step, Explanation
from ..factor import Factor, Variable, Power, Fraction, Number
from ..logic import Equivalence
from . import explans as xpl


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
        return [self.get_at_path(path)
                for path in self._get_var_paths()]

    def _get_no_expon_var_paths(self) -> List[str]:
        """Return the paths of the variables that lack an exponent."""
        return [p for p in self._get_var_paths()
                if not p.endswith('.base')]

    def _get_no_expon_vars(self) -> List[Variable]:
        """Return the variables that lack an exponent."""
        return [self.get_at_path(path)
                for path in self._get_no_expon_var_paths()]

    def solve_vars(self) -> Solution:
        # PURPOSE
        purpose = Explanation(description=xpl.SEARCH_MONOM_VARS_PURP_DESCR())

        # EXECUTION
        monom_exe = deepcopy(self)

        for i, var in enumerate(monom_exe._get_vars()):
            var.label = xpl.SEARCH_MONOM_VARS_EXEC_LABEL(i + 1)
            var.mark = i

        execution = Explanation(illustration=monom_exe)

        # RESULT
        monom_res = deepcopy(monom_exe)
        for var in monom_res._get_vars():
            var.label = None

        result = Explanation(
            description=xpl.SEARCH_MONOM_VARS_RESULT_DESCR(
                monom_res._get_var_paths()),
            illustration=monom_res)

        return Solution([Step(purpose=purpose,
                              execution=execution,
                              result=result)])

    def solve_unit_var_exponent(self) -> Solution:
        """
        Return the solution for explicitely adding a unit exponent to all
        variables that do not have an exponent.
        """
        # PURPOSE
        purpose = Explanation(
            description=xpl.UNIT_VAR_EXPONENT_PURP_DESCR()
        )

        # EXECUTION
        for i, var in enumerate(self._get_no_expon_vars()):
            var.mark = i

        # Copy the monomial and, in the old monomial, label the variables that
        # do not have an exponent
        old_monom = deepcopy(self)
        for i, p in enumerate(old_monom._get_no_expon_var_paths()):
            var = old_monom.get_at_path(p)
            var.label = xpl.UNIT_VAR_EXPONENT_EXEC_LABEL()

        # In the new monomial, i.e. `self`, wrap Powers around variables
        for i, p in enumerate(self._get_no_expon_var_paths()):
            var = self.get_at_path(p)
            self.set_at_path(p, Power(base=var, exponent=Number(1)))

        execution = Explanation(
            description=xpl.UNIT_VAR_EXPONENT_EXEC_DESCR(),
            illustration=Equivalence([old_monom, deepcopy(self)])
        )

        # RESULT
        result = Explanation(
            decription=xpl.UNIT_VAR_EXPONENT_RESULT_DESCR(),
            illustration=deepcopy(self))

        return Solution([Step(purpose=purpose, execution=execution,
                              result=result)])

    def solve_var_expons(self) -> Solution:
        """Return the solution for finding the exponents of each variable"""
        # First step: write 1 at variables with no power
        solution = self.solve_unit_var_exponent()

        var_paths = self._get_var_paths()

        # PURPOSE
        purpose = Explanation(
            description=xpl.SEARCH_VAR_EXPON_PURP_DESCR(len(var_paths)))

        # EXECUTION
        var_expons = {}
        monom_exe = deepcopy(self)
        for i, var_path in enumerate(var_paths):
            if var_path.endswith('.base'):
                pow_path = var_path[:var_path.rfind('.base')]
                power = eval(f'{self}{pow_path[1:]}')
                power.exponent.mark = power.base.mark
                power.exponent.label = xpl.SEARCH_VAR_EXPON_EXEC_LABEL(
                    var_path)
                var_expons[var_path] = pow_path
        execution = Explanation(illustration=monom_exe)

        # RESULT

        solution.append(Step(purpose=purpose, execution=execution))
        return solution

    def solve_grade(self) -> Solution:
        # Find variables
        # var_sol = self.solve_vars()

        # Find exponents of variables
        # Sum exponents
        pass
