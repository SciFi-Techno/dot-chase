import pyray as pr

class Food:
    def __init__(self):
        self.position = pr.Vector2(pr.get_random_value(0, pr.get_screen_width()),
                                   pr.get_random_value(47, pr.get_screen_height()))
        self.shape = pr.Vector2(15, 15)

    def draw_shape(self):
        pr.draw_rectangle_v(self.position, self.shape, pr.RED)

    def get_position(self):
        return self.position

    def get_shape(self):
        return self.shape

    def update_position(self):
        self.position = pr.Vector2(pr.get_random_value(0, pr.get_screen_width()),
                                   pr.get_random_value(47, pr.get_screen_height()))