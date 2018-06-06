def intercambiar (n):
    if isinstance (n, int):
        return intercambiar_aux(n,0)
    else: return "Error"

def intercambiar_aux (n,pot):
    if n == 0:
        return 0
    else: return(n%100//10)*10**(pot) + n % 10 *10**(pot+1) + intercambiar_aux(n//100, pot+2)
