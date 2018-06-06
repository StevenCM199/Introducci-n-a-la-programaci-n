def es_magico(matriz):
    if isinstance(matriz,list):
        return sumar_fila(matriz,0,0,0,0)
    else: return "Error"

def sumar_fila(matriz,fila,columna,resultado,contador):
    if contador == len(matriz):
        return sumar_columna(matriz,0,0,0,0)
    if fila == len(matriz) - 1:
        return sumar_fila(matriz, 0, columna + 1, resultado, contador + 1)
    else: return sumar_fila(matriz, fila + 1 , columna, resultado + matriz[fila][columna], contador + 1)

def sumar_columna (matriz,fila, columna, resultado2, contador):
    if contador == len(matriz):
        return sumar_diagonal(matriz, 0, 0, 0, 0)
    elif columna == len(matriz) - 1:
        return sumar_columna(matriz, fila + 1, 0, resultado2,contador + 1)
    else: return sumar_columna(matriz,fila,columna + 1, resultado2 + matriz[fila] [columna], contador + 1)

def sumar_diagonal(matriz,fila,columna,resultado3,contador):
    if contador == len(matriz):
        return anti_diagonal(matriz,len(matriz)-1, 0, 0)
    else: return sumar_diagonal(matriz, fila + 1, columna + 1, resultado3 + matriz [fila] [columna], contador + 1)

def anti_diagonal(matriz,fila,columna, resultado4, contador):
    if contador == len(matriz):
        return sumaresultado(resultado,resultado2,resultado3,resultado4)
    else: return anti_diagonal(matriz, fila - 1, columna + 1, resultado4 + matriz[fila][columna], contador + 1)

def sumaresultados (resultado,resultado2,resultado3,resultado4):
    if (resultado - resultado3) - (resultado2 - resultado4) == 0:
        return True
    else:
        return False



