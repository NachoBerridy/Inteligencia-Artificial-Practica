from Simulated_Annealing_df import Simulated_Annealing
from path import Path
from layout import Layout
import matplotlib.pyplot as plt
import pandas as pd
import re

if __name__ == "__main__":

    layout1 = Layout()
    layout1.fill_mat()
    path1 = Path(layout1)
    nodes = [1, 100, 5, 27, 98, 19, 21, 35, 28, 17, 15, 55, 34, 72, 26, 91]
    list = []
    for i in range(100):
        list.append(i+1)
        pass
    

    def read_txt():

        orders=open(".\orders.txt","r")
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
        
        orders = list_1[:]
        return orders

    def crate_df():
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
                        id = '%s->%s'%(i,j)
                        path_1.starting_point = (racks[i][0],racks[i][1])
                        path_1.target = (racks[j][0],racks[j][1])
                        id_list.append(id)
                        costos.append(len(path_1.a_star()))

        df.index = id_list[:]
        df['costo'] = costos[:]
        return (df)
    
    orders = read_txt()
    df = crate_df()

    S_Ann = Simulated_Annealing(orders[5], list, df)
    S_Ann.fill_dicts()
    costs = []
    states = []
    T= []
    #state, cost = S_Ann.sequence()
    for i in range(100):
        cost, state = S_Ann.sequence()
        states.append(state)
        costs.append(cost)
        T.append(i)
    #print("Mejor estado corto] %s"%state)
    #print("Costo: %s"%costs)

    
    fig, ax= plt.subplots()
    ax.plot(T, costs)
    ax.set_xlabel("Iteracion")
    ax.set_ylabel("Costo de la orden")
    ax.set_title('Simulated annealing con log base 1000000 Desde Y = 5000')
    plt.show()
