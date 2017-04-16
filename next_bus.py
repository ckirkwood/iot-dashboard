import requests, json, dweepy, time

while True:
    r = requests.get('https://transportapi.com/v3/uk/bus/stop/1800NB04841/live.json?app_id=391561b5&app_key=0e3179907ec6f4ea2ca0a1f0b1c82c3f&group=route&nextbuses=yes')
    j = r.json()
#    dweepy.dweet_for('63Bus', {'time': Line_63})
#    time.sleep(0.5)
    Line_33 = j['departures'][u'33'][0][u'aimed_departure_time']
    time.sleep(0.5)
    dweepy.dweet_for('33Bus', {'time': Line_33})
    time.sleep(600)


