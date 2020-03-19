# -*- coding: utf-8 -*-
import requests

class Route:
    
    def __init__(self, origin, destination, distance):
        self.origin = origin
        self.destination = destination
        self.distance = distance
        
    def __str__(self):
        return '\n\nThe distance between {} and {} is {}'.format(self.origin, self.destination, self.distance)


def build_url(parameters):

    url = 'https://maps.googleapis.com/maps/api/distancematrix/json?'
    api_key = ''

    for key, value in parameters.items():
        url += '{}={}&'.format(key, value)
        
    url += 'key={}'.format(api_key)
    
    return url


def format_address(address):
    return '{}+{}+{}'.format(address[1], address[0], address[2])


def get_route(origin, destination):
    
    parameters = {}
    
    parameters['origins'] = format_address(origin)
    parameters['destinations'] = format_address(destination)
    
    json_response = requests.get(build_url(parameters)).json()
    
    distance = json_response.get('rows')[0].get('elements')[0].get('distance').get('text')
    
    route = Route(json_response.get('origin_addresses')[0], json_response.get('destination_addresses')[0], distance) 
    
    return route
    
    
def main():
    
    origin = input('Which is your starting point (Format: Street, Number, Place)?').split(',')
    destination = input('Which is your destination point (Format: Street, Number, Place)?').split(',')
    
    route = get_route(origin, destination)
    
    print(route)
    

if __name__ == '__main__':
    main()
    