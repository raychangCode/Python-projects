"""
Name: Ray Chang, 2020, 09
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman, 
and Jerry Liao

YOUR DESCRIPTION HERE
"""
from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GOval, GRect, GLabel
from campy.gui.events.mouse import onmouseclicked, onmousemoved


import random

BRICK_SPACING = 5      # Space between bricks (in pixels). This space is used for horizontal and vertical spacing.
BRICK_WIDTH = 40       # Height of a brick (in pixels).
BRICK_HEIGHT = 15      # Height of a brick (in pixels).
BRICK_ROWS = 10         # Number of rows of bricks.
BRICK_COLS = 10         # Number of columns of bricks.
BRICK_OFFSET = 50      # Vertical offset of the topmost brick from the window top (in pixels).
BALL_RADIUS = 10       # Radius of the ball (in pixels).
PADDLE_WIDTH = 75      # Width of the paddle (in pixels).
PADDLE_HEIGHT = 15     # Height of the paddle (in pixels).
PADDLE_OFFSET = 50     # Vertical offset of the paddle from the window bottom (in pixels).

INITIAL_Y_SPEED = 7.0  # Initial vertical speed for the ball.
MAX_X_SPEED = 5        # Maximum initial horizontal speed for the ball.


class BreakoutGraphics:

    def __init__(self, ball_radius=BALL_RADIUS, paddle_width=PADDLE_WIDTH,
                 paddle_height=PADDLE_HEIGHT, paddle_offset=PADDLE_OFFSET,
                 brick_rows=BRICK_ROWS, brick_cols=BRICK_COLS,
                 brick_width=BRICK_WIDTH, brick_height=BRICK_HEIGHT,
                 brick_offset=BRICK_OFFSET, brick_spacing=BRICK_SPACING,
                 title='Breakout'):

        # Create a graphical window, with some extra space.
        self.window_width = brick_cols * (brick_width + brick_spacing) - brick_spacing
        self.window_height = brick_offset + 3 * (brick_rows * (brick_height + brick_spacing) - brick_spacing)
        self.window = GWindow(width=self.window_width, height=self.window_height, title=title)

        # Create a gift
        self.box = GRect(brick_width/2, brick_height/2)
        self.box.filled = True
        self.box.fill_color = 'red'

        # Create a paddle.
        self.paddle = GRect(paddle_width, paddle_height,
                            x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset)
        self.window.add(self.paddle)

        self.paddle_new = GRect(paddle_width*5, paddle_height,
                                x=(self.window_width-paddle_width)/2, y=self.window_height-paddle_offset)

        # Center a filled ball in the graphical window.
        self.ball = GOval(ball_radius*2, ball_radius*2,
                          x=(self.window_width-ball_radius)/2, y=(self.window_height-ball_radius)/2)
        self.window.add(self.ball)

        # Default initial velocity for the ball.
        self.ball.filled = True
        self.ball.fill_color = 'navy'
        self.__dx = 0
        self.__dy = 0

        # Initialize our mouse listeners.
        onmouseclicked(self.start)
        onmousemoved(self.control_paddle)

        # Draw bricks.
        for i in range(brick_cols+1):
            for j in range(brick_rows):
                self.brick = GRect(brick_width, brick_height, x=i*(brick_width+brick_spacing),
                                   y=j*(brick_height+brick_spacing) + brick_offset)
                self.brick.filled = True
                self.window.add(self.brick)
                if j % 4 == 1:
                    self.brick.fill_color = 'black'
                elif j % 4 == 2:
                    self.brick.fill_color = 'grey'
                elif j % 4 == 3:
                    self.brick.fill_color = 'lightgrey'
                else:
                    self.brick.fill_color = 'white'

        self.total_bricks = brick_rows * brick_cols
        self.scores = 0
        # Draw Score
        self.score_board = GLabel('Scores: ' + str(self.scores))
        self.score_board.font = '-15'
        self.window.add(self.score_board, x=0, y=self.window.height)

    def control_paddle(self, event):
        if event.x + (self.paddle.width/2) >= self.window.width:
            self.paddle.x = self.window.width - self.paddle.width
        elif event.x - (self.paddle.width/2) <= 0:
            self.paddle.x = 0
        else:
            self.paddle.x = event.x - (self.paddle.width/2)

    def set_ball_velocity(self):
        self.__dx = random.randint(0, MAX_X_SPEED)
        self.__dy = INITIAL_Y_SPEED
        # 一半的機率讓球往左跑
        if random.random() > 0.5:
            self.__dx = -self.__dx

    def get_vx(self):
        return self.__dx

    def get_vy(self):
        return self.__dy

    def reverse_vx(self):
        self.__dx = -self.__dx

    def reverse_vy(self):
        self.__dy = -self.__dy

    def start(self, event):
        if self.__dx != 0:
            pass
        else:
            self.set_ball_velocity()

    def reset_ball(self):
        """
        put ball to the init position
        """
        self.ball.x = (self.window_width-self.ball.width*2)/2
        self.ball.y = (self.window_height - self.ball.width * 2) / 2
        self.__dx = 0
        self.__dy = 0

    def reset_vx(self):
        """
        increase vx a little bit when collision happens
        """
        self.__dx = - (self.__dx + random.random())

    def reset_vy(self):
        """
        increase vy a little bit when collision happens
        """
        self.__dy = - (self.__dy + random.random())

    def sensor(self):
        """
        add checkpoint to detect collision
        """
        sensor1 = self.window.get_object_at(self.ball.x, self.ball.y)
        sensor2 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y)
        sensor3 = self.window.get_object_at(self.ball.x, self.ball.y + self.ball.width)
        sensor4 = self.window.get_object_at(self.ball.x + self.ball.width, self.ball.y + self.ball.width)
        if sensor1 is None and sensor2 is None and sensor3 is None and sensor4 is None:
            pass
        else:
            if sensor1 is self.paddle or sensor2 is self.paddle or sensor3 is self.paddle or sensor4 is self.paddle:
                self.ball.y = self.paddle.y - self.ball.height
                self.reset_vy()
            elif sensor1 is (self.score_board or self.box) or sensor2 is self.score_board or sensor3 is self.score_board \
                    or sensor4 is self.score_board:
                pass
            else:
                if sensor1 is not None:
                    self.reset_vy()
                    self.window.remove(sensor1)
                    self.scores += 1
                elif sensor2 is not None:
                    self.reset_vy()
                    self.window.remove(sensor2)
                    self.scores += 1
                elif sensor3 is not None:
                    self.reset_vy()
                    self.window.remove(sensor3)
                    self.scores += 1
                elif sensor4 is not None:
                    self.reset_vy()
                    self.window.remove(sensor4)
                    self.scores += 1

            self.score_board.text = 'Scores: ' + str(self.scores)

    def box_sensor(self):

        sensor1 = self.window.get_object_at(self.box.x, self.box.y + self.box.width)
        sensor2 = self.window.get_object_at(self.box.x + self.box.width, self.box.y + self.box.width)
        if sensor1 is None and sensor2 is None:
            pass
        else:
            if sensor1 is self.paddle or sensor2 is self.paddle:
                self.window.remove(self.box)
                self.window.remove(sensor1)
                self.window.remove(sensor2)
                self.paddle = self.paddle_new
                self.window.add(self.paddle)

    def drop_a_gift(self):
        if self.scores % 5 == 1:
            self.window.add(self.box, x=self.window.width/2, y=0)

    def end(self):
        """
        stop the animation when all bricks are gone
        """
        if self.scores == self.total_bricks:
            self.reset_ball()
            self.gameover()

    def gameover(self):
        over = GLabel('Game Over!')
        over.font = '-50'
        over.color = 'red'
        self.window.add(over, x=(self.window.width-over.width)/2, y=self.window.height/2)
        self.window.remove(self.ball)
