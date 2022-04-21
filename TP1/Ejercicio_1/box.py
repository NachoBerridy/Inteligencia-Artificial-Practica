from re import X


class Box:

    def __init__(self,x:int,y:int,rack:bool, color):
        self.x = x
        self.y = y

        self.is_rack = rack
        self.is_target = False
        self.is_starting_point = False
        self.is_cargo_bay = False
        self.h=0.0 #Heuristica
        self.g=0 #Costo
        self.f=0.0 #costoTotal
        self.root=(0,0)
        self.color = color

    def set_color(self, color = (255, 255, 255)):
        if self.is_target == True:
            self.color = ((152, 0, 0))
        elif self.is_starting_point == True:
            self.color = ((0, 0, 202))
        else:
            self.color = color
   