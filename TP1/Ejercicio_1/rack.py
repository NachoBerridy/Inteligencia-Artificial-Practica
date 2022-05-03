from box import Box

class Rack(Box):
     
    def __init__(self,x:int,y:int,rack:bool, color, ay, ax):
        super().__init__(x, y, rack, color)
        self.a_x = ax
        self.a_y = ay