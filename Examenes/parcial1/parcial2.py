def palindromo(num):
    if isinstance (num,int) and num > 0:
        contador = contarDigitos(num) -1
        nuevo = palindromo_aux (num,contador)
        if (num == nuevo):
            return True
        else: return False
    else:
        return "El numero no es valido"
    
def contarDigitos(num):
    if num == 0:
        return 0
    else:
        return 1 + contarDigitos(num//10)

def palindromo_aux(num,contador):
    if num == 0:
        return 0
    else:
        return (num%10)*(10**contador) + palindromo_aux(num//10,contador-1) 
