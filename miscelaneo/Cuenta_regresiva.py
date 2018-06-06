#Cuenta desde un numero determinado hasta que llega a 0

def cuenta_regresiva (valor):
    print (valor)
    if (valor > 0) : # Seguir - Verde
        cuenta_regresiva (valor - 1)

    else:
        if (valor <= 0) : # Parar - Rojo
            return 0
