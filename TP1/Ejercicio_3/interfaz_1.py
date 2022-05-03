from faulthandler import disable
from importlib.resources import path
from tkinter import *
from tkinter import ttk 
from path import*

class Gui:
    def __init__(self):
        self.path1:Path
        self.root = Tk()
        self.frm = ttk.Frame(self.root,padding=10)
        self.frm.grid()
        self.lista=["horizontal","vertical"]

        ttk.Label(self.frm, text="Seleccione la ortientacion").grid(column=0, row=0,ipady=5, ipadx=46)
        self.op=StringVar(self.root)
        self.op.set("seleccione")
        self.opcion=OptionMenu(self.frm,self.op,*self.lista)
        self.opcion.grid(column=1, row=0,ipady=5, ipadx=46)
        ttk.Button(self.frm, text="Aceptar", command=lambda:self.do_bloquear()).grid(column=2, row=0,ipady=5, ipadx=46)

        ttk.Label(self.frm, text="Cantidad filas de estanterias").grid(column=0, row=1,ipady=5, ipadx=46)
        ttk.Label(self.frm, text="Cantidad de columnas de estanterias").grid(column=0, row=2,ipady=5, ipadx=46)
        self.c_rows=Entry(self.frm)
        self.c_rows.grid(column=1, row=2,ipady=5, ipadx=46)
        self.c_col=Entry(self.frm)
        self.c_col.grid(column=1, row=1,ipady=5, ipadx=46)

        ttk.Label(self.frm, text="Cantidad de filas por estanteria").grid(column=0, row=3,ipady=5, ipadx=46)
        ttk.Label(self.frm, text="Cantidad de columnas por estanteria").grid(column=0, row=4,ipady=5, ipadx=46)
        self.rows=Entry(self.frm,state='disable')
        self.rows.grid(column=1, row=3,ipady=5, ipadx=46)
        self.col=Entry(self.frm,state='disable')
        self.col.grid(column=1, row=4,ipady=5, ipadx=46)
        ttk.Label(self.frm, text="  ").grid(column=0, row=5,ipady=5, ipadx=46)
        ttk.Button(self.frm, text="Start", command=lambda:self.do_funcion()).grid(column=0, row=6,ipady=5, ipadx=45)
        ttk.Button(self.frm, text="Quit", command=lambda:self.root.destroy()).grid(column=1, row=6,ipady=5, ipadx=46)

    
    def do_bloquear(self):
        if (self.op.get()=="horizontal"):
            self.col.configure(state='normal')
            self.rows.configure(state='disable')
        else:
            self.rows.configure(state='normal')
            self.col.configure(state='disable')

    def do_funcion(self):
        if(self.op.get()=="horizontal"):
            grid=Layout(int(self.c_rows.get()),int(self.c_col.get()),1,int(self.col.get()),2)
        else:
            grid=Layout(int(self.c_rows.get()),int(self.c_col.get()),0,2,int(self.rows.get()))
        grid.fill_mat()
        self.path1=Path(grid)
        self.root.destroy()

 