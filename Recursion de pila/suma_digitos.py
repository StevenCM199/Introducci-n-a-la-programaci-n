#Entrada: es un numero entero
#Restricciones: es un entero mayor a cero
#Salida: suma de los digitos

#Codigo de comprobacion (comprueba las restricciones que debe llevar el numero)
def suma_digitos(num):
    if isinstance (num,int) and (num > 0)
        return suma_digitos_aux (abs(num))
    else:
        return "Error"

#Codigo de funcion (ejecuta la operacion)
def suma_digitos_aux (num):
    if (num == 0):
        return 0
    else:
        return num % 10 + suma_digitos_aux (num // 10)
