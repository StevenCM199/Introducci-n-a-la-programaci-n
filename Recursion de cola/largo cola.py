def largo (num):
    if isinstance(num,int):
        return largo_aux(num,0)
    else:
        return "Error: el número no es un entero"

def largo_aux(num,resultado):
    if (num == 0):
        return resultado
    else:
        return largo_aux(num // 10, resultado+1)
        
