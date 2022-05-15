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

    fig, ax = plt.subplots(1,2)

    it = [] 
    dis = []

    for i in (g_a.iteration_list):
        for j in range(len(g_a.iteration_list)):
            it.append(i)

    for i in g_a.dispersion:
        for j in range(len(i)):
            dis.append(i[j])

    ax[0].plot(g_a.iteration_list, g_a.total_fitness_list)
    ax[0].set_ylabel("Fitness de cada poblacion")
    ax[0].set_xlabel("Iteraciones")
    ax[1].scatter(it, dis)
    ax[1].set_ylabel("Dispersion de cada individuo")
    ax[1].set_xlabel("Iteraciones")
    plt.show()
    main_loop(path1)
 