#Crear una traspuesta de una matriz dada (voltear filas a columnas)


def trasp(matriz):
    if isinstance(matriz,list) and matriz !=[]:
        return trasp_aux(matriz, len(matriz), len(matriz[0]), 0 , 0, 0, 0)
    else:return "La matriz no es una lista"

def trasp_aux(matriz, num_filas, num_columnas, fila, columna, matrizTras, ind):
    if filas == num_filas:
        return trasp_aux(matriz, num_filas, num_columnas, 0, columna + 1, matrizTraz[ind], ind + 1)
    else: return trasp_aux(matriz, num_filas, num_columnas, fila + 1, columna, ([matrizTraz[ind] + matriz[fila][columna], ind))

