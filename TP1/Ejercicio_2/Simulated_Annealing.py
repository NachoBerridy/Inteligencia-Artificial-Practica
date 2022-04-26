import random
import math
class Simulated_Annealing:

    def __init__(self,nodes):
        self.t=True
        self.new_state=[]
        self.best_state=[]
        self.dict_cost={}
        self.dict_path = {}
        self.nodes = nodes

    def cost(self,state):
        cost = 0
        for i in range(len(state)-1):
            cost = cost + self.dict_cost["%s,%s"%(state[i],state[i+1])]
        return cost

    def fill_dicts(self,path_1):
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if self.nodes[i] != self.nodes[j]:
                    path_1.starting_point = self.nodes[i]
                    path_1.target =self.nodes[j]
                    #print("%s,%s" % (path_1.starting_point,path_1.target))
                    self.dict_path["%s,%s"%(self.nodes[i],self.nodes[j])] = path_1.a_star()
                    #self.dict_path["%s,%s"%(self.nodes[j],self.nodes[i])] = list(reversed(self.dict_path["%s,%s"%(self.nodes[i],self.nodes[j])]))
                    self.dict_cost["%s,%s"%(self.nodes[i],self.nodes[j])] = len(self.dict_path["%s,%s"%(self.nodes[i],self.nodes[j])])
                    #self.dict_cost["%s,%s"%(self.nodes[j],self.nodes[i])] = len(self.dict_path["%s,%s"%(self.nodes[i],self.nodes[j])])
        print(self.dict_cost)
        print(self.dict_path)

    def sequence(self,current_state,T):
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
            cost1=self.cost(current_state)
            cost2=self.cost(self.new_state)
            deltaE=cost2-cost1
            if deltaE<0:
                current_state=self.new_state
            elif random.random()<math.exp(-deltaE/T):
                current_state=self.new_state
             
            if self.cost(current_state)<self.cost(self.best_state):
                self.best_state=current_state




    