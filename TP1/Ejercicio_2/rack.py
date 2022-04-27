from box import Box

class Rack(Box):
     
    def __init__(self,y:int,x:int,rack:bool, color, product, ay, ax):
        super().__init__(y, x, rack, color)
        self.a_x = ax
        self.a_y = ay
        self.product = product