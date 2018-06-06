#Sumar todos los datos de una matriz y devolver su promedio


def suma_matriz(matriz):
    if isinstance(matriz,list) and matriz !=[]:
        return matriz_aux(matriz, len(matriz), len(matriz[0]) ,0,0,0)
    else:return "La matriz no es una lista"

def matriz_aux(matriz, num_filas, num_columnas, fila, columna, resultado):
    if fila == len(matriz):
        return promedio(resultado, (len(matriz)*len(matriz[0])),0)
    elif columna == len(matriz[0]):
        return matriz_aux(matriz, num_filas, num_columnas, fila + 1 , 0, resultado)
    else: return matriz_aux(matriz, num_filas, num_columnas, fila, columna + 1, resultado + matriz[fila][columna])

def promedio(suma, num_datos, resultado):
    if suma == 0:
        return suma, resultado
    else:
        return suma, resultado + suma / num_datos
    
