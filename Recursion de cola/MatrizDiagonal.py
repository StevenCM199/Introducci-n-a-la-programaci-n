def suma(matriz):
    if isinstance(matriz,list) and matriz !=[]:
        return matriz_aux(matriz, 0, 0)
    else:return "La matriz no es una lista"

def matriz_aux(matriz, indice, resultado):
    if len(matriz) == indice:
        return resultado
    else:
        return matriz_aux(matriz, indice + 1,(resultado + matriz[indice][indice]))
    
