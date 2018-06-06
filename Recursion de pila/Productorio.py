#Productorio de un numero elevado a n y restado entre 2 


def productorio(n):
  if isinstance (n,int) and n >=1:
      return productorio_aux(n)
  else: return "Error"

  
def productorio_aux (n):
  if n == 0:
    return 1
  else:
    return (3**n-2) * productorio_aux (n-1)
