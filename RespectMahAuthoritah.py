import arcade

class Eric(arcade.Window):
    def __init__(self):
        super().__init__(1280, 720, "Respect Mah Authoritahhhh", fullscreen= True)
        #Head
        self.head_center = (760, 575)
        self.head_height = 350
        self.head_width = 400

        #Eye
        self.links = (720,575)
        self.rechts = (795,575)
        self.i_width = 90
        self.i_height = 70

        #Eyeballs
        self.links_ball = (733, 575)
        self.rechts_ball = (783,575)

        #Mouth & Chin
        self.mouth_mid = (760,450)
        self.chin_mid = (760, 425)
        self.doublechin_mid = (760, 422)
        self.radius = 10
    def setup(self):
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)

    def on_draw(self):
        self.clear()
        arcade.draw_ellipse_filled(*self.head_center, self.head_width, self.head_height, (255, 223, 178))
        arcade.draw_ellipse_filled(*(self.links), self.i_width, self.i_height, arcade.color.WHITE, tilt_angle= -60)
        arcade.draw_ellipse_filled(*(self.rechts), self.i_width, self.i_height, arcade.color.WHITE, tilt_angle= 60)
        arcade.draw_arc_outline(*(self.mouth_mid), 60, 15, arcade.color.BLACK, 0, 180, 10)
        arcade.draw_arc_outline(*(self.chin_mid), 85, 15, arcade.color.BLACK, -180, 0, 5)
        arcade.draw_arc_outline(*(self.doublechin_mid), 160, 35, arcade.color.BLACK, -170, -10, 3.5)
        arcade.draw_circle_filled(*(self.links_ball), self.radius, arcade.color.BLACK)
        arcade.draw_circle_filled(*(self.rechts_ball), self.radius, arcade.color.BLACK)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.set_fullscreen(False)
    
def main():
    window = Eric()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()