import arcade

from detail_of_map import Map

screen_width = 1000
screen_height = 600


class Game_Window(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

    def on_draw(self):
        arcade.start_render()

if __name__ == '__main__':
    window = Game_Window(screen_width, screen_height)
    arcade.run()
