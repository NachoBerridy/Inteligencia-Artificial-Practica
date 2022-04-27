import re
import random
class Genetic_Algorithm:

    def __init__(self):
        pass

    def read_txt(self):
        orders=open("orders.txt","r")
        a=1
        list_1=[]
        list_2=[]
        list_3=[]
        counter=0
        for i in orders:
            list_1.append(i) #txt en una lista
            if i==("Order %s\n"%(a)):
                a=a+1
                list_2.append(counter) #puntos donde cortar las lista del txt
            counter=counter+1

        for i in range(len(list_2)-1):
            list_3.append(list_1[list_2[i]+1:list_2[i+1]-1])
        list_3.append(list_1[list_2[len(list_2)-1]+1:-1])
        
        list_1=[]
        list_2=[]

        for i in range(len(list_3)):
            for j in range(len(list_3[i])):
                for s in re.findall(r'-?\d+\.?\d*', list_3[i][j]):
                    list_2.append(int(s))
            list_1.append(list_2)
            list_2=[]
        
        return list_1

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


    def crossover(self,father_1,father_2):
        child_1=[]
        child_2=[]
        for i in range(len(father_1)):
            child_1.append(0)
            child_2.append(0)
        pos1=random.randrange(0,(len(father_1)),1)
        pos2=pos1
        while pos1==pos2:
            pos2=random.randrange(1,(len(father_1)),1) 

        if pos1<pos2:
            for i in range(pos1,pos2):
                child_1[i]=father_2[i]
                child_2[i]=father_1[i]
            child_1=self.child_complete(father_1,child_1,pos2)
            child_2=self.child_complete(father_2,child_2,pos2)
        else:
            for i in range(pos2,pos1):
                child_1[i]=father_2[i]
                child_2[i]=father_1[i]
            child_1=self.child_complete(father_1,child_1,pos1)
            child_2=self.child_complete(father_2,child_2,pos1)

    def mutation(self,child):
        if random.random()<0.05:
            pos1=random.randrange(0,(len(child)),1)
            pos2=pos1
            while pos1==pos2:
                pos2=random.randrange(1,(len(child)),1) 
            child[pos1],child[pos2]=child[pos2],child[pos1]
        return child

    def fitness(self):
        pass

    def optimal_layout():
        pass

    pass