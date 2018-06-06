#Sumatoria de un numero 


def sumatoria(n):
  if isinstance (n,int) and n >=1:
      return sumatoria_aux(n)
  else: return "Error"

  
def sumatoria_aux (n):
  if n == 0:
    return 0
  else:
    return n + sumatoria_aux (n-1)
