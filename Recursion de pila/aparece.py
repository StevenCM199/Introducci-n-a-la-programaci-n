#Saber cuantas digitos iguales aparecen en una cifra determinada


def aparece (num, digito):
    if isinstance (num, int) and (num > 0)  and isinstance (digito, int) and (digito > 0) and (digito < 9): 
        return aparece_aux (abs(num), digito)
    else:
        return "Error"

def aparece_aux (num, digito):
    if (num == 0) or (digito == 0):
        return 0
    else:
        if num % 10 == digito:
            return 1 + aparece_aux (num // 10 , digito)
        else:
            return aparece_aux (num // 10 , digito)
