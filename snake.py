import pyray as pr

class Snake:
    def __init__(self, speed):
        self.position = pr.Vector2(pr.get_screen_width() // 2.0, pr.get_screen_height() // 2.0)
        self.shape = pr.Vector2(20, 20)
        self.speed = speed

    def draw_shape(self):
        pr.draw_rectangle_v(self.position, self.shape, pr.GOLD)

    def get_position(self):
        return self.position

    def get_shape(self):
        return self.shape

    def update_position_x(self, operator):
        if operator == '+':
            self.position.x += self.speed
        elif operator == '-':
            self.position.x -= self.speed

    def update_position_y(self, operator):
        if operator == '+':
            self.position.y += self.speed
        elif operator == '-':
            self.position.y -= self.speed

    def increase_speed(self):
        self.speed += 1

    def decrease_speed(self):
        self.speed -= 2