# -*- coding: utf-8 -*-
from PIL import Image


def crop_image(file_path):
    image = Image.open(file_path)
    new_image = image.crop((100, 150, 400, 400))
    return new_image


if __name__ == '__main__':
    file_path = 'beauty.jpg'
    crop_image(file_path).show()
    