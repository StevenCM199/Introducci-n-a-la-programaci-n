def intercambiar(lista):
    if lista == []:
        return []
    else: return [lista[1]] + [lista[0]] + intercambiar(lista[2:])
