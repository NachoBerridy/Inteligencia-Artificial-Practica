import random
import math


class Simulated_Annealing:

    def __init__(self,nodes):
        self.t=True
        self.new=nodes
        self.best__state_=nodes
        self.dict_cost={}
        self.dict_path = {}
        self.racks = {}
        self.nodes = nodes

    def cost(self,state):
        cost = 0
        for i in range(len(state)-1):
            cost = cost + self.dict_cost["%s->%s"%(state[i],state[i+1])]
        return cost

    def fill_dicts(self,path_1):
        """
        Crea dos diccionarios, uno con los costos de ir de un nodo a otro y otro con el camino entre nodos
        """

        for j in path_1.storage.mat:
            for i in j:
                if i.is_rack == False:
                    self.racks["%s" %(i.product)] = (i.a_y,i.a_x)
        
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if self.nodes[i] != self.nodes[j]:
                    path_1.starting_point = self.racks[str(self.nodes[i])]
                    path_1.target = self.racks[str(self.nodes[j])]
                    self.dict_path["%s->%s"%(self.nodes[i],self.nodes[j])] = path_1.a_star()
                    self.dict_cost["%s->%s"%(self.nodes[i],self.nodes[j])] = len(self.dict_path["%s->%s"%(self.nodes[i],self.nodes[j])])


    def sequence(self,current_state,T):
        
        """
        Ejecuta el algoritmo de recocido simulado y devuelve una lista con el mejor orden que encontro, 
        el costo de dicho orden y ademas una lista de las T y una de los costos de cada orden que ha ido
        encontrando para graficarlos 
        """   

        new = current_state[:] #Nuevo estado depues de permutar sus nodos
        b_state = current_state[:] #Mejor estado econtrado
        c_state = current_state[:] #Estado actual con el que trabaja el algoritmo

        temperature_list = [T]
        state_list = [self.cost(c_state)]

        while self.t==True:

            T=T-1
            temperature_list.append(T)
            state_list.append(self.cost(c_state))
            
            if T==0:

                print ("Estado final %s"%c_state)
                print(self.cost(c_state))

                return (b_state, self.cost(b_state), list(reversed(temperature_list)), state_list)

            pos1=random.randrange(1,(len(c_state)-1),1) 
            pos2=pos1
            while pos1==pos2:
                pos2=random.randrange(1,(len(c_state)-1),1) 

            new[pos1],new[pos2]=new[pos2],new[pos1]

            cost1=self.cost(c_state)
            cost2=self.cost(new)
            deltaE=cost2-cost1

            if deltaE<0 or (random.random()<(math.exp(-deltaE/T)) and deltaE>0):
                c_state=new[:]
                
            if self.cost(c_state)<self.cost(b_state):
                b_state=c_state[:]

            new = c_state[:]

                



    