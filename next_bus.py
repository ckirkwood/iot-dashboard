## Post the next bus from your local stop to Dweet.io, to be retreived by Freeboard.io

import requests, json, dweepy, time

while True:
## Query Transport API database, create dictionary from the output
## Replace ATCO-CODE (unique bus stop identifier), APP-ID and APP-KEY with your own details
    j = requests.get('https://transportapi.com/v3/uk/bus/stop/ATCO-CODE/live.json?app_id=APP-ID&app_key=APP-KEY&group=route&nextbuses=yes').json()
    d = json.dumps(j)
    data = json.loads(d)

## Check to see if values for each service are present before pushing data to Dweet.io
    if '33' in data.get('departures') != True:
        Line_33 = data['departures']['33'][0]['aimed_departure_time']
        time.sleep(0.5)
        dweepy.dweet_for('33Bus', {'time': Line_33})
    else:
    	dweepy.dweet_for('33Bus', {'time': 'No busses'})

    if '63' in data.get('departures') != True:
        Line_63 = data['departures']['63'][0]['aimed_departure_time']
	time.sleep(0.5)
        dweepy.dweet_for('63Bus', {'time': Line_63})
    else:
	dweepy.dweet_for('63Bus', {'time': 'No busses'})
        time.sleep(300)

