from path import*
from interfaz_2 import*



if __name__ == "__main__":

    cuadro = Layout(8,7,0,4,4)
    cuadro.fill_mat()
    path1=Path(cuadro)
    main_loop(path1)