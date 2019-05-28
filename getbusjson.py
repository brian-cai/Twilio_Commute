import requests
from datetime import datetime  
from datetime import timedelta   

def go_beale_st():
    msg = '\nF Line buses headed to Beale Street:\n'
    token = open("token.txt","r")
    try: 
        r = requests.get("https://api.actransit.org/transit/stops/50242/predictions" + token.read())
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        return "Error: " + str(e)
    if not r.ok:
        return "Error " + str(r) + "\nPerhaps the AC Transit API is down"
    return get_predictions(r.json(), msg)

def go_home():
    msg = '\nF Line buses headed to Emeryville:\n'
    token = open("token.txt", "r")
    try:
        r = requests.get("https://api.actransit.org/transit/stops/50747/predictions" + token.read())
    except requests.exceptions.HTTPError as e:
        # Whoops it wasn't a 200
        return "Error: " + str(e)
    if not r.ok:
        return "Error " + str(r) + "\nPerhaps the AC Transit API is down"
    return get_predictions(r.json(), msg)

def get_predictions(allrides, msg):
    count = 1
    for ride in allrides:
        if ride['RouteName'] == 'F':
            msg += "Bus # " + str(count) + "\n"
            count += 1
            msg += "Original Departure: " + ride['PredictedDeparture'][11:] + "\n"
            msg += "Delay: " + str(ride['PredictedDelayInSeconds']/60) +" minutes\n"
            dt = datetime.strptime(ride['PredictedDeparture'], "%Y-%m-%dT%H:%M:%S") + timedelta(seconds = ride['PredictedDelayInSeconds'])
            msg += "Predicted Departure: " + dt.strftime("%H:%M:%S") + "\n"
    print(msg)
    return msg