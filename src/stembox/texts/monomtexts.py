# Searching the variables in a monomial
def SEARCH_MONOM_VARS_PURPOSE_DESCR():
    return ('Zoek de [variabelen](/lessen/wiskunde/veeltermen/variabelen/) '
            'in de eenterm')


def SEARCH_MONOM_VARS_EXEC_LABEL(var_idx):
    return f'variabele {var_idx}'


def SEARCH_MONOM_VARS_RESULT_DESCR(var_paths):
    var_link = '![gevonden variabele]({0} "variabele")'

    if len(var_paths) == 1:
        descr = 'De variabele is ' + var_link.format(var_paths[0])
    else:
        descr = 'De variabelen zijn '
        descr = descr + ', '.join([var_link.format(p)
                                   for p in var_paths[:-1]])
        descr = descr + ' en ' + var_link.format(var_paths[-1])

    return descr


# Explicitely writing unit variable exponents where necessary
def UNIT_VAR_EXPONENT_PURPOSE_DESCR():
    return 'Zorg dat elke variabele een expliciete exponent heeft'


def UNIT_VAR_EXPONENT_EXEC_LABEL():
    return 'zonder exponent'


def UNIT_VAR_EXPONENT_EXEC_DESCR():
    return ('Schrijf een exponent van 1 '
            + f'bij de variabelen zonder exponent\n\n'
            + '![variabelen exponent van 1 geven]($)')


def UNIT_VAR_EXPONENT_RESULT_DESCR():
    return ('We schrijven de eenterm als ![nieuwe eenterm]($)')


# Searching the exponents of the monomial variables
def SEARCH_VAR_EXPON_PURPOSE_DESCR(num_vars):
    """
    Args:
        num_vars (int): the number of variables
    """
    return f'Zoek de exponent van de variabele{"n" if num_vars > 1 else ""}'


def SEARCH_VAR_EXPON_EXEC_LABEL(var_path):
    """
    Args:
        var_path (str): the illustration path of the variable where the
        exponent belongs to
    """
    return f'exponent van ![gevonden exponent]({var_path} "exponent")'


def SEARCH_VAR_EXPON_RESULT_DESCR(var_expons):
    """
    Args:
        var_expons (dict): a dictionary with the illustration path of the
        variable as key and the illustration path of the corresponding exponent
        as value.
    """
    descr = 'De exponent van '

    if len(var_expons) == 1:
        descr += (f'![variabele]({list(var_expons.keys())[0]}) '
                  + 'is ' + f'[exponent]({list(var_expons.items())[0]})')
    else:
        descrs = [f'![variabele]({var_path}) is ![exponent]({expon_path})'
                  for var_path, expon_path in var_expons.items()]
        descr += descrs[0]
        descr += ', die van '.join(descrs[1:-1])
        descr += ' en die van ' + descrs[-1]
    return descr


# Add exponents
def ADD_EXPONENTS_PURPOSE_DESCR():
    return 'Tel de exponenten op'


def ADD_EXPONENTS_EXEC_ILLUSTR_LABEL(var_path: str):
    return f'exponent van ![variabele]({var_path})'


def ADD_EXPONENTS_EXEC_DESCR(eqn_path: str):
    """
    Args:
        eqn_path (str): the illustration path to the equation displaying the
        summation of the exponents
    """
    return f'![optelling van de exponenten]({eqn_path})'


def ADD_EXPONENTS_RESULT_DESCR(result_path: str):
    """
    Args:
        result_path (str): the illustration path of the result of summing the
        exponents
    """
    return f'De som van de exponenten is ![som van exponenten]({result_path})'


# Find grade of monomial
def FIND_MONOMIAL_GRADE_PURPOSE_DESCR():
    return 'Zoek de graad van de eenterm'


def FIND_MONOMIAL_GRADE_RESULT_DESCR(grade_path):
    return f'De graad van de eenterm is ![graad van eenterm]({grade_path})'
