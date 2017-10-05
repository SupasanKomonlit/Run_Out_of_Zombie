import arcade

class Map:
    def __init__(self, width_screen, height_screen, width_grid, height_grid):
        self.width = width_screen
        self.height = height_screen
        self.width_grid = width_grid
        self.height_grid = height_grid
        self.grid = []
        for row in range(20):
            self.grid.append([])
            for column in range(12):
                self.grid[row].append(0)

#    def update(self, delta):

    def draw(self):
        for row in range(12):
            for column in range(20):
                x = column * (self.width_grid ) + self.width_grid//2
                y = row * (self.height_grid ) + self.height_grid//2

                arcade.draw_rectangle_filled(x, y,self.width_grid, self.height_grid, arcade.color.BLACK)

#    def on_key_press(self, key, key_modifiers):
#        if key == arcade.key.SPACE:
#            self.ship.switch_direction()
