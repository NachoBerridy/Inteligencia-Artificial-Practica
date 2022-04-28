from layout_ga import Layout
from genetic_algorithm import Genetic_Algorithm
from interfaz_2 import*
from path import Path
import matplotlib.pyplot as plt

if __name__ == "__main__":

    g_a = Genetic_Algorithm(15)

    o_layout= g_a.optimal_layout()
    print("El mejor individuo es: ",o_layout)
    print("El minimo valor de fitness es: ",100/g_a.total_fitness)
    print("Se realizaron %s iteraciones"%g_a.iteration_list[-1])
    layout1 = Layout()
    layout1.fill_mat(o_layout)
    path1 = Path(layout1)

    fig, ax = plt.subplots(1,2)
    ax[0].plot(g_a.iteration_list[(len(g_a.iteration_list)-len(g_a.st_dev_list)):], g_a.st_dev_list)
    ax[1].plot(g_a.iteration_list, g_a.total_fitness_list)

    main_loop(path1)
