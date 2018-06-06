
def revise_num(num):
    if isinstance (num, int):
        entre0y4 = lambda digito : digito<=4
        entre5y9 = lambda digito : digito>=5
        return revise_aux(num, entre0y4), revise_aux(num, entre5y9)
    else: return "Error"

def entreCeroyCuatro(digito):
    return digito <= 4

def entreCincoyNueve(digito):
    if digito >= 5:
        return True
    else: return False

def revise_aux(num, condicion):
    if num == 0:
        return 0
    elif condicion(num % 10):
        return 1 + revise_aux (num // 10, condicion)
    else: return revise_aux (num // 10, condicion)
        
