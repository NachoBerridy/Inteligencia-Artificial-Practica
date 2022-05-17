from layout_ga import Layout
from genetic_algorithm import Genetic_Algorithm
from interfaz_2 import*
from path import Path
import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":

    g_a = Genetic_Algorithm(15)

    o_layout= g_a.optimal_layout()
    print("El mejor individuo es: ",o_layout)
    print("El minimo valor de fitness es: ",g_a.best_fitness)
    print("Se realizaron %s iteraciones"%g_a.iteration_list[-1])
    layout1 = Layout()
    layout1.fill_mat(o_layout)
    path1 = Path(layout1)

   
    fig1, ax1 = plt.subplots()
    fig2, ax2= plt.subplots()
    fig3, ax3 = plt.subplots()

    it = [] 
    dis = []

    for i in (g_a.iteration_list):
        for j in range(len(g_a.iteration_list)):
            it.append(i)

    for i in g_a.dispersion:
        for j in range(len(i)):
            dis.append(i[j])

    ax1.plot(g_a.iteration_list, g_a.total_fitness_list, marker = 'o')

    ax1.set_ylabel("Fitness de cada poblacion")
    ax1.set_xlabel("Iteraciones")

    ax2.boxplot(g_a.dispersion)
    ax2.set_ylabel("Dispersion de cada individuo")
    ax2.set_xlabel("Iteraciones")
    ax2.set_xticklabels(g_a.iteration_list)
    fitness_a=[]
    for i in g_a.total_fitness_list:
        fitness_a.append(i/g_a.numero_poblacion)
    
    ax3.plot(g_a.iteration_list, fitness_a)
    ax3.set_ylabel("Fitness promedio de cada poblacion")
    ax3.set_xlabel("Iteraciones")
    
    plt.show()
    main_loop(path1)
 