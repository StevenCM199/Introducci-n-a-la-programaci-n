#Verificar que un numero sea primo o compuesto (el 0 y el 1 no se consideran primos ni compuestos)

def validar(n):
    if isinstance (n, int) and (n > 1):
        return primo(n , n - 1)
    elif n == 0 or n == 1:
        return "Especial"

        
def primo(n , q): 
    if q == 1:
        return "Primo"
    elif n % q == 0:
        return "Compuesto"
    else: return primo(n , q - 1)


