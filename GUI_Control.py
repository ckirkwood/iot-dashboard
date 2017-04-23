    Copyright (C) 2017 Callum Kirkwood

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from guizero import App, Text, PushButton
import requests
import json

app = App("Blinkt Control", layout="grid")

def blinkt_on():
    r = requests.get('http://192.168.1.104:5000/blinkt/api/v1.0/on')
def blinkt_off():
    r = requests.get('http://192.168.1.104:5000/blinkt/api/v1.0/off')
            

Text(app, "Blinkt", grid=[2,2])
PushButton(app, command=blinkt_on, text="On", grid=[2, 3])
PushButton(app, command=blinkt_off, text="Off", grid=[2, 4])


app.display()
