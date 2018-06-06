def sumar (lista):
    if isinstance (lista, list):
        return sumar_lista(lista)
    else: return "El valor ingresado no es una lista"

def sumar_lista(lista):
    if lista == []:
        return 0
    elif isinstance (lista[0],list):
        return sumar_lista(lista[0]) + sumar_lista(lista[1:])
    else: return lista[0] + sumar_lista(lista[1:])
