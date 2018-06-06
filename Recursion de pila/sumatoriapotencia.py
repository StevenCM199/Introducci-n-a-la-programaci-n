#Sumatoria de un numero elevado a la tercera potencia y multiplicado por 3


def sumatoria3(n):
  if isinstance (n,int) and n >=1:
      return sumatoria3_aux(n)
  else: return "Error"
  

def sumatoria3_aux (n):
  if n == 0:
    return 0

  else:
    return (n * n**3) + sumatoria3_aux (n-1)
