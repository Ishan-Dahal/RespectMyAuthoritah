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
        self.radius = 10
        #Mouth & Chin
        self.mouth_mid = (760,450)
        self.chin_mid = (760, 425)
        self.doublechin_mid = (760, 422)

        #Touqe
        self.main_part = (760, 620)
        self.touqe_base = (760, 620)
        
        #Touqe Top Furs
        self.big_long_fur = (760, 780)
        self.vertical_fur = (753, 785)
        self.furball_above = (780, 790)
        self.furball_left = (735, 782)
        self.furball_below = (770, 775)
        self.furball_right = (790, 780)
        #Face & Touqe Patches
        self.below_touqe= (760, 620)
        self.tri_right= (955, 620, 960, 650, 985, 620)#x1,y1,x2,y2,x3,y3
        self.tri_left=(565, 620, 560, 650, 535, 620)#x1,y1,x2,y2,x3,y3

        """--------------------------------------------------------------------"""

        #Body and Patches
        self.body = (760, 350)
        self.left_foot = (642.5, 100)
        self.right_foot = (867.5,100)
        self.r_hand = (1040, 320)
        self.l_hand = (500,320)
        
    def setup(self):
        arcade.set_background_color(arcade.color.BLUE_SAPPHIRE)

    def on_draw(self):
        self.clear()
        arcade.draw_lbwh_rectangle_filled(530,100, 450, 200, (166, 47, 13)) #Pants
        arcade.draw_triangle_filled(530,100, 530,220, 500,220,(166, 47, 13)) #Left pant angled patch
        arcade.draw_triangle_filled(980,100, 980,220, 1010,220,(166, 47, 13)) #Right pant angled patch
        arcade.draw_ellipse_filled(*(self.body),600, 420, arcade.color.RED) #Body
        arcade.draw_arc_filled (995, 280, 200, 100, arcade.color.RED, 20, 120, 120) #R_Shirt_patch
        arcade.draw_arc_filled (540, 250, 200, 100, arcade.color.RED, 20, 120, 230) #L_Shirt_patch
        arcade.draw_arc_filled(1080, 300, 300, 100, arcade.color.BLUE_SAPPHIRE, 0, 180, 270) #R_Shirt_Cut
        arcade.draw_lbwh_rectangle_filled(530, 140, 450, 60, (166, 47, 13)) #Pant_Mid_Patch
        arcade.draw_arc_filled(*(self.left_foot), 250, 60, arcade.color. BLACK, 0, 180) #LFoot
        arcade.draw_arc_filled(*(self.right_foot), 250, 60, arcade.color. BLACK, 0, 180)#RFoot
        arcade.draw_arc_filled(608, 190, 200, 50, (166, 47, 13), 0, 180)#shirt shape bottom left
        arcade.draw_triangle_filled(504, 201, 490, 250, 525, 203, arcade.color.RED)#Left pant shirt blend
        arcade.draw_circle_filled(980, 192, 10, (166, 47, 13)) #pant patch smallest
        arcade.draw_arc_filled(900, 200, 160, 10, (166, 47, 13), 0 , 180) #Bottom right shirt blend
        arcade.draw_triangle_filled(1020, 320, 1044, 420, 1070, 320, arcade.color.RED)#right sleeve
        arcade. draw_circle_filled(*(self.r_hand), 50, arcade.color.YELLOW) #right hand
        arcade.draw_ellipse_filled(*(self.l_hand), 108, 100, arcade.color.YELLOW, 60)#left hand
        
        """---------------------------------------------------------------------------------------------------------"""
        arcade.draw_ellipse_filled(*self.head_center, self.head_width, self.head_height, (255, 223, 178))
        arcade.draw_ellipse_filled(*(self.links), self.i_width, self.i_height, arcade.color.WHITE, tilt_angle= -60)
        arcade.draw_ellipse_filled(*(self.rechts), self.i_width, self.i_height, arcade.color.WHITE, tilt_angle= 60)
        arcade.draw_arc_outline(*(self.mouth_mid), 60, 15, arcade.color.BLACK, 0, 180, 10)
        arcade.draw_arc_outline(*(self.chin_mid), 85, 15, arcade.color.BLACK, -180, 0, 5)
        arcade.draw_arc_outline(*(self.doublechin_mid), 160, 35, arcade.color.BLACK, -170, -10, 3.5)
        arcade.draw_circle_filled(*(self.links_ball), self.radius, arcade.color.BLACK)
        arcade.draw_circle_filled(*(self.rechts_ball), self.radius, arcade.color.BLACK)
        arcade.draw_arc_filled(*(self.main_part), self.head_width-15, 320, (0, 194, 216), 0,180)
        arcade.draw_arc_filled(*(self.below_touqe), self.head_width-13.5, 90,(255, 223, 178),0, 180) #patch for face
        arcade.draw_arc_outline(*(self.touqe_base), self.head_width, 105, arcade.color.YELLOW,8,172, 30)
        arcade.draw_ellipse_filled(*(self.big_long_fur), 90, 22, arcade.color.YELLOW)
        arcade.draw_ellipse_filled(*(self.vertical_fur), 40, 30, arcade.color.YELLOW, tilt_angle=-60)
        arcade.draw_circle_filled(*(self.furball_above), 12, arcade.color.YELLOW)
        arcade.draw_circle_filled(*(self.furball_left), 13, arcade.color.YELLOW)
        arcade.draw_circle_filled(*(self.furball_below), 10, arcade.color.YELLOW)
        arcade.draw_circle_filled(*(self.furball_right), 12, arcade.color.YELLOW)
        arcade.draw_triangle_filled(*(self.tri_right), arcade. color. BLUE_SAPPHIRE)
        arcade.draw_triangle_filled(*(self.tri_left), arcade. color. BLUE_SAPPHIRE)
        

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.ESCAPE:
            self.set_fullscreen(False)
    
def main():
    window = Eric()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()