"""
stanCode Breakout Project
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10000 / 120    # 120 frames per second
NUM_LIVES = 3			    # Number of attempts


def main():
    graphics = BreakoutGraphics()
    lives = NUM_LIVES

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
        if graphics.remove_all_brick():                  # Game complete
            break
        if graphics.ball.y >= graphics.window.height:    # lost one life
            lives -= 1
            if lives == 0:
                break               # Game over
            else:
                graphics.reset()    # Restart


if __name__ == '__main__':
    main()
