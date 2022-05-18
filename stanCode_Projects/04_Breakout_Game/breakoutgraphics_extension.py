"""
stanCode Breakout Project
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved
import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 8         # Number of rows of bricks.
BRICK_COLS = 8        # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 10    # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space
        window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=window_width, height=window_height, title=title)

        # Create a paddle
        self.paddle = GRect(paddle_width, paddle_height, x=(window_width-paddle_width)/2,
                            y=window_height-paddle_offset-paddle_height)
        self.paddle.filled = True
        self.window.add(self.paddle)

        # Center a filled ball in the graphical window
        self.__ball_initial_x = window_width / 2 - ball_radius        # initial x of ball
        self.__ball_initial_y = window_height / 2 - ball_radius       # initial y if ball
        self.ball = GOval(ball_radius*2, ball_radius*2)
        self.ball.filled = True

        # Default initial velocity for the ball
        self._dx = 0
        self._dy = 0

        # Initialize our mouse listeners
        onmousemoved(self.paddle_move)      # move paddle
        self.__click_start = 0
        onmouseclicked(self.start_game)     # click to start game

        # Draw bricks
        self.__total_brick = brick_rows * brick_cols     # total number of brick
        for i in range(brick_rows):
            for j in range(brick_cols):
                self.brick = GRect(brick_width, brick_height, x=j*(brick_width+brick_spacing),
                                   y=brick_offset+i*(brick_height+brick_spacing))
                self.brick.filled = True
                if i // 2 % 7 == 0:
                    self.brick.fill_color = 'red'
                elif i // 2 % 7 == 1:
                    self.brick.fill_color = 'orange'
                elif i // 2 % 7 == 2:
                    self.brick.fill_color = 'yellow'
                elif i // 2 % 7 == 3:
                    self.brick.fill_color = 'green'
                elif i // 2 % 7 == 4:
                    self.brick.fill_color = 'blue'
                elif i // 2 % 7 == 5:
                    self.brick.fill_color = 'indigo'
                else:
                    self.brick.fill_color = 'purple'
                self.window.add(self.brick)

        # Create Game label
        self.__word = GLabel("Click to start game!")
        self.__word.font = 'Verdana-13-bold'
        self.window.add(self.__word, x=(self.window.width - self.__word.width) / 2,
                        y=(self.window.height + self.__word.height) / 2)

        # Scoreboard
        self.__score = 0
        self.__score_label = GLabel('Score: '+str(self.__score))
        self.__score_label.font = 'Verdana-13-bold'
        self.window.add(self.__score_label, x=5, y=self.window.height-5)

        # Create lives label
        self.lives_label = GLabel("")
        self.lives_label.font = '-15'
        self.lives_label.color = 'firebrick'
        self.window.add(self.lives_label, x=self.window.width - self.lives_label.width - 5, y=self.window.height - 5)

        # if dead or not
        self.__is_dead = False

    # Getter
    def get_dx(self):
        return self._dx

    # Getter
    def get_dy(self):
        return self._dy

    # move paddle by the mouse
    def paddle_move(self, mouse):
        if mouse.x <= self.paddle.width/2:
            self.paddle.x = 0
        elif mouse.x >= self.window.width-self.paddle.width/2:
            self.paddle.x = self.window.width-self.paddle.width
        else:
            self.paddle.x = mouse.x - self.paddle.width/2

    # click to start game
    def start_game(self, mouse):
        """
        1st click to remove word and add ball;
        2nd click to set ball velocity
        set ball x velocity to random negative or positive
        set ball y velocity to INITIAL_Y_SPEED
        """
        self.__click_start += 1
        # 1st click
        if self.__click_start == 1:
            self.window.remove(self.__word)
            self.window.add(self.ball, self.__ball_initial_x, self.__ball_initial_y)
            self.__is_dead = False
        # 2nd click
        elif self.__click_start == 2:
            self._dx = random.randint(1, MAX_X_SPEED)
            if random.random() > 0.5:
                self._dx *= -1
            self._dy = INITIAL_Y_SPEED

    # reset game
    def reset(self):
        self.__click_start = 0
        self._dx = 0
        self._dy = 0

    # update dx and dy when ball hits the wall
    def check_window(self):
        if self.ball.x <= 0 or self.ball.x + self.ball.width >= self.window.width:
            self._dx *= -1
        if self.ball.y <= 0:
            self._dy *= -1

    # check if ball hits object
    def check_obj(self):
        if self.ball.y < self.paddle.y:
            is_check = True                        # to check object or not
            for i in range(0, 2):
                for j in range(0, 2):
                    if is_check:                   # if True, check object
                        obj_x = self.ball.x + i * self.ball.width
                        obj_y = self.ball.y + j * self.ball.height
                        obj = self.window.get_object_at(obj_x, obj_y)
                        if obj is not None:
                            self.ball_hit_obj(obj)
                            is_check = False

    def ball_hit_obj(self, obj):
        # ball hits paddle
        if self.paddle == obj and self._dy > 0:
            self._dy *= -1
        # ball hits brick
        elif self.paddle != obj:
            self._dy *= -1
            self.window.remove(obj)
            self.__total_brick -= 1
            self.__score += 10
            self.__score_label.text = 'Score: '+str(self.__score)

    # Game complete when remove all bricks
    def remove_all_brick(self):
        if self.__total_brick == 0:
            win_label = GLabel("You Win!")
            win_label.font = 'Verdana-13-bold'
            self.window.add(win_label, x=(self.window.width - win_label.width) / 2,
                            y=(self.window.height + win_label.height) / 2)
            return True

    def word(self, n):
        """
        :param n: the remaining lives
        add different label base on the remaining lives
        """
        if n >= 2:
            self.__word.text = "ReStart!"
        elif n == 1:
            self.__word.text = "Last Chance!"
        else:
            self.__word.text = "Game Over"
        self.window.add(self.__word, x=(self.window.width - self.__word.width) / 2,
                        y=(self.window.height + self.__word.height) / 2)

    # if dead or not
    def dead(self):
        if not self.__is_dead:
            self.__is_dead = True
            return True

    # update lives board
    def live_board(self, n):
        lives = chr(10084)
        self.lives_label.text = lives*n
        self.window.add(self.lives_label, x=self.window.width - self.lives_label.width - 5,
                        y=self.window.height - 5)
