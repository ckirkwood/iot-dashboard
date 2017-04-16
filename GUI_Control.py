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
