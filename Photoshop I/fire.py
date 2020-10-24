"""
File: fire.py
Name: Ray Chang, 2020,08
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation
"""

from simpleimage import SimpleImage

HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename:
    :return:
    """
    img = SimpleImage(filename)
    for pixel in img:
        avg = (pixel.red+pixel.green+pixel.blue)/3
        fire = avg * HURDLE_FACTOR
        if pixel.red > fire:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.green = avg
    return img


def main():
    """
    TODO:
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


if __name__ == '__main__':
    main()
