"""
File: shrink.py
Name:Zoey
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str, the file path of the original image
    :return img: SimpleImage,which is
    """
    original_img = SimpleImage(filename)
    shrink_img = SimpleImage.blank(original_img.width // 2, original_img.height // 2)
    for x in range(original_img.width // 2):
        for y in range(original_img.height // 2):
            shrink_pixel = shrink_img.get_pixel(x, y)
            original_pixel = original_img.get_pixel(x*2, y*2)
            shrink_pixel.red = original_pixel.red
            shrink_pixel.green = original_pixel.green
            shrink_pixel.blue = original_pixel.blue
    return shrink_img


def main():
    """
    The program makes image half the width and height of the original.
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
