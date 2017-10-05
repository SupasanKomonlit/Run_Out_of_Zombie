import arcade

class Main_Character:
    def __init__(self, world, pos_x, pos_y):
        self.world = world
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.real_x = 1 + self.pos_x*self.world.width + self.world.width/2
        self.real_y = 1 + self.pos_y*self.world.width + self.world.width/2
        self.limit_x = len(self.world.plan_map[0])
        self.limit_y = len(self.world.plan_map)
        print("limit is %i and %i"%(self.limit_x,self.limit_y))

    def update(self, movement_x , movement_y):
        print("move is %i and %i"%(movement_x,movement_y))
        if self.pos_x + movement_x > -1 and self.pos_x + movement_x < self.limit_x:
            self.pos_x += movement_x 
        if self.pos_y + movement_y > -1 and self.pos_y + movement_y < self.limit_y:
            self.pos_y += movement_y
        self.real_x = 1 + self.pos_x*self.world.width + self.world.width/2
        self.real_y = 1 + self.pos_y*self.world.width + self.world.width/2
