import arcade

from detail_of_map import Map

NUM_ROW = 12
NUM_COLUMN = 16

WIDTH = 51
HIGHT = 51

SCREEN_WIDTH = NUM_COLUMN * WIDTH
SCREEN_HIGHT = NUM_ROW * HIGHT


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


    def on_draw(self):
        arcade.start_render()
        self.map.draw()

if __name__ == '__main__':
    window = Game_Window(SCREEN_WIDTH, SCREEN_HIGHT)
    arcade.run()
