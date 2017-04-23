## Add physical buttons to a connected home system - buttons hit the API endpoints covered in Pimoroni's Mote/Homekit tutorial

################################################################################    
#    Copyright (C) 2017 Callum Kirkwood                                        #
#                                                                              #
#    This program is free software: you can redistribute it and/or modify      #
#    it under the terms of the GNU General Public License as published by      #
#    the Free Software Foundation, either version 3 of the License, or         #
#    (at your option) any later version.                                       #
#                                                                              #
#    This program is distributed in the hope that it will be useful,           #
#    but WITHOUT ANY WARRANTY; without even the implied warranty of            #
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the             #
#    GNU General Public License for more details.                              #
#                                                                              #
#    You should have received a copy of the GNU General Public License         #
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     #
################################################################################

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
