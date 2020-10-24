"""
File: blur.py
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred img. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors
"""

from simpleimage import SimpleImage


def main():
    """
    TODO:
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


def blur(img):
    """
    :param img:
    :return:
    """
    new_img = SimpleImage.blank(img.width, img.height)

    for x in range(img.width):
        for y in range(img.height):
            red_s = 0
            green_s = 0
            blue_s = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x + i
                    pixel_y = y + j
                    if 0 <= pixel_x <= img.width-1:
                        if 0 <= pixel_y <= img.height-1:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            red_s += pixel.red
                            green_s += pixel.green
                            blue_s += pixel.blue
                            count += 1
            new_pixel = new_img.get_pixel(x, y)
            new_pixel.red = red_s // count
            new_pixel.green = green_s // count
            new_pixel.blue = blue_s // count
    return new_img


if __name__ == '__main__':
    main()
