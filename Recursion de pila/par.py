#Sacar el numero de digitos pares e impares en una cifra.

def pares_impares(num):
    if isinstance (num, int) and (num > 0):
        return par(num) , impar(num)
    else:
        return "Error"

def par (num):
    if (num == 0): # Condicion de parada
        return 0
    else:
        if ((num % 10) % 2) == 0:
            return 1 + par (num // 10)
        else:
            return par (num // 10)

def impar(num):
    if (num == 0):
        return 0
    else:
        if ((num % 10) % 2) == 1:
            return 1 + impar (num // 10)
        else:
            return impar (num // 10)
