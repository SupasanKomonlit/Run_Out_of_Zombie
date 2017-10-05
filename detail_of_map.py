class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height

#    def update(self, delta):

    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.SPACE:
            self.ship.switch_direction()
