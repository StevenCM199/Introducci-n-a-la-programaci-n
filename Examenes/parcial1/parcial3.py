def contarConsonantes(palabra):
    if isinstance (palabra,str):
        return contarConsonantes_aux(palabra)
    else:
        return "El valor introducido no es valido" 

def contarConsonantes_aux(palabra):
    if palabra == '':
        return 0
    elif (palabra[0] == 'a') or (palabra[0] == 'e') or (palabra[0] == 'i') or (palabra[0] == 'o') or (palabra[0] == 'u'):
        return contarConsonantes_aux(palabra[1:])
    else:
        return 1 + contarConsonantes_aux(palabra[1:])
    
