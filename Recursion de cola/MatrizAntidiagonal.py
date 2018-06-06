def suma(matriz):
    if isinstance(matriz,list) and matriz !=[]:
        return matriz_aux(matriz, 0,(len(matriz)-1), 0)
    else:return "La matriz no es una lista"

def matriz_aux(matriz, fila, indice, resultado):
    if indice == -1:
        return resultado
    else:
        return matriz_aux(matriz, fila + 1, indice - 1,(resultado + matriz[fila][indice]))
