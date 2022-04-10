from re import X


class Box:

    def __init__(self,rack:bool):
        self.is_rack = rack
        self.h:float #Heuristica
        self.g=0 #Costo
        self.f:float #costoTotal
        self.root=(0,0)
    
