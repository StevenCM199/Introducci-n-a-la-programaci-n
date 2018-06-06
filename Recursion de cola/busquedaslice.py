#Devolver "True" si el digito de "num" esta presente en la lista
#Si no es asi, devolver "False"

def busqueda(num, lista):
    if isinstance (num,int) and (lista,list):
        return busqueda_aux(num, lista)
    else:
        return "Error" 

def busqueda_aux(num, lista):
    if lista == []:
        return False
    elif num == lista[0]:
        return True
    else:
        return busqueda_aux(num, lista[1:])
