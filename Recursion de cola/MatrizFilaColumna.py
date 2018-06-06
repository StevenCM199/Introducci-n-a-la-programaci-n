#Sumar los valores de la primera fila, los valores de la ultima fila,
#los valores de la primera columna y los valores de la ultima columna

def suma(matriz):
    if isinstance(matriz,list) and matriz !=[]:
        return matriz_aux(matriz, 0, 0, 0)
    else:return "La matriz no es una lista"

def matriz_aux(matriz, indice, indice2, suma):
    if len(matriz) == indice2:
        return suma
    else:
        return matriz_aux(matriz, indice, indice2 + 1,(suma + matriz[indice][indice2]))
