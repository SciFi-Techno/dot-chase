import pyray as pr
import snake
import food

# Initialize window & render
pr.init_window(1200, 800, "Dot Chase")
pr.set_target_fps(60)

# Initialize player / snake
player = snake.Snake(2)

# Initialize multiple dots / food
food_list = list()
for i in range(10):
    food_list.append(food.Food())

# Initialize score & whether game is over
score = 0
game_over = False

# Open window until user clicks ESC
while not pr.window_should_close():

    # Game over when _ time is reached
    if pr.get_time() >= 60:
        game_over = True

    # While game is not over
    if not game_over:
        # Player movements
        if pr.is_key_down(pr.KeyboardKey.KEY_LEFT):
            player.update_position_x("-")
        elif pr.is_key_down(pr.KeyboardKey.KEY_RIGHT):
            player.update_position_x("+")
        elif pr.is_key_down(pr.KeyboardKey.KEY_UP):
            player.update_position_y("-")
        elif pr.is_key_down(pr.KeyboardKey.KEY_DOWN):
            player.update_position_y("+")

        # Check if player collides with any of the dots
        for dot in food_list:
            if pr.check_collision_recs(pr.Rectangle(player.get_position().x, player.get_position().y, player.get_shape().x,
                                                player.get_shape().y),
                                       pr.Rectangle(dot.get_position().x, dot.get_position().y, dot.get_shape().x,
                                                dot.get_shape().y)):
                # Increase player speed & score based on dot type
                if dot.get_type() == 1:
                    player.increase_speed()
                    score += 1
                elif dot.get_type() == 2:
                    player.decrease_speed()
                # Make new dot
                dot.update_position()

        # Prevent player from going beyond borders
        if pr.check_collision_circle_line(pr.Vector2(player.get_position().x, player.get_position().y),
                                          player.get_shape().y // 2.0, pr.Vector2(0, 35),
                                          pr.Vector2(pr.get_screen_width(), 35)):
            player.update_position_y("+")
        elif pr.check_collision_circle_line(pr.Vector2(player.get_position().x, player.get_position().y),
                                          player.get_shape().y // 2.0, pr.Vector2(-12, 35),
                                            pr.Vector2(-12, pr.get_screen_height())):
            player.update_position_x("+")
        elif pr.check_collision_circle_line(pr.Vector2(player.get_position().x, player.get_position().y),
                                            player.get_shape().y // 2.0, pr.Vector2(pr.get_screen_width(), 35),
                                            pr.Vector2(pr.get_screen_width(), pr.get_screen_height())):
            player.update_position_x("-")
        elif pr.check_collision_circle_line(pr.Vector2(player.get_position().x, player.get_position().y),
                                            player.get_shape().y // 2.0, pr.Vector2(0, pr.get_screen_height()),
                                            pr.Vector2(pr.get_screen_width(), pr.get_screen_height())):
            player.update_position_y("-")

    # Draw on canvas & set background color
    pr.begin_drawing()
    pr.clear_background(pr.DARKGRAY)

    # Draw player & dots
    player.draw_shape()
    for dot in food_list:
        dot.draw_shape()

    # Draw upper border
    pr.draw_line_bezier(pr.Vector2(0, 45), pr.Vector2(pr.get_screen_width(), 45), 2, pr.WHITE)

    # Draw score
    pr.draw_text("Score: " + str(score), 10, 10, 25, pr.BLUE)

    # Draw timer as long as time is less than _ seconds
    if pr.get_time() <= 60:
        pr.draw_text("Timer: " + str(int(pr.get_time())) + "s", 140, 10, 25, pr.BLUE)
    # Else draw a pop-up window
    else:
        pr.gui_message_box(pr.Rectangle(pr.get_window_position().x // 2.0, pr.get_window_position().y // 2.0,
                                        300, 300),
                           "Game over", "Your score was " + str(score), "Press 'Esc' to exit")

    pr.end_drawing()

pr.close_window()