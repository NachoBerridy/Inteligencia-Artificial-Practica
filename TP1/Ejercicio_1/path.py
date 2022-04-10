from cmath import sqrt
from msilib import sequence
from layout import Layout
class Path:

    def __init__(self):
        self.box_list
        self.total_cost:int
        self.storage:Layout

    def a_star(self,starting_point,c_row,c_col,target):
        open_nodes =[]
        closed_nodes=[]
        neighbours=[]
        sequence=[]
        closed_nodes.append(starting_point)
        (x,y)=starting_point
        while (x,y)!=target: ##nodo objetivo

            root = (x,y) #nodo raiz
            neighbours.clear()

            if   y==0: 
                if 0<x<c_col: #c_col: cantidad de columnas
                    neighbours = [(x,y + 1),(x+1,y),(x-1,y)]
                elif x==0:
                    neighbours = [(x+1,y),(x,y+1)]
                elif x==c_col:
                    neighbours = [(x,y+1),(x-1,y)]            

            elif x==0:  
                if  0<y<c_row:
                    neighbours = [(x+1,y),(x,y-1),(x,y+1)]
                elif y==c_row:
                    neighbours = [(x,y-1),(x+1,y)]

            elif x ==c_col:
                if 0<y<c_row:
                    neighbours = [(x-1,y),(x,y+1),(x,y-1)]
                elif y==c_row:
                    neighbours = [(x-1,y),(x,y-1)]

            elif y==c_row:  
                if 0<x<c_col:
                    neighbours = [(x+1,y),(x-1,y),(x,y-1)]
            else: 
                neighbours = [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]

            for i in neighbours: 
                if self.storage.mat[i]==False or i in closed_nodes:
                    neighbours.remove(i)
            for i in neighbours:
                if i in open_nodes:
                    if self.storage.mat[i].g>self.storage.mat[x,y].g+1: 
                        self.storage.mat[i].root=root
                        self.storage.mat[i].g=self.storage.mat[x,y].g+1
                        self.storage.mat[i].f=self.storage.mat[i].h+self.storage.mat[i].g
                else:
                    open_nodes.append(i)
                    self.storage.mat[i].root=root
                    self.storage.mat[i].h=round(sqrt(((target[0]-i[0])**2)+((target[1]-i[1])**2)))
                    self.storage.mat[i].g=self.storage.mat[x,y].g+1
                    self.storage.mat[i].f=self.storage.mat[i].h+self.storage.mat[i].g
            (x,y)=open_nodes[0]
            for i in open_nodes:
                if (self.storage.mat[x,y].f>self.storage.mat[i].f):
                    (x,y) = i
            closed_nodes.append((x,y))
            open_nodes.remove((x,y))
        while target != starting_point:
            sequence.append(target)
            target=self.storage.mat[target].root
            ordered_sequence=reversed(sequence)

        return ordered_sequence