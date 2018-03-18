# -*- coding: utf-8 -*-
"""
Created on Sun Mar 18 19:11:23 2018

@author: thinkpad
"""

from deal_with_images.deal_with_images import (cut_image, 
                                               show_images, 
                                               save_images,
                                               )

if __name__ == '__main__':
    image_list = cut_image('beauty.jpg', 2, 2)
    save_images(image_list)
    show_images(image_list, 2, 2).show()