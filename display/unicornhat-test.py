#!/usr/bin/env python

# Quick test of unicorn hat hd as a feedback display using 16x16 px png files

import signal
import time
from sys import exit

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

try:
    import unicornhathd as unicorn
    print("16x16 unicorn detected")
except ImportError:
    from unicorn_hat_sim import unicornhathd as unicorn


print("""Unicorn HAT HD: lofi feedback display prototype

Based on Pimoroni's show-png.py example for the unicorn hat hd

Licensed under Creative Commons Attribution-Noncommercial-Share Alike 3.0
Unported License.

Press Ctrl+C to exit!

""")

unicorn.rotation(270)
unicorn.brightness(0.5)

width, height = unicorn.get_shape()

def icon(image):
    try:
        for o_x in range(int(image.size[0] / width)):
            for o_y in range(int(image.size[1] / height)):
                valid = False
                for x in range(width):
                    for y in range(height):
                        pixel = image.getpixel(((o_x * width) + y, (o_y * height) + x))
                        r, g, b = int(pixel[0]), int(pixel[1]), int(pixel[2])
                        if r or g or b:
                            valid = True
                        unicorn.set_pixel(x, y, r, g, b)
                if valid:
                    unicorn.show()
                    time.sleep(2)
    except KeyboardInterrupt:
        unicorn.off()

while True:
    img = Image.open('iot-dashboard/display/hi.png')
    icon(img)
    img = Image.open('iot-dashboard/display/tick.png')
    icon(img)
    img = Image.open('iot-dashboard/display/cross.png')
    icon(img)
