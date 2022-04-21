from path import*
from interfaz_2 import*



if __name__ == "__main__":

    layout_1 = Layout(8,7,0,4,4)
    layout_1.fill_mat()
    path_1=Path(layout_1)
    main_loop(path_1)