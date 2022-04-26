from path import*
from interfaz_2 import*
from interfaz_1 import*



if __name__ == "__main__":

    #gui1=Gui()
    #gui1.root.mainloop()
    layout1 = Layout()
    layout1.fill_mat()
    path1 = Path(layout1)
    main_loop(path1)
