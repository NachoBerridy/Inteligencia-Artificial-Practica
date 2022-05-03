import re
import random
import numpy as np
import pandas as pd
from path import *
from Simulated_Annealing_df import Simulated_Annealing
import time

class Genetic_Algorithm:

    def __init__(self, n_population):
        self.numero_poblacion = n_population
        self.population = []
        self.fitness_list = []
        self.real_fitness_list = []
        self.probability = []
        self.total_fitness = 0
        self.total_fitness_list = []
        self.orders = []
        self.best = []
        self.best_fitness=0
        self.st_dev_list = []
        self.iteration_list = []
        self.father1 = []
        self.father2 = []

    def read_txt(self):

        orders=open("C:\\DiscoD\\Nacho\\Facultad\\Materias_en_curso\\9-IA2\\Grupo6-IA-II\\TP1\\Ejercicio_3\\orders.txt","r")
        a = 1
        list_1 = []
        list_2 = []
        list_3 = []
        counter = 0
        for i in orders:
            list_1.append(i) #txt en una lista
            if i==("Order %s\n"%(a)):
                a = a + 1
                list_2.append(counter) #puntos donde cortar las lista del txt
            counter = counter + 1

        for i in range(len(list_2)-1):
            list_3.append(list_1[list_2[i]+1:list_2[i+1]-1])
        list_3.append(list_1[list_2[len(list_2)-1]+1:-1])
        
        list_1 = []
        list_2 = []

        for i in range(len(list_3)):
            for j in range(len(list_3[i])):
                for s in re.findall(r'-?\d+\.?\d*', list_3[i][j]):
                    list_2.append(int(s)+1)
            list_1.append(list_2)
            list_2 = []
        
        self.orders = list_1[:]
        #print(self.orders)

    def crate_df(self):
        layout1 = Layout()
        layout1.fill_mat()
        path_1 = Path(layout1)
        df = pd.DataFrame()
        
        racks = []
        costos = []
        id_list = [] 

        for j in path_1.storage.mat:
            for i in j:
                if i.is_rack == False:
                    racks.append((i.a_y,i.a_x))
        for j in path_1.storage.mat:
            for i in j:
                if i.is_cargo_bay == True:
                    racks.append((i.y,i.x))

        for i in range(len(racks)):
                for j in range(len(racks)):
                    if racks[i] != racks[j]:
                        #id  = '%s,%s->%s,%s'%(racks[i][0],racks[i][1],racks[j][0],racks[j][1])
                        id = '%s->%s'%(i,j)
                        path_1.starting_point = (racks[i][0],racks[i][1])
                        path_1.target = (racks[j][0],racks[j][1])
                        id_list.append(id)
                        costos.append(len(path_1.a_star()))

        df.index = id_list[:]
        df['costo'] = costos[:]
        #print(df.loc['23->25',"costo"])
        return (df)

    def child_complete(self,father,child,pos): 
        aux=[]
        c_2=0
        c=0 
        for j in range(pos,len(father)):
            if father[j] not in child: 
                aux.append(father[j])
        for i in range(len(aux)):
            child[pos+i]=aux[i]
        aux=[]
        c_2=0
        c=0  
        for j in range(len(father)):
            if father[j] not in child: 
                aux.append(father[j])
    
        while c<len(aux):
            for j in range(pos,len(father)):
                if child[j]==0:
                    child[j]=aux[c]
                    c=c+1
            child[c_2]=aux[c]
            c=c+1
            c_2=c_2+1
        return child


    def crossover(self):
        #inicio = time.time()
        child_1=[]
        child_2=[]
        for i in range(len(self.father1)):
            child_1.append(0)
            child_2.append(0)
        pos1=random.randrange(0,len(self.father1),1)
        pos2=pos1
        while pos1==pos2:
            pos2=random.randrange(1,len(self.father1),1) 

        if pos1<pos2:
            for i in range(pos1,pos2):
                child_1[i]=self.father2[i]
                child_2[i]=self.father1[i]
            child_1=self.child_complete(self.father1,child_1,pos2)
            child_2=self.child_complete(self.father2,child_2,pos2)
        else:
            for i in range(pos2,pos1):
                child_1[i]=self.father2[i]
                child_2[i]=self.father1[i]
            child_1=self.child_complete(self.father1,child_1,pos1)
            child_2=self.child_complete(self.father2,child_2,pos1)
        
        child_1=self.mutation(child_1)[:]
        child_2=self.mutation(child_2)[:]
        #fin = time.time()
        #print("Tiempo de ejecucion de crossover:" ,(fin-inicio))
        return (child_1,child_2)

    def mutation(self,child):
        #inicio = time.time()
        if random.random()<0.05:
            pos1=random.randrange(0,len(child),1)
            pos2=pos1
            while pos1==pos2:
                pos2=random.randrange(1,len(child),1) 
            child[pos1],child[pos2]=child[pos2],child[pos1]
        #fin = time.time()
        #print("Tiempo de ejecucion de mutation:" ,(fin-inicio))
        return child

    def fitness(self, list_layout, df): #lista layout es uno de los individuos de la poblacion, osea una configuracion del layout
        #inicio = time.time()
        fitness = 0
        #print(self.orders)
        for i in self.orders:
            #print(self.orders.index(i))
            s = Simulated_Annealing(i,list_layout, df)
            s.fill_dicts()
            fitness = fitness + s.sequence()[0]
            del s 
        #fin = time.time()
        #print("Tiempo de ejecucion de fitness:" ,(fin-inicio))
        return 100/fitness


    def selec_parents(self, p):
        #inicio = time.time()
        i = random.random()
        j = 0
        l = 0
        for k in self.probability:
            if j <= i <= j+k:
                if p==1:
                    self.father1 = self.population[l][:]
                elif p==2:
                    self.father2 = self.population[l][:]
                #fin = time.time()
                #print("Tiempo de ejecucion de select parents%s: %s"%(p,fin-inicio))
                return (l)
            j = j+k
            l = l + 1  
                 


    def first_population(self):
        individuo = []
        for i in range(100):
            individuo.append(i+1)

        while len(self.population)<self.numero_poblacion:
            a = random.sample(individuo, 100)
            if a not in self.population:
                self.population.append(a)
                
    def optimal_layout(self):
        self.read_txt()
        df = self.crate_df()
        self.first_population()
        self.best = self.population[0][:]
        iteration=0
        
        while iteration<15:
            tiempo_inicial=time.time()
            print(iteration)
            self.iteration_list.append(iteration)
            index_list = []
            children_list = []
            self.fitness_list = []
            self.total_fitness = 0
            self.probability = []
            self.real_fitness_list = []
            real_fitness=0
            #best_fitness = self.fitness(self.best, df)
            #lista del fitness
            for i in range(len(self.population)):
                self.fitness_list.append(self.fitness(self.population[i], df))

                self.real_fitness_list.append(100/self.fitness_list[i]) 

                self.total_fitness = self.total_fitness + self.fitness_list[i]
                real_fitness = real_fitness + 100/self.fitness_list[i]
                if i==0 and iteration==0:
                    self.best_fitness=self.real_fitness_list[0]
                try:
                    if self.real_fitness_list[i]<self.best_fitness:
                        self.best = self.population[i][:]
                        self.best_fitness = self.real_fitness_list[i]
                except:
                    pass


            #lista de fitness total 
            self.total_fitness_list.append(real_fitness)

            #lista de probabilidades de cada individuo
            for i in range(len(self.fitness_list)):
                self.probability.append(self.fitness_list[i]/ self.total_fitness)

            #seleccion 
            for i in range(int(len(self.population)/2)):
                index_1 = self.selec_parents(1)
                self.father2 = self.father1[:]
                index_2 = index_1
                while self.father2==self.father1 and (index_1, index_2) in index_list:
                    index_2 = self.selec_parents(2)
                index_list.append((index_1, index_2))
                children_list.extend(self.crossover())
            
            #Desviación estandar relativa a la media 
            #if iteration>9:
                #st_dev=np.std(self.total_fitness_list[-10:])/np.average(self.total_fitness_list[-10:])
            if iteration>5:
                st_dev=np.std(self.real_fitness_list[:])/np.average(self.real_fitness_list[:])
                self.st_dev_list.append(st_dev)
                if st_dev<0.005:
                    print("converge")
                    return self.best
        
            #nueva poblacion
            self.population=children_list[:]
            iteration = iteration  + 1

        #print(self.total_fitness)
            tiempo_final=time.time()
            print("el tiempo de iteracion es:",(tiempo_final-tiempo_inicial))
        return (self.best)