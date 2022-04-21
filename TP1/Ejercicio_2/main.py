from Simulated_Annealing import Simulated_Annealing
from interfaz_1 import Gui

if __name__ == "__main__":

    gui_1 = Gui()
    gui_1.root.mainloop()
    nodes = [(5,0),(1,3),(4,8),(7,5),(5,0)]
    S_Ann = Simulated_Annealing(nodes)
    S_Ann.fill_dicts(gui_1.path1)
    print(S_Ann.sequence(nodes,50))
