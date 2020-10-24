"""
File: mirror_lake.py
Name: Ray Chang, 2020.08
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing the inverse image of
mt-rainier.jpg below the original one
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename:
    :return:
    """
    img = SimpleImage(filename)
    new_img = SimpleImage.blank(img.width, img.height*2)

    for x in range(img.width):
        for y in range(img.height):
            pixel_img = img.get_pixel(x, y)
            pixel_new_img1 = new_img.get_pixel(x, y)
            pixel_new_img2 = new_img.get_pixel(x, new_img.height-y-1)
            pixel_new_img1.red = pixel_img.red
            pixel_new_img1.green = pixel_img.green
            pixel_new_img1.blue = pixel_img.blue
            pixel_new_img2.red = pixel_img.red
            pixel_new_img2.green = pixel_img.green
            pixel_new_img2.blue = pixel_img.blue
    return new_img


def main():
    """
    TODO:
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


if __name__ == '__main__':
    main()
