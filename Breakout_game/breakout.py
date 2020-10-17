"""
Name: Ray Chang, 2020, 09
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics
from breakout_extention import Breakout_Extention


FRAME_RATE = 1000 / 120 # 120 frames per second.
NUM_LIVES = 3


def main():
    graphics = BreakoutGraphics()
    live = NUM_LIVES
    score = graphics.scores

    # Add animation loop here!
    while True:

        pause(FRAME_RATE)
        if graphics.ball.y + graphics.ball.height >= graphics.window.height:
            live -= 1
            if live > 0:
                graphics.reset_ball()
            else:
                graphics.gameover()
                break

        dx = graphics.get_vx()
        dy = graphics.get_vy()
        graphics.ball.move(dx, dy)
        graphics.sensor()
        # graphics.box_sensor()
        # graphics.drop_a_gift()
        # graphics.box.move(0,5)
        graphics.end()

        if score == 3:
            graphics.window.add()

        if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
            graphics.reverse_vx()
        if graphics.ball.y <= 0:
            graphics.reverse_vy()


if __name__ == '__main__':
    main()
