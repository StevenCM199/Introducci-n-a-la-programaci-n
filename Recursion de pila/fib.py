#Calcular la serie de Fibonacci para un numero


def fib(n):
  if isinstance (n,int):
        return fib_aux(n)
  else: return "Error"


def fib_aux(n):
  if n == 0:
      return 1 
  elif n == 1:
      return 1
  else:   
      return fib(n-1) + fib(n-2) 

