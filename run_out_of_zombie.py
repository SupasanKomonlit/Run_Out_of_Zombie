import arcade, arcade.key

from detail_of_map import Map

NUM_ROW = 12
NUM_COLUMN = 16

WIDTH = 51
HIGHT = 51

SCREEN_WIDTH = NUM_COLUMN * WIDTH +1
SCREEN_HIGHT = NUM_ROW * HIGHT +1

NUM_TRAP = NUM_ROW*NUM_COLUMN*50//100

class Game_Character(arcade.Sprite):
    def __init__(self, *location_of_picture, **character):
        self.knight = character.pop('knight', None)
        super().__init__(*location_of_picture, **character)

    def sync_with_model(self):
        if self.knight:
            self.set_position(self.knight.real_x, self.knight.real_y)

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

        self.map = Map(SCREEN_WIDTH,SCREEN_HIGHT,WIDTH,HIGHT,self.setup_map,NUM_TRAP)
        self.knight_sprite = Game_Character('images/Knight.png',knight=self.map.knight)

    def update(self, data):
#        print("Update_in_Game_Window")
        if self.map.knight.status == 2:
            self.current_state = "you_win"

    def draw_win_game(self):
        output = "Congraturation!!!"
        arcade.draw_text(output, SCREEN_WIDTH/8, SCREEN_HIGHT/2, arcade.color.RED, 60)
        output = "You Win"
        arcade.draw_text(output, SCREEN_WIDTH/3, SCREEN_HIGHT/2-80, arcade.color.RED, 60)

    def on_draw(self):
        arcade.start_render()
        if self.current_state == "game_running":
            self.map.draw_grid()
            self.knight_sprite.draw()
            self.map.draw_trap()
        elif self.current_state == "you_win":
            self.draw_win_game()

    def on_key_press(self, key, key_modifiers):
        self.map.on_key_press(key, key_modifiers)

if __name__ == '__main__':
    window = Game_Window(SCREEN_WIDTH, SCREEN_HIGHT)
    arcade.run()
