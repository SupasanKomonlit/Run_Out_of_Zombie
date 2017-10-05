import arcade, arcade.key, random

from detail_of_characters import Main_Character

class Map:
    def __init__(self, SCREEN_WIDTH, SCREEN_HIGHT, WIDTH, HIGHT, array_map ):
        self.plan_map = array_map
        self.width = WIDTH
        self.hight = HIGHT
        self.widths = SCREEN_WIDTH
        self.hights = SCREEN_HIGHT
        self.knight = Main_Character(self, 0, 0)
        print("len(self.plan_map) is %i"%(len(self.plan_map)))
        print("len(self.plan_map[0]) is %i"%(len(self.plan_map[0])))
        self.plan_map[0][0] = 1
        self.plan_map[len(self.plan_map)-1][len(self.plan_map[0])-1] = 2
        print("self.plan_map")
        print(self.plan_map)
                
    def draw_grid(self):
        for row in range(len(self.plan_map)):
            for column in range(len(self.plan_map[row])):
                arcade.draw_rectangle_filled(column*self.width+self.width/2+1,row*self.hight+self.hight/2,self.width-1,self.hight-1,arcade.color.BLACK)
                if row == len(self.plan_map)-1 and column == len(self.plan_map[row])-1:
                    arcade.draw_rectangle_filled(column*self.width+self.width/2+1,row*self.hight+self.hight/2,self.width-1,self.hight-1,arcade.color.GREEN)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.MOTION_DOWN:
            self.knight.update(0,-1)
        elif key == arcade.key.MOTION_UP:
            self.knight.update(0,1)
        elif key == arcade.key.MOTION_LEFT:
            self.knight.update(-1,0)
        elif key == arcade.key.MOTION_RIGHT:
            self.knight.update(1,0)                

    def random_position_trap(array_map,number):
        limit_y = len(array_map) - 1
        limit_x = len(array_map[0]) -1 
        while True:
            switch_x = random.randint(0,limit_x)
            switch_y = random.randint(0,limit_y)
            if(array_map[switch_x][switch_y] == 0):
                None
            else:
                continue
            trap_x = random.randint(0,limit_x)
            trap_y = random.randint(0,limit_y)
            if(array_map[trap_x][trap_y] == 0):
                None
            else:
                continue
            return switch_x, switch_y, trap_x, trap_y
