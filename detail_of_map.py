import arcade, arcade.key, random

from detail_of_characters import Main_Character

def random_position_trap(array_map):
    limit_y = len(array_map) - 1
    limit_x = len(array_map[0]) -1 
    print("limit_x : {} limit_y : {}".format(limit_x,limit_y))
    while True:
        switch_x = random.randint(0,limit_x)
        switch_y = random.randint(0,limit_y)
        print("switch_x : {} switch_y : {}".format(switch_x,switch_y))
        if(array_map[switch_y][switch_x] == 0):
            None
        else:
            continue
        trap_x = random.randint(0,limit_x)
        trap_y = random.randint(0,limit_y)
        print("trap_x : {} trap_y : {}".format(trap_x,trap_y))
        if(array_map[trap_y][trap_x] == 0):
            None
        else:
            continue
        return switch_x, switch_y, trap_x, trap_y

def print_map(text,array_map):
    print(text)
    row = len(array_map) - 1
    while row > -1:
        for column in range(len(array_map[row])):
            print("{:>5.0f}".format(array_map[row][column]), end = " ")
        print()
        row -= 1


#value in map 1 : start  2 : finish 3 : zombie >10 : trap
class Map:

    def __init__(self, SCREEN_WIDTH, SCREEN_HIGHT, WIDTH, HIGHT, array_map , NUM_TRAP):
        self.plan_map = array_map
        self.width = WIDTH
        self.hight = HIGHT
        self.widths = SCREEN_WIDTH
        self.hights = SCREEN_HIGHT
        self.knight = Main_Character(self, 0, 0)
        self.num_trap = NUM_TRAP
        print("len(self.plan_map) is %i"%(len(self.plan_map)))
        print("len(self.plan_map[0]) is %i"%(len(self.plan_map[0])))
        self.plan_map[0][0] = 1
        self.plan_map[len(self.plan_map)-1][len(self.plan_map[0])-1] = 2
        print_map("Print set up map",self.plan_map) # check map
        self.trap_keys = {}
        for count in range(self.num_trap):
            print("count is {}".format(count))
            data = random_position_trap(self.plan_map)
            self.plan_map[data[1]][data[0]] = count+10
            self.trap_keys[count+10] = [data[3],data[2],0]
        print_map("Print set up map after add trap",self.plan_map) # check map
        print(self.trap_keys) # 0 is row 1 is column 3 has two value 0 close 1 open

                
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
