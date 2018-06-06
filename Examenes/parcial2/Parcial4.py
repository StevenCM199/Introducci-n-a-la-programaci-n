def rotar(matriz):
    if isinstance (matriz, list):
        return rotar_aux(matriz,0,len(matriz[0]) - 1, 1, [])
    else: return "Error"

def rotar_aux(matriz, fila, columna, contador, nuevaMatriz):
    if contador == len(matriz) * len(matriz):
        return nuevaMatriz
    elif fila == len(matriz) - 1:
        return rotar_aux(matriz, 0, columna - 1, contador + 1, nuevaMatriz + [fila])
    else:
        return rotar_aux(matriz, fila + 1, columna, contador + 1, nuevaMatriz)
