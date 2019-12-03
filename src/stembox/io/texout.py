from ..illustrs import Expression
from ..illustrs import Equation
from ..illustrs import Equivalence, Implication
from ..illustrs import Monomial, Polynomial
from ..illustrs import Factor, Sign, Variable, Brackets, Number
from ..illustrs import Fraction, Power, Root


def render_variable(variable: Variable):
    return variable.symbol


def render_brackets(brackets: Brackets):
    return f'({render_factor(brackets.content)})'


def render_number(number: Number):
    return f'{number.absvalue}'


def render_fraction(frac: Fraction):
    return f'\\frac{{{frac.numerator}}}{{{frac.denominator}}}'


def render_power(pow: Power):
    if (isinstance(pow.base, Polynomial)
            or isinstance(pow.base, Monomial)
            or isinstance(pow.base, Fraction)):
        return (f'{{({render_expression(pow.base)})^'
                f'{{{render_expression(pow.exponent)}}}')
    else:
        return (f'{{{render_factor(pow.base)}}}^'
                f'{{{render_factor(pow.exponent)}}}')


def render_root(root: Root):
    if root.index == 2:
        return f'\\sqrt{{{root.radicand}}}'
    else:
        return f'\\sqrt[{root.index}]{{{root.radicand}}}'


def render_factor(factor: Factor):
    sign_tex = '' if factor.sign == Sign.POSITIVE else '-'

    if isinstance(factor, Variable):
        fac_tex = render_variable(factor)
    elif isinstance(factor, Brackets):
        fac_tex = render_brackets(factor)
    elif isinstance(factor, Number):
        fac_tex = render_number(factor)
    elif isinstance(factor, Fraction):
        fac_tex = render_fraction(factor)
    elif isinstance(factor, Power):
        fac_tex = render_power(factor)
    elif isinstance(factor, Root):
        fac_tex = render_root(factor)
    else:
        raise ValueError(f'Factor rendering of type {type(factor)} '
                         'is not supported')
    return sign_tex + fac_tex


def render_monomial(monom: Monomial, implicit_multiply=True):
    """
    Args:
        monom (Monomial): the monomial to render
        implicit_multiply (bool): whether to implicitly multiply when
        applicable
    """
    facs = monom.factors
    tex = render_factor(facs[0])

    for prev_fac, cur_fac in zip(facs, facs[1:]):
        if (isinstance(prev_fac, Number)
                and isinstance(cur_fac, Number)):
            tex += '\\cdot ' + render_factor(cur_fac)
        elif implicit_multiply:
            tex += render_factor(cur_fac)
        else:
            tex += '\\cdot ' + render_factor(cur_fac)

    return tex


def render_polynom(polynom: Polynomial, implicit_multiply=True):
    """Render the given `Polynomial` into LaTeX format.

    Args:
        monom (Monomial): the monomial to render
        implicit_multiply (bool): whether to implicitly multiply when
        applicable
    """
    terms = polynom.terms
    tex = render_monomial(terms[0])

    for term in terms[1:]:
        if term.factors[0].sign == Sign.POSITIVE:
            tex += f'+{render_monomial(term)}'
        else:
            tex += render_monomial(term)

    return tex


def render_equation(eqn: Equation):
    return (render_expression(eqn.lhs)
            + '='
            + render_expression(eqn.rhs))


def render_equivalence(equiv: Equivalence):
    return r'\Leftrightarrow '.join([render_expression(expr) + r'\\' + '\n'
                                     for expr in equiv.expressions])


def render_implication(impl: Implication):
    return r'\Rightarrow '.join([render_expression(expr) + r'\\' + '\n'
                                 for expr in impl.expressions])


def render_expression(expr: Expression):
    """Render the given `Expression` into LaTeX format."""
    if isinstance(expr, Polynomial):
        return render_polynom(expr)
    elif isinstance(expr, Monomial):
        return render_monomial(expr)
    elif isinstance(expr, Factor):
        return render_factor(expr)
    elif isinstance(expr, Equation):
        return render_equation(expr)
    elif isinstance(expr, Equivalence):
        return render_equivalence(expr)
    elif isinstance(expr, Implication):
        return render_implication(expr)
    else:
        raise ValueError(f'Rendering of Expression of type '
                         f'{type(expr)} is not supported')
