class Matriz:
    def __init__(self):
        pass

    def crearMatriz(self,num):
        if isinstance(num,int):
            return self.rellenar(num,[],[],0,0)
        else:return "La matriz no es una lista"



    def rellenar(self,n,matriz,fila,indiceFila,indiceColumna):
        if indiceFila == n:
            return matriz
        
        elif indiceColumna == n:
            return (self.rellenar(n,matriz + [fila], [], indiceFila + 1, 0))
        
        elif indiceFila == 0 or indiceFila == (n - 1):
            return (self.rellenar(n,matriz, fila + ["*"],indiceFila, indiceColumna + 1))
        
        elif indiceColumna == 0 or indiceColumna == (n-1):
            return (self.rellenar(n,matriz,fila+["*"], indiceFila,indiceColumna + 1))
        else:
            return (self.rellenar(n, matriz, fila + [0], indiceFila, indiceColumna + 1))

