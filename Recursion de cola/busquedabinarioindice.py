def busqueda(num, lista):
    if isinstance (num,int) and (lista,list):
        return busqueda_aux(num, lista, len(lista)//2)
    else:
        return "Error" 

def busqueda_aux(num, lista, mitad):
    
    if lista == []:
        return False
    
    elif num == lista[mitad]:
        return True
    
    elif num > lista[mitad]:
        return busqueda_aux(num,lista[(mitad + 1):], lista[mitad+1])
    
    elif num < lista[mitad]:
        return busqueda_aux(num, lista[:mitad], lista[:mitad])
    
