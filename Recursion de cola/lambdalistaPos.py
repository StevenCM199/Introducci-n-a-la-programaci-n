#Devolver True si en una lista no hay negativos, devolver False si en una lista hay negativos

def listaPos (lista):
    if isinstance (lista, list) and lista != []:
        negativo = lambda digito : digito < 0
        return listaPos_aux(lista, negativo)  
    else:
        return "Error: el valor ingresado no es una lista"


def listaPos_aux(lista, condicion):
    if lista == []:
        return True
    elif condicion (lista[0]):
        return False
    else:
        return listaPos_aux (lista[1:], condicion)
