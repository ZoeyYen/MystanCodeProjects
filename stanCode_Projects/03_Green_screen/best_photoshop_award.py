"""
File: best_photoshop_award.py
----------------------------------
This file creates a photoshopped image
that is going to compete for the Best
Photoshop Award for SC001.
Please put all the images you will use in the image_contest folder
and make sure to choose the right folder when loading your images.
"""

from simpleimage import SimpleImage


# Controls the threshold of detecting white screen pixel
THRESHOLD = 0.7


def main():
    """
    To replace the background
    """
    img = SimpleImage("image_contest/dog1.jpg")
    img.show()
    travel = SimpleImage("image_contest/japan.jpg")
    travel.make_as_big_as(img)
    new_img = combine(img, travel)
    new_img.show()


def combine(img, travel):
    for x in range(img.width):
        for y in range(img.height):
            pixel = img.get_pixel(x, y)
            avg = (pixel.red + pixel.green+pixel.blue)//3
            if avg > 255 * THRESHOLD:
                new_pixel = travel.get_pixel(x, y)
                pixel.red = new_pixel.red
                pixel.green = new_pixel.green
                pixel.blue = new_pixel.blue
    return img


if __name__ == '__main__':
    main()
