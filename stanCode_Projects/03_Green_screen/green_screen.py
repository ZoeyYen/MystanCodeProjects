"""
File: green_screen.py
Name:Zoey
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in "ReyGreenScreen.png".
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img: image, the background image
    :param figure_img: image, the figure image
    :return figure_img: combine background_img and figure_img
    """
    for x in range(figure_img.width):
        for y in range(figure_img.height):
            pixel = figure_img.get_pixel(x, y)
            bigger = max(pixel.red, pixel.blue)  # returns the one that is bigger
            if pixel.green > bigger*2:
                new_pixel = background_img.get_pixel(x, y)
                pixel.red = new_pixel.red
                pixel.green = new_pixel.green
                pixel.blue = new_pixel.blue
    return figure_img


def main():
    """
    To replace the green screen with the background image
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
