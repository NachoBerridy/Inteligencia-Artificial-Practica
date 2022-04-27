from unicodedata import name
from layout_ga import Layout
from genetic_algorithm import Genetic_Algorithm
from interfaz_2 import*
from path import Path


if __name__ == "__main__":

    g_a = Genetic_Algorithm()

    o_layout = g_a.optimal_layout()
    
    layout1 = Layout()
    layout1.fill_mat(o_layout)
    path1 = Path(layout1)
    
    main_loop(path1)
