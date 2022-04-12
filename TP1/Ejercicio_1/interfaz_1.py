from logging import root
from tkinter import *
from tkinter import ttk as t

class Gui:
    def __init__(self):
        self.root = Tk()
        self.frm = t.Frame(self.root)
        self.frm.grid()
        self.lista=["horizontal","vertical"]
        t.Label(self.frm, text="Cantidad de filas de estanterias").grid(column=0, row=0)
        self.c_rows=Entry(self.frm)
        self.c_rows.grid(column=1, row=0)
        c=self.c_rows.get()
        self.op=StringVar(self.root)
        self.opcion=OptionMenu(self.frm,self.op,*self.lista)
        self.opcion.grid(column=1, row=2,ipady=5, ipadx=46)
        t.Button(self.frm, text="Start", command=self.do_funcion(self.op)).grid(column=0, row=2,ipady=5, ipadx=45)
        t.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=2, row=2,ipady=5, ipadx=46)
    
    def do_funcion(self,c):
        o=self.op.get()
        print("hola")

""" def _init_(self):
        super(cliente,self)._init_()
        self.i = 0
        self.robot3D = grafico(19999)
        self.root = Tk()
        self.frm = ttk.Frame(self.root, padding=10)
        self.frm.grid()
        ttk.Button(self.frm, text="1: Conectar", command=lambda:self.do_c(1)).grid(column=0, row=1,ipady=5, ipadx=45)
        ttk.Button(self.frm, text="2: Encender", command=lambda:self.do_c(2)).grid(column=0, row=2,ipady=5, ipadx=45)
        ttk.Label(self.frm, text="").grid(column=0, row=3)
        ttk.Button(self.frm, text="3: Girar articulacion 1", command=lambda:self.do_c(3)).grid(column=0, row=4,ipady=5, ipadx=23)
        self.angulo1=Entry(self.frm)
        ttk.Label(self.frm, text="Angulo").grid(column=1, row=4)
        self.angulo1.grid(column=1,row=5)
        self.velocidad1=Entry(self.frm)
        ttk.Label(self.frm, text="Velocidad").grid(column=2, row=4)
        self.velocidad1.grid(column=2, row=5)
        ttk.Button(self.frm, text="4: Girar articulacion 2", command=lambda:self.do_c(4)).grid(column=0, row=5,ipady=5, ipadx=23)
        ttk.Button(self.frm, text="5: Girar articulacion 3", command=lambda:self.do_c(5)).grid(column=0, row=6,ipady=5, ipadx=23)
        ttk.Label(self.frm, text="").grid(column=0, row=7)
        ttk.Button(self.frm, text="6: Accionar Efector", command=lambda:self.do_c(6)).grid(column=0, row=8,ipady=5, ipadx=29)
        ttk.Label(self.frm, text="").grid(column=0, row=9)
        ttk.Button(self.frm, text="7: Mover Robot", command=lambda:self.do_c(7)).grid(column=0, row=10,ipady=5, ipadx=38)
        self.x1=Entry(self.frm)
        ttk.Label(self.frm, text="X").grid(column=1, row=9)
        self.x1.grid(column=1,row=10)
        self.y1=Entry(self.frm)
        ttk.Label(self.frm, text="Y").grid(column=2, row=9)
        self.y1.grid(column=2,row=10)
        self.velocidad2=Entry(self.frm)
        ttk.Label(self.frm, text="Velocidad").grid(column=3, row=9)
        self.velocidad2.grid(column=3, row=10)
        ttk.Label(self.frm, text="").grid(column=0, row=11)
        ttk.Button(self.frm, text="8: Retorno al Origen", command=lambda:self.do_c(8)).grid(column=0, row=12,ipady=5, ipadx=26)
        ttk.Label(self.frm, text="").grid(column=0, row=13)
        ttk.Button(self.frm, text="9: Modo automatico", command=lambda:self.do_c(9)).grid(column=0, row=14,ipady=5, ipadx=25)
        self.p1=Entry(self.frm)
        ttk.Label(self.frm, text="Cantidad de movimientos").grid(column=1, row=13)
        self.p1.grid(column=1,row=14)
        ttk.Label(self.frm, text="").grid(column=0, row=15)

        ttk.Button(self.frm, text="Reporte", command=lambda:self.do_reporte()).grid(column=0, row=16,ipady=5, ipadx=46)
        ttk.Button(self.frm, text="Gcode", command=lambda:self.do_gcode()).grid(column=0, row=17,ipady=5, ipadx=46)
        ttk.Button(self.frm, text="Quit", command=self.root.destroy).grid(column=0, row=18,ipady=5, ipadx=46)
"""
if __name__=="__main__":
    gui1=Gui()
    gui1.root.mainloop() 