def EsNumero(letra):
    R = False
    #dice si es una vocal
    if letra.isdigit():
        R = True
    else:
        R = False
    return R
def EsVocal(letra):
    R = False
    vocales = "aeiouAEIOU"
    for i in vocales:
        if letra == i:
            R = True
    return R