from msilib import sequence
from Simulated_Annealing import Simulated_Annealing
from path import Path
from layout import Layout
import matplotlib.pyplot as plt

if __name__ == "__main__":

    layout1 = Layout()
    layout1.fill_mat()
    path1 = Path(layout1)
    nodes = [1, 100, 5, 27, 98, 19, 21, 35, 28, 17, 15, 55, 34, 72, 26, 91]
    list = []
    for i in range(100):
        list.append(i+1)
        pass
    S_Ann = Simulated_Annealing(nodes)
    S_Ann.fill_dicts(path1)
    sequence, cost, T_list, states_list = S_Ann.sequence(nodes, 600000)

    print("Mejor estado: %s"%sequence)
    print("Costo: %s"%cost)

    
    """fig, ax= plt.subplots(1,3)
    ax.plot(T_list, states_list)
    plt.show()
    """
