import arcade, random

class Main_Character:
    def __init__(self, world, pos_x, pos_y):
        self.world = world
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.real_x = 1 + self.pos_x*self.world.width + self.world.width/2
        self.real_y = 1 + self.pos_y*self.world.hight + self.world.hight/2
        self.limit_x = len(self.world.plan_map[0])
        self.limit_y = len(self.world.plan_map)
        print("limit is %i and %i"%(self.limit_x,self.limit_y))
        self.status = 1
# assign status 1 is alive 2 is winner 3 is die

    def update(self, movement_x , movement_y):
        print("move is %i and %i"%(movement_x,movement_y))
        if self.pos_x + movement_x > -1 and self.pos_x + movement_x < self.limit_x and movement_x != 0:
            self.pos_x += movement_x
            self.check_map() 
        elif self.pos_y + movement_y > -1 and self.pos_y + movement_y < self.limit_y and movement_y != 0:
            self.pos_y += movement_y
            self.check_map() 
        self.real_x = 1 + self.pos_x*self.world.width + self.world.width/2
        self.real_y = 1 + self.pos_y*self.world.hight + self.world.hight/2

    def check_map(self):
        print("Welcome to check_map in Main_Character")
# Check about switch
        if self.world.plan_map[self.pos_y][self.pos_x] > 10:
            print("That is switch")
            self.world.open_or_close(self.world.plan_map[self.pos_y][self.pos_x])
# Check about target
        elif self.world.plan_map[self.pos_y][self.pos_x] == 2:
            print("You win")
            self.status = 2
        for test_key in self.world.trap_keys.keys():
            if self.world.trap_keys[test_key][0] == self.pos_y and self.world.trap_keys[test_key][1] == self.pos_x:
                print("this position have black hole")
                if self.world.trap_keys[test_key][2] == 1:
                    print("you are dead")
                    self.status = 3
                else:
                    None
                break 

class Zombie_Character:
    def __init__(self, world, pos_x, pos_y):
        self.world = world
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.real_x = 1 + self.pos_x*self.world.width + self.world.width/2
        self.real_y = 1 + self.pos_y*self.world.hight + self.world.hight/2
        self.limit_x = len(self.world.plan_map[0])
        self.limit_y = len(self.world.plan_map)
        self.seeing = 0
        self.picture = arcade.Sprite("images/Zombie_01.png")
        self.picture.set_position(self.real_x,self.real_y)
        print("limit is %i and %i"%(self.limit_x,self.limit_y))
        self.status = 1

    def draw(self):
        self.picture.draw()

    def update(self):
        movement_x = 0
        movement_y = 0
        if self.status == 0:
            None
        elif self.seeing == 0:
            while True:
                rand_move = random.randint(1,100)
                if rand_move < 26:
                    movement_x = -1
                elif rand_move < 51:
                    move_y = -1
                elif rand_move < 76:
                    move_x = 1
                else:
                    move_y = 1
                print("move is %i and %i"%(movement_x,movement_y))
                if self.pos_x + movement_x > -1 and self.pos_x + movement_x < self.limit_x and movement_x != 0:
                    self.pos_x += movement_x
                    self.check_map() 
                elif self.pos_y + movement_y > -1 and self.pos_y + movement_y < self.limit_y and movement_y != 0:
                    self.pos_y += movement_y
                    self.check_map()
                else:
                    continue   
                    print("random again") 
                self.real_x = 1 + self.pos_x*self.world.width + self.world.width/2
                self.real_y = 1 + self.pos_y*self.world.hight + self.world.hight/2
                break
        else:
            target_x = self.world.knight.pos_x
            target_y = self.world.knight.pos_y

    def check_map(self):
        print("Welcome to check_map in Zombie_Character")
# Check about switch
        if self.world.plan_map[self.pos_y][self.pos_x] > 10:
            self.world.open_or_close(self.world.plan_map[self.pos_y][self.pos_x])
# Check about target
        for test_key in self.world.trap_keys.keys():
            if self.world.trap_keys[test_key][0] == self.pos_y and self.world.trap_keys[test_key][1] == self.pos_x:
#                print("this position have black hole")
                if self.world.trap_keys[test_key][2] == 1:
#                    print("zombie dead")
                    self.status = 0
                else:
                    None
                break 
