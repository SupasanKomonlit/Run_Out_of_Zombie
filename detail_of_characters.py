import arcade

class Main_Character:
    def __init__(self, world, pos_x, pos_y):
        self.world = world
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.limit_x = len(self.world.plan_map[0])
        self.limit_y = len(self.world.plan_map)

    def update(self, movement_x , movement_y):
        if self.pos_x + movement_x > -1 and self.pos_x + movement_x < self.limit_x:
            self.pos_x += movement_x 
        if self.pos_y + movement_y > -1 and self.pos_y + movement_y < self.limit_y:
            self.pos_y += movement_y
