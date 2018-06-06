#Comprobar si hay un cero en una lista

def lista0 (lista):
    if isinstance (lista, list):
        cero = lambda digito : digito == 0 
        return lista0_aux(lista, cero)
    else:
        return "Error: el valor ingresado no es una lista"

def lista0_aux (lista, condicion):
    if lista == []:
        return False
    elif condicion (lista[0]):
        return True 
    else: return lista0_aux (lista[1:], condicion)
    
