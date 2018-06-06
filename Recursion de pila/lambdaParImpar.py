
def revise(num):
    if isinstance (num, int):
        par = lambda digito : ((digito % 10) % 2) == 0
        impar = lambda digito : ((digito % 10) % 2) == 1
        return revise_aux(num, par), revise_aux(num, impar)
    else: return "Error"

def revise_aux(num, condicion):
    if num == 0:
        return 0
    elif condicion(num % 10):
        return 1 + revise_aux (num // 10, condicion)
    else:
        return revise_aux (num // 10, condicion)


