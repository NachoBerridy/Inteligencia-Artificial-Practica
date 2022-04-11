from re import X


class Box:

    def __init__(self,x:int,y:int,rack:bool):
        self.x = x
        self.y = y

        self.is_rack = rack
        self.is_target = False
        self.is_starting_point = False
        self.h=0.0 #Heuristica
        self.g=0 #Costo
        self.f=0.0 #costoTotal
        self.root=(0,0)
    
