import datetime
import json
import threading
import time
import requests


import readRoute

INTERVAL = 1
SERVER = "docker.dev.delifteducation.be"
PORT = '8100'
UR = 'fhttp://{SERVER}:{PORT}/positions/'
URL = 'http://docker.dev.delifteducation.be:8100/positions/'

def send_location(participation_id, latitude, longitude, distance_walked, deviation):
    now = datetime.datetime.now()
    print(f"{now} at lon: {longitude}, lat: {latitude} with distance {distance_walked}")
    position = {}
    position["time"] = now.isoformat()
    position["longitude"] = longitude
    position["latitude"] = latitude
    position["deviation"] = deviation
    position["distance"] = distance_walked
    position["participation"] = participation_id
    # request_body = json.dumps(position)
    # print(request_body)
    response = requests.post(URL, json=position)
    print(response)

def mock_participant(participation_id, speed):
    # speed in km/h
    segments = readRoute.get_segments("route.json")
    speed_in_ISO = speed / (60*60) * 1000.0# omzetting van km/h naar naar meter per seconde
    distance_per_interval = speed_in_ISO * INTERVAL
    distance_walked = 0.0
    while distance_walked < 101 * 1000:
        # zoek segment waar we nu op zitten. Dit is het eerste segment waar beginAfstand groter of gelijk aan de afgelegde afstand is.
        for segment in segments:
            if not "lengte" in segment:
                continue # skip zero length segments
            if segment["beginafstand"] >= distance_walked:
                deel_van_segment = distance_walked - segment["beginafstand"]
                fractie_van_segment = deel_van_segment/(segment["lengte"])
                latitude_begin = segment["coordinate1"]['latitude']
                latitude_eind = segment["coordinate2"]['latitude']
                latitude = latitude_begin + (latitude_eind - latitude_begin) * fractie_van_segment
                longitude_begin = segment["coordinate1"]['longitude']
                longitude_eind = segment["coordinate2"]['longitude']
                longitude = longitude_begin + (longitude_eind - longitude_begin) * fractie_van_segment
                send_location(participation_id, latitude, longitude, distance_walked, 0.0)
                break
        time.sleep(INTERVAL)
        distance_walked = distance_walked + distance_per_interval




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # mock_participant(4, 5)
    p2 = threading.Thread(target=mock_participant, args=(2, 50.0))
    p2.start()
    p3 = threading.Thread(target=mock_participant, args=(3, 50.5))
    p3.start()
    p4 = threading.Thread(target=mock_participant, args=(4, 51.0))
    p4.start()
    p5 = threading.Thread(target=mock_participant, args=(5, 48.2))
    p5.start()
