# Won't run on MacOS
# Credit - https://www.calazan.com/how-to-continuously-monitor-your-wi-fis-signal-strength-in-ubuntu/

import subprocess
import time
import argparse
import signal
import unicornhathd
from sys import exit

try:
    from PIL import Image
except ImportError:
    exit("This script requires the pillow module\nInstall with: sudo pip install pillow")

parser = argparse.ArgumentParser(description='Display WLAN signal strength.')
parser.add_argument(dest='interface', nargs='?', default='wlan0',
                    help='wlan interface (default: wlan0)')
args = parser.parse_args()

print '\n---Press CTRL+Z or CTRL+C to stop.---\n'

unicornhathd.rotation(90)
unicornhathd.brightness(0.5)

width, height = unicornhathd.get_shape()


def icon(img):
    img = Image.open(img)
    while True:
        for o_x in range(int(img.size[0]/width)):
            for o_y in range(int(img.size[1]/height)):
                valid = False
                for x in range(width):
                    for y in range(height):
                        pixel = img.getpixel(((o_x*width)+y,(o_y*height)+x))
                        r, g, b = int(pixel[0]),int(pixel[1]),int(pixel[2])
                        if r or g or b:
                            valid = True
                            unicornhathd.set_pixel(x, y, r, g, b)
                            if valid:
                                unicornhathd.show()


try:
    while True:
        cmd = subprocess.Popen('iwconfig %s' % args.interface, shell=True, stdout=subprocess.PIPE)
        for line in cmd.stdout:
            if 'Link Quality' in line:
                icon('tick.png')
                continue
            elif 'Not-Associated' in line:
                icon('cross.png')
                continue
            time.sleep(1)

except KeyboardInterrupt:
    unicornhathd.off()

