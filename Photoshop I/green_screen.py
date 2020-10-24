"""
File: green_screen.py
-------------------------------
This file creates a new image that uses
MillenniumFalcon.png as background and
replace the green pixels in ReyGreenScreen.png
"""

from simpleimage import SimpleImage


def combine(background_img, figure_img):
    """
    :param background_img:
    :param figure_img:
    :return:
    """
    for x in range(background_img.width):
        for y in range(background_img.height):
            pixel_fig = figure_img.get_pixel(x, y)
            bigger = max(pixel_fig.red, pixel_fig.blue)
            if pixel_fig.green > 2*bigger:
                pixel_bg = background_img.get_pixel(x, y)
                pixel_fig.red = pixel_bg.red
                pixel_fig.blue = pixel_bg.blue
                pixel_fig.green = pixel_bg.green
    return figure_img


def main():
    """
    TODO:
    """
    space_ship = SimpleImage("images/MillenniumFalcon.png")
    figure = SimpleImage("images/ReyGreenScreen.png")
    result = combine(space_ship, figure)
    result.show()


if __name__ == '__main__':
    main()
