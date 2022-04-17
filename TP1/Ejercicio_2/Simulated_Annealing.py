import random
import math
class Simulated_Annealing:

    def __init__(self):
        self.t=True
        self.new_state=[]
        self.best_state=[]
    def cost(self,list,lista_diccionario):
        pass
    def sequence(self,current_state,lista_diccionario,T):
        self.new_state=current_state
        self.best_state=current_state
        while self.t==True:
            T=T-1
            if T==0:
                return self.best_state
            pos1=random.randrange(1,(len(current_state)-1),1) 
            pos2=pos1
            while pos1==pos2:
                pos2=random.randrange(1,(len(current_state)-1),1) 
            
            self.new_state[pos1],self.new_state[pos2]=current_state[pos2],current_state[pos1]
            cost1=self.cost(current_state,lista_diccionario)
            cost2=self.cost(self.new_state,lista_diccionario)
            deltaE=cost2-cost1
            if deltaE<0:
                current_state=self.new_state
            elif random.random()<math.exp(-deltaE/T):
                current_state=self.new_state
             
            if self.cost(current_state,lista_diccionario)<self.cost(self.best_state,lista_diccionario):
                self.best_state=current_state




    