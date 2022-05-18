"""
File: blur.py
Name:Zoey
-------------------------------
This file shows the original image(smiley-face.png)
first, and then its blurred image. The blur algorithm
uses the average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img:the original image
    :return new_img:the blurred image
    """
    w = img.width
    h = img.height
    new_img = SimpleImage.blank(w, h)
    for x in range(w):
        for y in range(h):
            new_pixel = new_img.get_pixel(x, y)
            pixel_0 = img.get_pixel(x, y)
            if x == 0 and y == 0:  # upper_left corner
                pixel_1 = img.get_pixel(x + 1, y)
                pixel_2 = img.get_pixel(x + 1, y + 1)
                pixel_3 = img.get_pixel(x, y + 1)
                new_pixel.red = (pixel_0.red + pixel_1.red + pixel_2.red + pixel_3.red) // 4
                new_pixel.green = (pixel_0.green + pixel_1.green + pixel_2.green + pixel_3.green) // 4
                new_pixel.blue = (pixel_0.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue) // 4
            elif x == 0 and y == h-1:  # lower_left corner
                pixel_1 = img.get_pixel(x + 1, y)
                pixel_2 = img.get_pixel(x + 1, y - 1)
                pixel_3 = img.get_pixel(x, y - 1)
                new_pixel.red = (pixel_0.red + pixel_1.red + pixel_2.red + pixel_3.red) // 4
                new_pixel.green = (pixel_0.green + pixel_1.green + pixel_2.green + pixel_3.green) // 4
                new_pixel.blue = (pixel_0.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue) // 4
            elif x == w - 1 and y == 0:  # upper_right corner
                pixel_1 = img.get_pixel(x - 1, y)
                pixel_2 = img.get_pixel(x - 1, y + 1)
                pixel_3 = img.get_pixel(x, y+1)
                new_pixel.red = (pixel_0.red + pixel_1.red + pixel_2.red + pixel_3.red) // 4
                new_pixel.green = (pixel_0.green + pixel_1.green + pixel_2.green + pixel_3.green) // 4
                new_pixel.blue = (pixel_0.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue) // 4
            elif x == w - 1 and y == h-1:  # lower_right corner
                pixel_1 = img.get_pixel(x - 1, y)
                pixel_2 = img.get_pixel(x - 1, y - 1)
                pixel_3 = img.get_pixel(x, y - 1)
                new_pixel.red = (pixel_0.red + pixel_1.red + pixel_2.red + pixel_3.red) // 4
                new_pixel.green = (pixel_0.green + pixel_1.green + pixel_2.green + pixel_3.green) // 4
                new_pixel.blue = (pixel_0.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue) // 4
            elif x == 0:  # left side
                pixel_1 = img.get_pixel(x, y - 1)
                pixel_2 = img.get_pixel(x, y + 1)
                pixel_3 = img.get_pixel(x + 1, y - 1)
                pixel_4 = img.get_pixel(x + 1, y)
                pixel_5 = img.get_pixel(x + 1, y - 1)
                new_pixel.red = (pixel_0.red + pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red +
                                 pixel_5.red) // 6
                new_pixel.green = (pixel_0.green + pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green +
                                   pixel_5.green) // 6
                new_pixel.blue = (pixel_0.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue +
                                  pixel_5.blue) // 6
            elif x == w-1:  # right side
                pixel_1 = img.get_pixel(x, y - 1)
                pixel_2 = img.get_pixel(x, y + 1)
                pixel_3 = img.get_pixel(x - 1, y - 1)
                pixel_4 = img.get_pixel(x - 1, y)
                pixel_5 = img.get_pixel(x - 1, y + 1)
                new_pixel.red = (pixel_0.red + pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red +
                                 pixel_5.red) // 6
                new_pixel.green = (pixel_0.green + pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green +
                                   pixel_5.green) // 6
                new_pixel.blue = (pixel_0.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue +
                                  pixel_5.blue) // 6
            elif y == 0:  # Top
                pixel_1 = img.get_pixel(x - 1, y)
                pixel_2 = img.get_pixel(x + 1, y)
                pixel_3 = img.get_pixel(x - 1, y + 1)
                pixel_4 = img.get_pixel(x, y + 1)
                pixel_5 = img.get_pixel(x + 1, y + 1)
                new_pixel.red = (pixel_0.red + pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red +
                                 pixel_5.red) // 6
                new_pixel.green = (pixel_0.green + pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green +
                                   pixel_5.green) // 6
                new_pixel.blue = (pixel_0.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue +
                                  pixel_5.blue) // 6
            elif y == h-1:  # Bottom
                pixel_1 = img.get_pixel(x - 1, y)
                pixel_2 = img.get_pixel(x + 1, y)
                pixel_3 = img.get_pixel(x - 1, y - 1)
                pixel_4 = img.get_pixel(x, y - 1)
                pixel_5 = img.get_pixel(x + 1, y - 1)
                new_pixel.red = (pixel_0.red + pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red +
                                 pixel_5.red) // 6
                new_pixel.green = (pixel_0.green + pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green +
                                   pixel_5.green) // 6
                new_pixel.blue = (pixel_0.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue +
                                  pixel_5.blue) // 6
            else:
                pixel_1 = img.get_pixel(x - 1, y)
                pixel_2 = img.get_pixel(x - 1, y - 1)
                pixel_3 = img.get_pixel(x, y - 1)
                pixel_4 = img.get_pixel(x + 1, y - 1)
                pixel_5 = img.get_pixel(x + 1, y)
                pixel_6 = img.get_pixel(x + 1, y + 1)
                pixel_7 = img.get_pixel(x, y + 1)
                pixel_8 = img.get_pixel(x - 1, y + 1)
                new_pixel.red = (pixel_0.red + pixel_1.red + pixel_2.red + pixel_3.red + pixel_4.red +
                                 pixel_5.red + pixel_6.red + pixel_7.red + pixel_8.red) // 9
                new_pixel.green = (pixel_0.green + pixel_1.green + pixel_2.green + pixel_3.green + pixel_4.green +
                                   pixel_5.green + pixel_6.green + pixel_7.green + pixel_8.green) // 9
                new_pixel.blue = (pixel_0.blue + pixel_1.blue + pixel_2.blue + pixel_3.blue + pixel_4.blue +
                                  pixel_5.blue + pixel_6.blue + pixel_7.blue + pixel_8.blue) // 9
    return new_img


def main():
    """
    This program makes image blurred.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(9):
        blurred_img = blur(blurred_img)
    blurred_img.show()


if __name__ == '__main__':
    main()
