## Adds physical buttons to a connected home system - buttons hit the API endpoints covered in Pimoroni's Mote/Homekit tutorial

from gpiozero import Button
import time
import urllib

on_button = Button(26)
off_button = Button(20)

while True:
    if on_button.is_pressed == True:
	req = urllib.urlopen('http://192.168.1.104:5000/blinkt/api/v1.0/on')
	time.sleep(0.3)	
    elif off_button.is_pressed == True:
	req = urllib.urlopen('http://192.168.1.104:5000/blinkt/api/v1.0/off')
	time.sleep(0.3)
