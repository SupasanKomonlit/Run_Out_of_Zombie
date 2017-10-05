import arcade

from detail_of_map import Map

NUM_ROW = 12
NUM_COLUMN = 16

WIDTH = 51
HIGHT = 51

SCREEN_WIDTH = NUM_COLUMN * WIDTH +1
SCREEN_HIGHT = NUM_ROW * HIGHT +1

class Game_Character(arcade.Sprite):
    def __init__(self, *location_of_picture, **character):
        self.knight = character.pop('knight', None)

        super().__init__(*location_of_picture, **character)

    def sync_with_model(self):
        if self.knight:
            self.set_position(self.knight.pos_x, self.knight.pos_y)

    def draw(self):
            self.sync_with_model()
            super().draw()

class Game_Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        self.setup_map= []
        for row in range(NUM_ROW):
            self.setup_map.append([])
            for column in range(NUM_COLUMN):
                self.setup_map[row].append(0)
        print(self.setup_map)

        self.map = Map(SCREEN_WIDTH,SCREEN_HIGHT,WIDTH,HIGHT,self.setup_map)
        self.knight_sprite = Game_Character('images/Knight.png',knight=self.map.knight)

    def on_draw(self):
        arcade.start_render()
        self.map.draw()
        self.knight_sprite.draw()

if __name__ == '__main__':
    window = Game_Window(SCREEN_WIDTH, SCREEN_HIGHT)
    arcade.run()
