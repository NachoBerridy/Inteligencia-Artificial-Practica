class Box:

    def __init__(self,x:int,y:int,rack:bool):
        self.x = x
        self.y = y
        self.is_rack = rack
        self.h:float #Heuristica
        self.g:float #Costo
    
    def heuristic(self):
        pass

    def cost(self):
        pass