# -*- coding: utf-8 -*-
"""
Created on Sat Dec 15 10:47:32 2018

@author: owner
"""

class Product:
    def __init__(self, name, quality):
        self.name = name
        self.quality = quality


def recalculate_quality(product):
    if product.name == "potato":
        product.quality = product.quality - 0.5
    elif product.name == "cheese":
        product.quality = product.quality - 2
    else:
        if product.quality < 5:
            product.quality -= 3