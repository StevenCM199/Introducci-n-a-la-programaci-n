def invertir(lista):
    if isinstance (lista,list):
        return invertir_aux(lista,0,len(lista),0)
    else: return "Error"

def invertir_aux(lista,indice,indice2,auxiliar):
    if auxliar == len(lista)+1:
        return lista
    lista[indice+auxiliar] = lista[indice2-auxiliar]
    else: return invertir_aux(lista,indice,indice2,auxiliar)
    
    
