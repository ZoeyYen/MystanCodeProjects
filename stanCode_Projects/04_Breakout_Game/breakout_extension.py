"""
stanCode Breakout Project
"""

from campy.gui.events.timer import pause
from breakoutgraphics_extension import BreakoutGraphics

FRAME_RATE = 10000 / 400    # 120 frames per second
NUM_LIVES = 3			    # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES
    graphics.live_board(lives)

    # Add animation loop here!
    while True:
        # pause
        pause(FRAME_RATE)
        # update
        dx = graphics.get_dx()
        dy = graphics.get_dy()
        graphics.ball.move(dx, dy)
        # check
        graphics.check_window()
        graphics.check_obj()
        if graphics.remove_all_brick():                      # Game complete
            break
        if graphics.ball.y >= graphics.window.height:
            if graphics.dead():                             # lost one life
                lives -= 1
                graphics.word(lives)
                graphics.live_board(lives)
                # Game over
                if lives == 0:
                    break
                # restart
                else:
                    graphics.reset()


if __name__ == '__main__':
    main()
