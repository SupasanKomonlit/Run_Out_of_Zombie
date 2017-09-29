import arcade
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height

class MapWindow(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        arcade.set_background_color(arcade.color.WHITE)

        self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
    
    def on_draw(self):
        arcade.start_render()

if __name__ == '__main__':
    window = MapWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.set_window(window)
    arcade.run()

    
