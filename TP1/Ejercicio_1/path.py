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
            """
            for n in neighbours: 
                if (self.storage.mat[n].is_rack == False):
                    neighbours.remove(n)
                elif n in closed_nodes:
                    neighbours.remove(n)
            """
            #print(neighbours)
            for i in neighbours[::1]:
                
                if self.storage.mat[i].is_rack == False:
                    neighbours.remove(i)
                    #print("Era barrera")
                    
                elif i in closed_nodes:
                    neighbours.remove(i)
                    #print("Estaba en nodos cerrados")
                elif i in open_nodes:
                    #print("Ya estaba guardado")
                    if self.storage.mat[i].g>(self.storage.mat[y,x].g+1): 
                        self.storage.mat[i].root=root1
                        self.storage.mat[i].g=self.storage.mat[y,x].g+1
                        self.storage.mat[i].f=self.storage.mat[i].h+self.storage.mat[i].g
                else:
                    #print("Nuevo!")
                    open_nodes.append(i)
                    self.storage.mat[i].root=root1
                    self.storage.mat[i].h=round(sqrt(((self.target[0]-i[0])**2)+((self.target[1]-i[1])**2)))
                    self.storage.mat[i].g=self.storage.mat[y,x].g+1
                    self.storage.mat[i].f=self.storage.mat[i].h+self.storage.mat[i].g

            print (open_nodes)
            (y,x)=open_nodes[0]

            for i in open_nodes:
                if (self.storage.mat[y,x].f > self.storage.mat[i].f):
                    (y,x) = i

            open_nodes.remove((y,x))
            closed_nodes.append((y,x))
            #print(y,x)
            
            
        while self.target != self.starting_point:
            sequence.append(self.target)
            self.target=self.storage.mat[self.target].root
            #print(sequence)
            #ordered_sequence=reversed(sequence)
        
        return sequence


layout_1 = Layout (6,5,1,6,6)
layout_1.fill_mat()
path1=Path(layout_1)
#print (path1.storage.columns)
#print (path1.storage.rows)
##path1.storage.mat[rows][columns]) asi lo lee
path1.starting_point = (10, 13)
path1.target = (15, 5) 

print(path1.a_star())
