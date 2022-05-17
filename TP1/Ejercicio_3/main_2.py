from cProfile import label
from Simulated_Annealing_df import Simulated_Annealing
from path import Path
from layout import Layout
import matplotlib.pyplot as plt
import pandas as pd
import re
import time
import math

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


    
    costs_list = []
    iterations = []
    T= []
    times = []


    def log50(t):
        return math.log(t, 50)

    def log30(t):
        return math.log(t, 30)
    
    def log20(t):
        return math.log(t, 20)
    
    def log10(t):
        return math.log(t, 10)

    def log5(t):
        return math.log(t, 5)

    def lineal(t):
        return t
    
    def quadratic(t):
        return t**2

    def cubic(t):
        return t**3
    

    functions = [log50, log30, log20] #, log10, log5, lineal, quadratic, cubic]
    functions_names = ["log50", "log30", "log20"] #, "log10", "log5"], "lineal", "quadratic", "cubic"]
    
    it, ax = plt.subplots()

    counter = 0

    #data = pd.DataFrame()

    for i in functions:
        a, b, c, d, e = S_Ann.sequence(i, 10000)
        costs_list.append(c[:])
        iterations.append(e[:])
        
        #data[functions_names[counter]] = c[:]

        ax.plot(iterations[counter], costs_list[counter], label = functions_names[counter])
        counter = counter +1


    ax.set_title("Distintas funciones de enfriamiento")
    ax.set_xlabel("Numero de iteraciones")
    ax.set_ylabel("Costos")
    ax.legend()

    """
    costs = []
    T = []
    costs_list = []
    counter = 0
    for j in functions:

        t_inicial = time.time()
        costs = []

        for i in range(100):
            costs.append(S_Ann.sequence(j, 5000)[0])
        
        
        t_final = time.time()

        times.append(t_final-t_inicial)
        costs_list.append(costs)
        T.append(functions_names[counter])  

        counter = counter +1
    print(T)
    boxes, ax = plt.subplots()
    ax.boxplot(costs_list)
    ax.set_xticklabels(T)
    ax.set_xlabel("Funcion")
    ax.set_ylabel("Costo de la orden")
    ax.set_title("Dispersion respecto del  la funcion")
    plt.show()

    tiempos, axx = plt.subplots()
    axx.plot(T, times, marker = 'o')
    axx.set_xlabel("Funcion")
    axx.set_xticklabels(T)
    axx.set_ylabel("Tiempo de ejecucion")
    axx.set_title("Tiempo respecto de la funcion")
    plt.show()
    """

    t = [100, 200, 500, 1000, 5000, 10000, 20000, 40000]
    for j in t:
        costs = []

        t_inicial = time.time()
        for i in range(100):

            costs.append(S_Ann.sequence(log20, j)[0])
        
        t_final = time.time()
        times.append(t_final-t_inicial)
        costs_list.append(costs)
        T.append(str(j))
        print("Tiempo con t = %s: %s"%(j, t_final-t_inicial))
    

    boxes, ax = plt.subplots()
    ax.boxplot(costs_list)
    ax.set_xticklabels(T)
    ax.set_xlabel("Numero de iteraciones")
    ax.set_ylabel("Costo de la orden")
    ax.set_title("Dispersion respecto del numero de iteraciones")
    plt.show()

    tiempos, axx = plt.subplots()
    axx.plot(T, times, marker = 'o')
    axx.set_xlabel("Numero de iteraciones")
    axx.set_ylabel("Tiempo de ejecucion")
    axx.set_title("Tiempo respecto del numero de iteraciones")
    plt.show()
