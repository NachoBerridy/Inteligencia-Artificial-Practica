from math import sqrt
from layout import Layout

class Path:

    def __init__(self,layout:Layout):

        self.total_cost:int
        self.storage=layout
        self.target=(0,0)
        self.starting_point=(0,0)

    def a_star(self): 

        open_nodes =[]
        closed_nodes=[]
        neighbours=[]
        sequence=[]
        closed_nodes.append(self.starting_point)
        x=self.starting_point[1]
        y=self.starting_point[0]

        while (y,x)!=self.target: ##nodo objetivo
            
            root1 = (y,x) #nodo raiz
            neighbours=[]
            if   y==0: 
                if 0<x<self.storage.columns-1: #self.storage.columns: cantidad de columnas
                    neighbours = [(y+1, x), (y, x+1),(y, x-1)]
                elif x==0:
                    neighbours = [(y, x+1),(y+1, x)]
                elif x==self.storage.columns-1:
                    neighbours = [(y+1, x),(y, x-1)]            

            elif x==0:  
                if  0<y<self.storage.rows-1:
                    neighbours = [(y, x+1),(y-1, x),(y+1, x)]
                elif y==self.storage.rows-1:
                    neighbours = [(y-1, x),(y, x+1)]

            elif x ==self.storage.columns-1:
                if 0<y<self.storage.rows-1:
                    neighbours = [(y, x-1),(y+1, x),(y-1, x)]
                elif y==self.storage.rows-1:
                    neighbours = [(y, x-1),(y-1, x)]

            elif y==self.storage.rows-1:  
                if 0<x<self.storage.columns-1:
                    neighbours = [(y, x+1),(y, x-1),(y-1, x)]
            else: 
                neighbours = [(y, x+1),(y, x-1),(y+1, x),(y-1, x)]
            
            for n in neighbours[::1]: 
                if (self.storage.mat[n].is_rack == False):
                    neighbours.remove(n)
                elif n in closed_nodes:
                    neighbours.remove(n)
            
            for i in neighbours[::1]:
                    
                if i in open_nodes:
                    if self.storage.mat[i].g>(self.storage.mat[y,x].g+1): 
                        self.storage.mat[i].root=root1
                        self.storage.mat[i].g=self.storage.mat[y,x].g+1
                        self.storage.mat[i].f=self.storage.mat[i].h+self.storage.mat[i].g
                else:
                    open_nodes.append(i)
                    self.storage.mat[i].root=root1
                    self.storage.mat[i].h=round(sqrt(((self.target[0]-i[0])**2)+((self.target[1]-i[1])**2)))
                    self.storage.mat[i].g=self.storage.mat[y,x].g+1
                    self.storage.mat[i].f=self.storage.mat[i].h+self.storage.mat[i].g

            (y,x)=open_nodes[0]

            for i in open_nodes:
                if (self.storage.mat[y,x].f > self.storage.mat[i].f):
                    (y,x) = i

            open_nodes.remove((y,x))
            closed_nodes.append((y,x))
            
        self.total_cost = self.storage.mat[self.target].f 

        while self.target != self.starting_point:
            sequence.append(self.target)
            self.target=self.storage.mat[self.target].root
        sequence.append(self.target)

        for i in sequence:
             self.storage.mat[i[0],i[1]].set_color((244, 216, 16))
        ordered_sequence=list(reversed(sequence))

        for  i in range(self.storage.rows):
            for  j in range(self.storage.columns):
                if self.storage.mat[i,j].is_target == True:
                    ordered_sequence.append((i, j))
                if self.storage.mat[i,j].is_starting_point == True:
                    ordered_sequence.insert(0,(i, j))

        return ordered_sequence
