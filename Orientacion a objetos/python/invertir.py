#Ingresar una lista y regresarla con el orden invertido

class Invertir:
    def __init__(self):
        pass

def invertir(self,lista):
    if isinstance(lista, list):
         return self.invertir_aux(lista)
    else:
        return "Error: el valor ingresado no es una lista"

def invertir_aux(self,lista):
    if lista == []:
        return []
    else:
        return self.invertir_aux(lista[1:]) + [lista[0]]



 

