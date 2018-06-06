
def repite (lista, num):
    if isinstance (lista, list) and (num, int):
        repetir = lambda n : n == num  
        return repite_aux (lista, repetir)

def repite_aux (lista, condicion):
    if lista == []:
        return 0
    elif condicion (lista[0]):
        return 1 + repite_aux (lista[1:], condicion)
    else: return repite_aux (lista[1:], condicion)
