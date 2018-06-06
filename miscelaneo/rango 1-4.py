#Verifica que todos los digitos del numero se encuentran entre 0 y 4
#Verdadero: si alguno de los digitos no esta entre 0 y 4
#Falso: si alguno de los digitos no esta entre 0 y 4

def rango (num):
    if (num == 0):
        return True
    else:
        if ((num % 10) >= 0) and ((num % 10) <= 4):
            return rango (num // 10)
        else:
            return False
