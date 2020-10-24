"""
File: shrink.py
Name: Ray Chang, 2020.08
-------------------------------
Create a new "out" image half the width and height of the original.
Set pixels at x=0 1 2 3 in out , from x=0 2 4 6 in original,
and likewise in the y direction.
"""

from simpleimage import SimpleImage


def shrink(filename):
    """
    :param filename: str,
    :return img: SimpleImage,
    """
    image = SimpleImage(filename)
    new_img = SimpleImage.blank(image.width // 2, image.height // 2)

    for x in range(image.width):
        for y in range(image.height):
            """
            new_pix should be ((x,y) + (x+1, y) + (x,y+1) + (x+1,y+1))//4
            """
            new_x = (x+x+1+x+x+1)//4
            new_y = (y+y+y+1+y+1)//4
            pix = image.get_pixel(new_x, new_y)
            new_pix = new_img.get_pixel(x//2, y//2)
            new_pix.red = pix.red
            new_pix.green = pix.green
            new_pix.blue = pix.blue
    return new_img


def main():
    """
    TODO:
    """
    original = SimpleImage("images/poppy.png")
    original.show()
    after_shrink = shrink("images/poppy.png")
    after_shrink.show()


if __name__ == '__main__':
    main()
