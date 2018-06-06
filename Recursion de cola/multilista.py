#Multiplicar los elementos de una lista por el resultado
#de multiplicaciones previas usando slicing

def multilista(n):
    if isinstance (n,list) and n !=[]:
        return multilista_aux(n,1)
    else:
        return "Error: el valor introducido no es una lista"

def multilista_aux(n,result):
    if n == []:
        return result
    else:
        return multilista_aux(n[1:],result*n[0])
