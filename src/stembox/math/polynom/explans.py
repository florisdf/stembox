def PURP_SEARCH_MONOM_VARS_DESCR():
    return ('Zoek de [variabelen](/lessen/wiskunde/veeltermen/variabelen/) '
            'in de eenterm')


def EXEC_SEARCH_MONOM_VARS_LABEL(var_number):
    return f'variabele {var_number}'


def RES_SEARCH_MONOM_VARS_DESCR(var_paths):
    var_link = '!(gevonden variabele)[{0} "variabele"]'

    if len(var_paths) == 1:
        descr = 'De variabele is ' + var_link.format(var_paths[0])
    else:
        descr = 'De variabelen zijn '
        descr = descr + ', '.join([var_link.format(p) for p in var_paths[:-1]])
        descr = descr + ' en ' + var_link.format(var_paths[-1])

    return descr
