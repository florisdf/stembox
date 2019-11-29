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


def _get_var_paths(monomial: Monomial) -> List[str]:
    vars = []
    for i, f in enumerate(monomial.factors):
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


def _get_vars(monomial: Monomial) -> List[Variable]:
    return [monomial.get_at_path(path)
            for path in _get_var_paths(monomial)]


def _get_no_expon_var_paths(monomial: Monomial) -> List[str]:
    """Return the paths of the variables that lack an exponent."""
    return [p for p in _get_var_paths(monomial)
            if not p.endswith('.base')]


def _get_no_expon_vars(monomial: Monomial) -> List[Variable]:
    """Return the variables that lack an exponent."""
    return [monomial.get_at_path(path)
            for path in _get_no_expon_var_paths(monomial)]


def solve_vars(monomial: Monomial) -> Solution:
    """Return the solution for finding the variables in the given monomial.
    """
    # PURPOSE
    purpose = Explanation(description=xpl.SEARCH_MONOM_VARS_PURP_DESCR())

    # EXECUTION
    monom_exe = deepcopy(monomial)

    for i, var in enumerate(_get_vars(monom_exe)):
        var.label = xpl.SEARCH_MONOM_VARS_EXEC_LABEL(i + 1)
        var.mark = i

    execution = Explanation(illustration=monom_exe)

    # RESULT
    monom_res = deepcopy(monom_exe)
    for var in _get_vars(monom_res):
        var.label = None

    result = Explanation(
        description=xpl.SEARCH_MONOM_VARS_RESULT_DESCR(
            _get_var_paths(monom_res)),
        illustration=monom_res)

    return Solution([Step(purpose=purpose,
                          execution=execution,
                          result=result)])


def solve_unit_var_exponent(monomial: Monomial) -> Solution:
    """
    Return the solution for explicitely adding a unit exponent to all
    variables that do not have an exponent.
    """
    no_expon_vars = _get_no_expon_var_paths(monomial)

    if len(no_expon_vars) == 0:
        # All variables have an exponent, so return a Solution without any
        # steps
        return Solution()

    # PURPOSE
    purpose = Explanation(
        description=xpl.UNIT_VAR_EXPONENT_PURP_DESCR()
    )

    # EXECUTION
    for i, var in enumerate(no_expon_vars):
        var.mark = i

    # Copy the monomial and, in the old monomial, label the variables that
    # do not have an exponent
    old_monom = deepcopy(monomial)
    for i, p in enumerate(_get_no_expon_var_paths(old_monom)):
        var = old_monom.get_at_path(p)
        var.label = xpl.UNIT_VAR_EXPONENT_EXEC_LABEL()

    # In the new monomial, wrap Powers around variables
    new_monomial = deepcopy(monomial)
    for i, p in enumerate(_get_no_expon_var_paths(new_monomial)):
        var = new_monomial.get_at_path(p)
        new_monomial.set_at_path(p, Power(base=var, exponent=Number(1)))

    execution = Explanation(
        description=xpl.UNIT_VAR_EXPONENT_EXEC_DESCR(),
        illustration=Equivalence([old_monom, deepcopy(new_monomial)])
    )

    # RESULT
    result = Explanation(
        decription=xpl.UNIT_VAR_EXPONENT_RESULT_DESCR(),
        illustration=deepcopy(new_monomial))

    return Solution([Step(purpose=purpose, execution=execution,
                          result=result)])


def solve_var_expons(monomial: Monomial) -> Solution:
    """Return the solution for finding the exponents of each variable"""
    # 1. Write 1 as exponent of variables with no exponent
    solution = solve_unit_var_exponent(monomial)

    # 2. Mark the exponents
    if len(solution) > 0:
        monomial = deepcopy(solution[-1].result.illustration)
    var_paths = _get_var_paths(monomial)

    # PURPOSE
    purpose = Explanation(
        description=xpl.SEARCH_VAR_EXPON_PURP_DESCR(len(var_paths)))

    # EXECUTION
    var_expons = {}
    monom_exe = deepcopy(monomial)
    for i, var_path in enumerate(var_paths):
        if var_path.endswith('.base'):
            pow_path = var_path[:var_path.rfind('.base')]
            power = eval(f'{monomial}{pow_path[1:]}')
            power.exponent.mark = power.base.mark
            power.exponent.label = xpl.SEARCH_VAR_EXPON_EXEC_LABEL(
                var_path)
            var_expons[var_path] = pow_path
    execution = Explanation(illustration=monom_exe)

    # RESULT
    result = Explanation(
        description=xpl.SEARCH_VAR_EXPON_RESULT_DESCR(var_expons),
        illustration=deepcopy(monom_exe))

    solution.append(Step(purpose=purpose,
                         execution=execution,
                         result=result))
    return solution


def solve_grade(monomial: Monomial) -> Solution:
    # Find variables
    # var_sol = solve_vars(monomial)

    # Find exponents of variables
    # Sum exponents
    pass
