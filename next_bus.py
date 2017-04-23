## Post the next bus from your local stop to Dweet.io, to be retreived by Freeboard.io

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

