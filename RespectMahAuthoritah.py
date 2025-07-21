import arcade

class Eric(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "Arcade Template", fullscreen= True)
        self.head_center = (760, 575)
        self.head_height = 350
        self.head_width = 400
        self.links = (730,575)
        self.rechts = (805,575)
        self.i_width = 90
        self.i_height = 70
    def setup(self):
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)

    def on_draw(self):
        self.clear()
        arcade.draw_ellipse_filled(*self.head_center, self.head_width, self.head_height, (255, 223, 178))
        arcade.draw_ellipse_filled(*(self.links), self.i_width, self.i_height, arcade.color.WHITE, tilt_angle= -60)
        arcade.draw_ellipse_filled(*(self.rechts), self.i_width, self.i_height, arcade.color.WHITE, tilt_angle= 60)
    
    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.set_fullscreen(False)
    
def main():
    window = Eric()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()