import pyray as pr
import snake
import food

# Initialize window & render
pr.init_window(700, 700, "game_draft")
pr.set_target_fps(60)

# Initialize player / snake, dot / food, & score
player = snake.Snake(6)
food = food.Food()
score = 0

# Open window until user clicks ESC
while not pr.window_should_close():

    # Player movements
    if pr.is_key_down(pr.KeyboardKey.KEY_LEFT):
        player.update_position_x("-")
    elif pr.is_key_down(pr.KeyboardKey.KEY_RIGHT):
        player.update_position_x("+")
    elif pr.is_key_down(pr.KeyboardKey.KEY_UP):
        player.update_position_y("-")
    elif pr.is_key_down(pr.KeyboardKey.KEY_DOWN):
        player.update_position_y("+")

    # Check if player collides with dot
    # If so, make new dot & increase score by 1
    if pr.check_collision_recs(pr.Rectangle(player.get_position().x, player.get_position().y, player.get_shape().x,
                                            player.get_shape().y),
                               pr.Rectangle(food.get_position().x, food.get_position().y, food.get_shape().x,
                                            food.get_shape().y)):
        food.update_position()
        score += 1

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

    # Draw on canvas
    pr.begin_drawing()
    pr.clear_background(pr.DARKGRAY)

    # Draw player & dot
    player.draw_shape()
    food.draw_shape()

    # Draw upper border
    pr.draw_line_bezier(pr.Vector2(0, 45), pr.Vector2(pr.get_screen_width(), 45), 2, pr.WHITE)

    # Draw score text
    pr.draw_text("Score: " + str(score), 10, 10, 25, pr.BLUE)
    pr.end_drawing()

pr.close_window()