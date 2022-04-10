from cmath import sqrt
from layout import Layout
class Path:

    def __init__(self):
        self.box_list
        self.total_cost:int
        self.storage:Layout

    def a_star(self,p_inicial,c_fila,c_col,target):
        nodos_abiertos =[]
        nodos_cerrados=[]
        puntos=[]
        camino=[]
        nodos_cerrados.append(p_inicial)
        (x,y)=p_inicial
        while (x,y)!=target: ##nodo objetivo

            root = (x,y) #nodo raiz
            puntos.clear()

            if   y==0: 
                if 0<x<c_col: #c_col: cantidad de columnas
                    puntos = [(x,y+1),(x+1,y),(x-1,y)]
                elif x==0:
                    puntos = [(x+1,y),(x,y+1)]
                elif x==c_col:
                    puntos = [(x,y+1),(x-1,y)]            

            elif x==0:  
                if  0<y<c_fila:
                    puntos = [(x+1,y),(x,y-1),(x,y+1)]
                elif y==c_fila:
                    puntos = [(x,y-1),(x+1,y)]

            elif x ==c_col:
                if 0<y<c_fila:
                    puntos = [(x-1,y),(x,y+1),(x,y-1)]
                elif y==c_fila:
                    puntos = [(x-1,y),(x,y-1)]

            elif y==c_fila:  
                if 0<x<c_col:
                    puntos = [(x+1,y),(x-1,y),(x,y-1)]
            else: 
                puntos = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

            for i in puntos: 
                if self.storage.mat[i]==False or i in nodos_cerrados:
                    puntos.remove(i)
            for i in puntos:
                if i in nodos_abiertos:
                    if self.storage.mat[i].g>self.storage.mat[x,y].g+1: 
                        self.storage.mat[i].root=root
                        self.storage.mat[i].g=self.storage.mat[x,y].g+1
                        self.storage.mat[i].f=self.storage.mat[i].h+self.storage.mat[i].g
                else:
                    nodos_abiertos.append(i)
                    self.storage.mat[i].root=root
                    self.storage.mat[i].h=round(sqrt(((target[0]-i[0])**2)+((target[1]-i[1])**2)))
                    self.storage.mat[i].g=self.storage.mat[x,y].g+1
                    self.storage.mat[i].f=self.storage.mat[i].h+self.storage.mat[i].g
            (x,y)=nodos_abiertos[0]
            for i in nodos_abiertos:
                if (self.storage.mat[x,y].f>self.storage.mat[i].f):
                    (x,y) = i
            nodos_cerrados.append((x,y))
            nodos_abiertos.remove((x,y))
        while target != p_inicial:
            camino.append(target)
            target=self.storage.mat[target].root
        camino_ordenado=reversed(camino)

        return camino_ordenado
