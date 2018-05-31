import requests

from datetime import date
from datetime import datetime
from datetime import timezone
from datetime import timedelta

url = 'https://maps.googleapis.com/maps/api/directions/json?'
api_key = 'YOUR API KEY'

class Error(Exception):
    pass

class WrongAddress(Error):
    pass

def request_direction():
    origin=input("Where from: ").replace(' ', "+")
    destination = input("Where to: ").replace(' ', "+")
    travel_mode = input("Travel mode, please enter 'driving', 'transit', 'bicycling' or 'walking': ")
    nav_request = "origin={0}&destination={1}&mode={3}&key={2}".format(origin, destination, api_key, travel_mode)
    request = url + nav_request  
    response = requests.get(request)
    return response 

def arrival_time():
    duration = int(data['routes'][0]['legs'][0]['duration']['value']) 
    time_now = datetime.now()
    arrival_time = time_now + (timedelta(seconds = duration))
    return "<b>ARRIVAL TIME:</b> {0}".format(datetime.strftime(arrival_time, "%H:%M:%S"))

while True:  
    try:
        data = request_direction().json()
        if data['status'] == 'OK': 
            legs = data['routes'][0]['legs'][0]
            break
        elif data['status'] != 'OK':
            raise WrongAddress(data['status'])
    except WrongAddress:
        print("Directions not found. Try again!")
        request_direction()

with open("directions.html", "w") as file:

    file.write('<br>')
    file.write("<b>START ADDRESS:</b> {0}".format(data['routes'][0]['legs'][0]['start_address']))
    file.write('<br>')
    file.write("<b>END ADDRESS:</b> {0}".format(data['routes'][0]['legs'][0]['end_address']))
    file.write('<br>')
    file.write("<b>TOTAL DURATION:</b> {0}".format(data['routes'][0]['legs'][0]['duration']['text']))
    file.write('<br>')
    file.write(str(arrival_time()))
    file.write('<br>')
    file.write('<br>')
    file.write("<b>DIRECTIONS</b>")
   
    
    integer_distance = 0
    integer_duration = 0
    integer_instructions = 0
 
    distance = legs['steps'][integer_distance]['distance']['text']
    duration = legs['steps'][integer_duration]['duration']['text']
    instructions = legs['steps'][integer_instructions]['html_instructions']
    
    while integer_distance < len(data['routes'][0]['legs'][0]['steps'])and integer_instructions < len(data['routes'][0]['legs'][0]['steps']) and integer_duration < len(data['routes'][0]['legs'][0]['steps']):
        distance = legs['steps'][integer_distance]['distance']['text']
        duration = legs['steps'][integer_duration]['duration']['text']
        instructions = legs['steps'][integer_instructions]['html_instructions']
        file.write('<br>')
        file.write("---------------------")
        file.write('<br>')
        file.write("{0}".format(instructions))
        file.write('<br>')
        file.write("Distance: {0}".format(distance))
        file.write('<br>')
        file.write("Durations: {0}".format(duration))
    
        integer_duration+=1
        integer_distance+=1
        integer_instructions+=1

    file.write('<br>')
    file.write("---------------------")

with open("directions.html", "r") as file: 
    for line in file:
        output = line.split('<br>')
        for line in output:
            print(line)