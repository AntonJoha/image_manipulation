#!/usr/bin/env python3

import random
from arg import get_args
import pathlib
from PIL import Image


def sort_pixel_height(img):

    c = 0
    for i in range(img.width):
        if c < 0:
            c += 1
            continue
        if random.random() < 0.05 * c:
            c = - random.randint(0,25)
            continue
        c += 1
        values = []
        for j in range(img.height):
            values.append(img.getpixel((i,j)))
        s = sorted(values, key=lambda x: x[2])
        for j in range(img.height):
            img.putpixel((i,j), s[j])
    return img

def sort_pixel(img, height=True):

    if height:
        return sort_pixel_height(img)

    c = 0
    for i in range(img.height):

        if c < 0:
            c += 1
            continue
        if random.random() < 0.05 * c:
            c = - random.randint(0,25)
            continue
        c += 1

        values = []
        if random.random() < 0.5:
            continue
        for j in range(img.width):
            values.append(img.getpixel((j,i)))
        s = sorted(values, key=lambda x: x[0] + x[1] + x[2])
        for j in range(img.width):
            img.putpixel((j,i), s[j])
    return img


a = get_args()

res = a.parse_args()
print(res.image)

with Image.open(res.image) as im:
    print(im.getpixel((0,0)))

    print(im.width)
    print(im.height)
    a = im.copy()
    
    for i in range(10):
        b = sort_pixel(a.copy(), random.random() < 0.5)
        a = Image.blend(a,b, 0.7)
    
    a = Image.blend(im, a, 0.8)
    a.show()
    #im.show()


