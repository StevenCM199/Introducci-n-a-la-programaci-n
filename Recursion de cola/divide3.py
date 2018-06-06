#Recibir un numero y eliminar los digitos divisibles entre 3

def divide3 (num):
    if isinstance(num,int):
        return divide3_aux(num,0,0)
    else:
        return "Error: el número no es un entero"

def divide3_aux(num,resultado,pot):
    if (num == 0):
        return resultado
    elif (num%10) % 3 == 0:
        return divide3_aux(num//10, resultado, pot)                    
    else:
        return divide3_aux(num//10, resultado+num%10*(10**pot),pot+1)
    

