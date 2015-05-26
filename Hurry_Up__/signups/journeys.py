# -*- coding: utf8 -*-
# Créé par jumelvin, le 22/01/2015 en Python 3.2

import urllib, json, datetime, urllib2

key='b05da061-a7fe-43b1-ba6b-8bf247357d78'

def query_navitia(api_call=''):
    api_call = urllib.quote(api_call,safe='/?=&,')
    url = 'https://api.navitia.io/' + 'v1/coverage/fr-idf' + api_call
    req = urllib2.Request(url)
    req.add_header('Authorization', key)
    r = urllib2.urlopen(req)
    return json.loads(r.read().decode().strip())

def get_journeys():
    transports = query_navitia()

    addresse_depart = query_navitia('/places?q=4, avenue du président Wilson, Saint-Denis')
    addresse_arrivee = query_navitia('/places?q=6 place de la Résistance, Saint-Denis')

    arret_depart = query_navitia('/coords/'+addresse_depart['places'][0]['id']+'/places_nearby')
    arret_arrivee = query_navitia('/coords/'+addresse_arrivee['places'][0]['id']+'/places_nearby')

    date = datetime.datetime.now()

    journey_call = "/journeys?from={resource_id_1}&to={resource_id_2}&datetime={datetime}".format(resource_id_1 = addresse_depart['places'][0]['id'], resource_id_2 = addresse_arrivee['places'][0]['id'], datetime = date.strftime('%Y%m%dT%H%M'))
    journey = query_navitia(journey_call)
    return journey

def get_best_route(journey):
    routes = journey['journeys']
    for route in routes:
        if route['type'] == 'best':
            best_route = route
    return best_route


def poi_departs_arrivees(best_route):
    departs = []
    arrivees = []
    for section in best_route['sections']:
        if section['type'] != 'waiting':
            departs.append(section['geojson']['coordinates'][0])
            arrivees.append(section['geojson']['coordinates'][-1])
    return departs, arrivees


def get_lines(best_route):
    lines = {}
    i = 0
    for section in best_route['sections']:
        i += 1
        line = []
        if section['type'] != 'waiting':
            for coord in section['geojson']['coordinates']:
                line.append([coord[1],coord[0]])
            lines[i] = line
    return lines


def get_poi_departs(departs):
    poi_departs = {}
    poi_num = 0
    for i in departs:
        poi_num += 1
        poi_departs[poi_num] = [i[1],i[0]]
    return poi_departs


journey = get_journeys()
best_route = get_best_route(journey)
departs, arrivees = poi_departs_arrivees(best_route)

print(get_lines(best_route))
