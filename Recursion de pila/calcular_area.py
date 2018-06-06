import math

def CalcularArea () :
        area = 0
        valor = input ("Ingrese el valor del radio")
        radio = int (valor)
        if radio > 0 :
            area = (radio ** 2) * math.pi
            print ("El valor del area es " , area)
        else:
            print ("El valor del radio no es mayor a cero")
            
