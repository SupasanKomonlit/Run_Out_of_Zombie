import arcade, arcade.key#, time

from detail_of_map import Map
from detail_of_board import Board

NUM_ROW = 12
NUM_COLUMN = 16

WIDTH = 51
HIGHT = 51
SCREEN_BOARD = 400
SCREEN_WIDTH = NUM_COLUMN * WIDTH +1 +SCREEN_BOARD 
SCREEN_HIGHT = NUM_ROW * HIGHT +1
SCREEN_MAP = NUM_COLUMN * WIDTH + 1

if NUM_COLUMN*NUM_ROW >=50:
    NUM_TRAP = NUM_ROW*NUM_COLUMN*20//100
    NUM_TRAP += NUM_TRAP%6
else:
    NUM_TRAP = NUM_ROW*NUM_COLUMN*5//100

NUM_WALL = NUM_ROW*NUM_COLUMN*25//100

NUM_ZOMBIE = NUM_ROW*NUM_COLUMN*8//100
#NUM_ZOMBIE = 2 
class Game_Character(arcade.Sprite):
    def __init__(self, *location_of_picture, **character):
        self.knight = character.pop('knight', None)
#        self.zombie = character.pop('zombie',None)
        super().__init__(*location_of_picture, **character)

    def sync_with_model(self):
        if self.knight:
            self.set_position(self.knight.real_x, self.knight.real_y)
#        elif self.zombie:
#            self.set_position(self.zombie.real_x, self.zombie.real_y)

    def draw(self):
        self.sync_with_model()
        super().draw()

class Game_Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)
        self.current_state = "game_running"
        self.setup_map= []
        for row in range(NUM_ROW):
            self.setup_map.append([])
            for column in range(NUM_COLUMN):
                self.setup_map[row].append(0)

        self.map = Map(SCREEN_WIDTH,SCREEN_HIGHT,WIDTH,HIGHT,self.setup_map,NUM_TRAP,NUM_ZOMBIE,NUM_WALL,SCREEN_MAP+10)
#        self.zombie_sprite = []
        self.knight_sprite = Game_Character('images/Knight.png',knight=self.map.knight)
#        for count in range(NUM_ZOMBIE):
#            self.zombie_sprite.append(Game_Character('images/Zombie_01.png',zombie=self.map.zombie)) 
                        
            
    def update(self, data):
#        print("Update_in_Game_Window")
        if self.map.knight.status == 2:
            self.current_state = "you_win"
        elif self.map.knight.status == 3 :
            print("Dead by Black Hole")
            self.current_state = "you_lose"
        elif self.map.knight.status == 4 :
            print("Dead by Zombie")
            self.current_state = "you_lose"

    def draw_win_game(self):
        output = "Congraturation!!!"
        size = 60
        delete_length = len(output)//2.5*size
        arcade.draw_text(output, SCREEN_WIDTH/2 - delete_length, SCREEN_HIGHT/2, arcade.color.RED, size)
        output = "You Win"
        arcade.draw_text(output, SCREEN_WIDTH/3, SCREEN_HIGHT/2- (3*size/2), arcade.color.RED, 60)

    def draw_lose_game(self):
        output = "Game Over!!!"
        size = 60
        delete_length = len(output)/2.5*size
        arcade.draw_text(output, SCREEN_WIDTH/2 - delete_length, SCREEN_HIGHT/2, arcade.color.RED, size)
        output = "You Lose"
        delete_length = len(output)/2.5*size
        arcade.draw_text(output, SCREEN_WIDTH/2- delete_length, SCREEN_HIGHT/2-(1.5*size), arcade.color.RED, 60)
        if self.map.knight.status == 3:
            output = "Dead by Black Hole "
            size = 40
            delete_length = len(output)/2.5*size
            arcade.draw_text(output, SCREEN_WIDTH/2 - delete_length, SCREEN_HIGHT/2 - (3.5*size), arcade.color.RED, size)
        elif self.map.knight.status == 4:
            output = "Dead by Zombie "
            size = 40
            delete_length = len(output)//2.5*size
            arcade.draw_text(output, SCREEN_WIDTH/2 - delete_length, SCREEN_HIGHT/2 - (3.5*size), arcade.color.RED, size)

    def on_draw(self):
        arcade.start_render()
        if self.current_state == "game_running":
            self.map.draw_grid()
            self.map.draw_wall()
            self.knight_sprite.draw()
            self.map.draw_trap()
            self.map.draw_zombie()
#            for count in range(NUM_ZOMBIE):
#                self.map.zombie[count].draw()
            self.map.set_up = 0
            self.map.board.standard_draw()
            self.map.board.event_draw()
        elif self.current_state == "you_win":
            self.draw_win_game()
        elif self.current_state == "you_lose":
            self.draw_lose_game()

    def on_key_press(self, key, key_modifiers):
        self.map.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = Game_Window(SCREEN_WIDTH, SCREEN_HIGHT)
    arcade.run()
