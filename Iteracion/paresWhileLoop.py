#Agrupar numeros entre listas de pares e impares
#Usando While

def pares(num):
    if isinstance(num , int) and num >= 0:
        return pares_impares_aux(num)

def pares_impares_aux(num):
    listaPares = []
    listaImpares = []
    while num > 0:
        digi = num % 10
        if (digi % 2 == 0): 
            listaPares += [digi]
        else: listaImpares += [digi]
        num = num // 10
    return listaPares, listaImpares
