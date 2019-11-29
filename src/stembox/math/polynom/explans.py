# Searching the variables in a monomial
def SEARCH_MONOM_VARS_PURPOSE_DESCR():
    return ('Zoek de [variabelen](/lessen/wiskunde/veeltermen/variabelen/) '
            'in de eenterm')


def SEARCH_MONOM_VARS_EXEC_LABEL(var_idx):
    return f'variabele {var_idx}'


def SEARCH_MONOM_VARS_RES_DESCR(var_paths):
    var_link = '!(gevonden variabele)[{0} "variabele"]'

    if len(var_paths) == 1:
        descr = 'De variabele is ' + var_link.format(var_paths[0])
    else:
        descr = 'De variabelen zijn '
        descr = descr + ', '.join([var_link.format(p)
                                   for p in var_paths[:-1]])
        descr = descr + ' en ' + var_link.format(var_paths[-1])

    return descr


# Explicitely writing unit variable exponents where necessary
def UNIT_VAR_EXPONENT_PURP_DESCR():
    return 'Zorg dat elke variabele een expliciete exponent heeft'


def UNIT_VAR_EXPONENT_EXEC_LABEL():
    return 'zonder exponent'


def UNIT_VAR_EXPONENT_EXEC_DESCR():
    return ('Schrijf een exponent van 1 '
            + f'bij de variabelen zonder exponent\n\n'
            + '!(variabelen exponent van 1 geven)[$]')


# Searching the exponents of the monomial variables
def SEARCH_VAR_EXPON_PURP_DESCR(num_vars):
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
    return f'exponent van !(gevonden exponent)[{var_path} "exponent"]'


def SEARCH_VAR_EXPON_RES_DESCR(var_expons):
    """
    Args:
        var_expons (dict): a dictionary with the illustration path of the
        variable as key and the illustration path of the corresponding exponent
        as value.
    """
    descr = 'De exponent van '

    if len(var_expons) == 1:
        descr = (descr + f'(variabele)[{list(var_expons.keys())[0]}] '
                 + 'is ' + f'(exponent)[{list(var_expons.items())[0]}]')
    else:
        pass

    return descr
