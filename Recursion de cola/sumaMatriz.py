def suma_matriz(matriz):
    if isinstance(matriz,list) and matriz !=[]:
        return matriz_aux(matriz, len(matriz), len(matriz[0]) ,0,0,0)
    else:return "La matriz no es una lista"

def matriz_aux(matriz, num_filas, num_columnas, fila, columna, resultado):
    if fila == len(matriz):
        return resultado
    elif columna == len(matriz[0]):
        return matriz_aux(matriz, num_filas, num_columnas, fila + 1 , 0, resultado)
    else: return matriz_aux(matriz, num_filas, num_columnas, fila, columna + 1, resultado + matriz[fila][columna])
