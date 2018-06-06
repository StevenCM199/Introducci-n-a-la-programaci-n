
def sumar (lista):
    if isinstance (lista, list):
        return sumar_lista(lista, 0)
    else: return "El valor ingresado no es una lista"


def sumar_lista(lista, pot):
    if lista == []:
        return 0
    elif isinstance (lista[0],list):
        return sumar_lista(lista[0], pot) + sumar_lista(lista[1:], pot + len(lista[0]))
    else: return lista[0]**(pot + 1) + sumar_lista(lista[1:], pot + 1)
