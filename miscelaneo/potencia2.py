#Mostrar todos los números de 2 elevado a la potencia de "n"

def potencia(n):
    if isinstance (n,int) and (n > 0):
        return potencia_aux(n)
    else:
        return "Error"

def potencia_aux(n):
    if n == 0:
        print (2 ** n , end = " ")
        return 0
    else:
        print (2 ** n , end = " ")
        return potencia_aux(n-1)
    
