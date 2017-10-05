import arcade, arcade.key

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

#    def update(self):
#        self.knight.update(0,0)
                
    def draw(self):
        for row in range(len(self.plan_map)):
            for column in range(len(self.plan_map[row])):
                arcade.draw_rectangle_filled(column*self.width+self.width/2+1,row*self.hight+self.hight/2,self.width-1,self.hight-1,arcade.color.BLACK)

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.MOTION_DOWN:
            self.knight.update(0,-1)
        elif key == arcade.key.MOTION_UP:
            self.knight.update(0,1)
        elif key == arcade.key.MOTION_LEFT:
            self.knight.update(-1,0)
        elif key == arcade.key.MOTION_RIGHT:
            self.knight.update(1,0)                
