import numpy as np
from box import Box
from rack import Rack
class Layout: #disposicion    
    
    def __init__(self,racks_by_columns = 2,racks_by_row = 5,racks_order = 0,racks_columns = 2,racks_rows = 5):
        self.columns:int #cantidad de columnas de espacios del almacen
        self.rows:int #cantidad de filas de espacios del almacen 
        self.racks_by_columns = racks_by_columns #Es la cantidad de filas de estantes en el almacen
        self.racks_by_row = racks_by_row #Es la cantidad de columnas de estantes en el almacen
        self.racks_order = racks_order # 0:vertical, 1:horizontal
        self.racks_columns = racks_columns
        self.racks_rows = racks_rows
        self.mat:np
        if self.racks_order == 0:
            self.racks_columns = 2
        else:
            self.racks_rows = 2

    def fill_mat(self):

        product = 0 #Numero de producto

        if(self.racks_order == 0): #Vertical
            self.columns = self.racks_by_row*4 + 2
            self.rows = self.racks_by_columns*(self.racks_rows+2) + 2
            self.mat = np.zeros((self.rows,self.columns),Box)

            for j in range (self.columns):
                counter = 0 #Contador para que coloque la cantidad de estanterias correctas
                for i in range (self.rows):
                    
                    if (counter ==self.racks_rows+2):
                        counter = 0

                    if (2<=j<=self.columns-3 and 2<=i<=self.rows-3 ):
                        if (counter<self.racks_rows):
                            
                            if self.mat[i,j-2].is_rack==False:
                                self.mat[i,j] = Box(i, j, True, (255, 255, 255))

                            elif self.mat[i,j-1].is_rack == False:
                                product = product + 1
                                self.mat[i,j] = Rack(i, j, False, (0, 0, 0), product, i, j+1)

                            else:
                                product = product + 1
                                self.mat[i,j] = Rack(i, j, False, (0, 0, 0), product, i, j-1)

                            counter=counter+1

                        elif  (self.racks_rows<=counter<self.racks_rows+2):
                            self.mat[i,j] = Box(i, j, True, (255, 255, 255))
                            counter=counter+1
                        
                    else:
                        self.mat[i,j] = Box(i, j, True, (255, 255, 255))

        else: #Horizontal
            self.columns = self.racks_by_row*(self.racks_columns+2)+2
            self.rows = self.racks_by_columns*4+2
            self.mat = np.zeros((self.rows,self.columns),Box)

            for i in range (self.rows):
                counter = 0
                for j in range (self.columns):
                   
                    if (counter ==self.racks_columns+2):
                        counter = 0

                    if (2<=j<=self.columns-3 and 2<=i<=self.rows-3 ):
                       
                        if (counter<self.racks_columns):
                            counter=counter+1
                            if self.mat[i-2,j].is_rack==False:
                                self.mat[i,j] = Box(i, j, True, (255, 255, 255))

                            elif self.mat[i-1,j].is_rack == False:
                                product = product + 1
                                self.mat[i,j] = Rack(i, j, False, (0, 0, 0), product, i+1, j)
                               
                            else:
                                product = product + 1
                                self.mat[i,j] = Rack(i, j, False, (0, 0, 0), product, i-1, j)
                                
                        elif  (self.racks_columns<=counter<self.racks_columns+2):
                            self.mat[i,j] = Box(i, j, True, (255, 255, 255))
                            counter=counter+1
                        
                    else:
                        self.mat[i,j] = Box(i, j, True, (255, 255, 255))
        
        for i in range (self.rows):
            if(i%5==0 and i!=0):
                self.mat[i,0].is_cargo_bay = True
                self.mat[i,0].set_color((157, 157, 157 ))





"""
objeto = Layout (3,4,1,4,60)

objeto.fill_mat()
matriz_prueba = np.zeros((objeto.rows,objeto.columns),int)
for j in range (objeto.columns):
    for i in range (objeto.rows):
        if objeto.mat[i,j].is_rack == True:
            matriz_prueba[i,j] = 0
        else:
            matriz_prueba[i,j] = 1

for line in matriz_prueba:
    print ('  '.join(map(str, line)))
"""