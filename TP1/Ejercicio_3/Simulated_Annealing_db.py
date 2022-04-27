import random
import math
import sqlite3 as sql

class Simulated_Annealing:

    def __init__(self, nodes, path, order):
        self.path1 = path
        self.t=True
        self.new=nodes
        self.best__state_=nodes
        self.dict_cost={}
        self.racks = {}
        self.nodes = nodes
        self.nodes.append(0)
        self.nodes.insert(0, 0)

    def cost(self,state):
        cost = 0
        for i in range(len(state)-1):
            cost = cost + self.dict_cost["%s->%s"%(state[i],state[i+1])]
        return cost

    def fill_dicts(self):

        conexion  = sql.connect("a_star.db")
        cursor = conexion.cursor()
        """
        Crea dos diccionarios, uno con los costos de ir de un nodo a otro y otro con el camino entre nodos
        """

        for j in self.path_1.storage.mat:
            for i in j:
                if i.is_rack == False:
                    self.racks["%s" %(i.product)] = (i.a_y,i.a_x)
                elif i.is_cargo_bay == True:
                    self.racks["0"] = (i.y,i.x)
        
        for i in range(len(self.nodes)):
            for j in range(len(self.nodes)):
                if self.nodes[i] != self.nodes[j]:
                    id = '%s,%s->%s,%s'%(self.racks[str(self.nodes[i])][0],self.racks[str(self.nodes[i])][1],
                                         self.racks[str(self.nodes[j])][0],self.racks[str(self.nodes[j])][1])
                    #La linea siguiente guarda en el diccionario de costos el costo que esta guardado en la base de datos
                    self.dict_cost["%s->%s"%(self.nodes[i],self.nodes[j])] = cursor.execute("SELECT costo FROM astar WHERE n ='%s'"%id).fetchone()[0]
        conexion.close()


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

                return (b_state, self.cost(b_state), list(reversed(temperature_list)), list(state_list))

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

                



    