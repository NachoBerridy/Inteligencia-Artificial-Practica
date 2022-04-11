from math import sqrt
from msilib import sequence
from layout import Layout
class Path:

    def __init__(self,layout:Layout):
        #self.box_list
        #self.total_cost:int
        self.storage=layout
        self.target=(0,0)
        self.starting_point=(0,0)

    def a_star(self): 
        open_nodes =[]
        closed_nodes=[]
        neighbours=[]
        sequence=[]
        closed_nodes.append(self.starting_point)
        x=self.starting_point[0]
        y=self.starting_point[1]
        while (x,y)!=self.target: ##nodo objetivo
            
            root1 = (x,y) #nodo raiz
            neighbours=[]
            if   y==0: 
                if 0<x<self.storage.columns-1: #self.storage.columns: cantidad de columnas
                    neighbours = [(x,y + 1),(x+1,y),(x-1,y)]
                elif x==0:
                    neighbours = [(x+1,y),(x,y+1)]
                elif x==self.storage.columns-1:
                    neighbours = [(x,y+1),(x-1,y)]            

            elif x==0:  
                if  0<y<self.storage.rows-1:
                    neighbours = [(x+1,y),(x,y-1),(x,y+1)]
                elif y==self.storage.rows-1:
                    neighbours = [(x,y-1),(x+1,y)]

            elif x ==self.storage.columns-1:
                if 0<y<self.storage.rows-1:
                    neighbours = [(x-1,y),(x,y+1),(x,y-1)]
                elif y==self.storage.rows-1:
                    neighbours = [(x-1,y),(x,y-1)]

            elif y==self.storage.rows-1:  
                if 0<x<self.storage.columns-1:
                    neighbours = [(x+1,y),(x-1,y),(x,y-1)]
            else: 
                neighbours = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]
           
            for i in neighbours: 
                if (self.storage.mat[i].is_rack == False):
                    neighbours.remove(i)
                elif i in closed_nodes:
                    neighbours.remove(i)

            
            for i in neighbours:
                if i in open_nodes:
                    if self.storage.mat[i].g>(self.storage.mat[x,y].g+1): 
                        self.storage.mat[i].root=root1
                        self.storage.mat[i].g=self.storage.mat[x,y].g+1
                        self.storage.mat[i].f=self.storage.mat[i].h+self.storage.mat[i].g
                    else:
                        pass
                else:
                    open_nodes.append(i)
                    self.storage.mat[i].root=root1
                    self.storage.mat[i].h=round(sqrt(((self.target[0]-i[0])**2)+((self.target[1]-i[1])**2)))
                    self.storage.mat[i].g=self.storage.mat[x,y].g+1
                    self.storage.mat[i].f=self.storage.mat[i].h+self.storage.mat[i].g
            (x,y)=open_nodes[0]
            for i in open_nodes:
                if (self.storage.mat[x,y].f > self.storage.mat[i].f):
                    (x,y) = i

            open_nodes.remove((x,y))
            closed_nodes.append((x,y))
            print(x,y)
            
            
        while self.target != self.starting_point:
            sequence.append(self.target)
            
            self.target=self.storage.mat[self.target].root
            #print(sequence)
            #ordered_sequence=reversed(sequence)
        return sequence