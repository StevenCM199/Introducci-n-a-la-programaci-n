def consecutivos(matriz):
    if isinstance(matriz,list) and matriz !=[]:
        return consecutivos_aux(matriz,0,0,1)
    else:
        return "Error"

def consecutivos_aux(matriz, fila, columna, numero):
    if numero == len(matriz) * len(matriz) and fila == len(matriz):
        return True
    if numero != len(matriz) * len(matriz) and fila == len(matriz):
        return False
    elif matriz[fila] [columna] == numero:
        return consecutivos_aux(matriz,0,0,numero + 1)
    else:
        return consecutivos_aux(matriz, fila, columna + 1, numero)
    if columna == len(matriz[0]) - 1:
        return consecutivos_aux(matriz,fila + 1,0,numero)
