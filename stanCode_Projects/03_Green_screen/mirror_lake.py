"""
File: mirror_lake.py
Name:Zoey
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return reflect_img: mirror the original image
    """
    img = SimpleImage(filename)
    reflect_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            original = img.get_pixel(x, y)
            # Blank Pixel 1
            reflect_1 = reflect_img.get_pixel(x, y)
            # Fill Pixel 1
            reflect_1.red = original.red
            reflect_1.green = original.green
            reflect_1.blue = original.blue
            # Blank Pixel 2
            reflect_2 = reflect_img.get_pixel(x, reflect_img.height-1-y)
            # Fill Pixel 2
            reflect_2.red = original.red
            reflect_2.green = original.green
            reflect_2.blue = original.blue
    return reflect_img


def main():
    """
    This program creates a mirror image below the original one.
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
