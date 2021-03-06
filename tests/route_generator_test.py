#!/usr/local/bin/python
# -*- coding: utf-8 -*-
"""
- LICENCE

The MIT License (MIT)

Copyright (c) 2016 Eleftherios Anagnostopoulos for Ericsson AB (EU FP7 CityPulse Project)

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.


- DESCRIPTION OF DOCUMENTS

-- MongoDB Database Documents:

address_document: {
    '_id', 'name', 'node_id', 'point': {'longitude', 'latitude'}
}
bus_line_document: {
    '_id', 'bus_line_id', 'bus_stops': [{'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}}]
}
bus_stop_document: {
    '_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}
}
bus_stop_waypoints_document: {
    '_id', 'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'waypoints': [[edge_object_id]]
}
bus_vehicle_document: {
    '_id', 'bus_vehicle_id', 'maximum_capacity',
    'routes': [{'starting_datetime', 'ending_datetime', 'timetable_id'}]
}
detailed_bus_stop_waypoints_document: {
    '_id', 'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'waypoints': [[edge_document]]
}
edge_document: {
    '_id', 'starting_node': {'osm_id', 'point': {'longitude', 'latitude'}},
    'ending_node': {'osm_id', 'point': {'longitude', 'latitude'}},
    'max_speed', 'road_type', 'way_id', 'traffic_density'
}
node_document: {
    '_id', 'osm_id', 'tags', 'point': {'longitude', 'latitude'}
}
point_document: {
    '_id', 'osm_id', 'point': {'longitude', 'latitude'}
}
timetable_document: {
    '_id', 'timetable_id', 'bus_line_id', 'bus_vehicle_id',
    'timetable_entries': [{
        'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
        'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
        'departure_datetime', 'arrival_datetime', 'number_of_onboarding_passengers',
        'number_of_deboarding_passengers', 'number_of_current_passengers',
        'route': {
            'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
            'distances_from_starting_node', 'times_from_starting_node',
            'distances_from_previous_node', 'times_from_previous_node'
        }
    }],
    'travel_requests': [{
        '_id', 'client_id', 'bus_line_id',
        'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
        'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
        'departure_datetime', 'arrival_datetime',
        'starting_timetable_entry_index', 'ending_timetable_entry_index'
    }]
}
traffic_event_document: {
    '_id', 'event_id', 'event_type', 'event_level', 'point': {'longitude', 'latitude'}, 'datetime'
}
travel_request_document: {
    '_id', 'client_id', 'bus_line_id',
    'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'departure_datetime', 'arrival_datetime',
    'starting_timetable_entry_index', 'ending_timetable_entry_index'
}
way_document: {
    '_id', 'osm_id', 'tags', 'references'
}

-- Route Generator Responses:

get_route_between_two_bus_stops: {
    'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'route': {
        'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
        'distances_from_starting_node', 'times_from_starting_node',
        'distances_from_previous_node', 'times_from_previous_node'
    }
}
get_route_between_multiple_bus_stops: [{
    'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'route': {
        'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
        'distances_from_starting_node', 'times_from_starting_node',
        'distances_from_previous_node', 'times_from_previous_node'
    }
}]
get_waypoints_between_two_bus_stops: {
    'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'waypoints': [[{
        '_id', 'starting_node': {'osm_id', 'point': {'longitude', 'latitude'}},
        'ending_node': {'osm_id', 'point': {'longitude', 'latitude'}},
        'max_speed', 'road_type', 'way_id', 'traffic_density'
    }]]
}
get_waypoints_between_multiple_bus_stops: [{
    'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    'waypoints': [[{
        '_id', 'starting_node': {'osm_id', 'point': {'longitude', 'latitude'}},
        'ending_node': {'osm_id', 'point': {'longitude', 'latitude'}},
        'max_speed', 'road_type', 'way_id', 'traffic_density'
    }]]
}]
"""
import time
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../'))
from src.common.logger import log
from src.common.parameters import testing_bus_stop_names
from src.route_generator.route_generator_client import get_route_between_two_bus_stops, \
    get_route_between_multiple_bus_stops, get_waypoints_between_two_bus_stops, get_waypoints_between_multiple_bus_stops

__author__ = 'Eleftherios Anagnostopoulos'
__email__ = 'eanagnostopoulos@hotmail.com'
__credits__ = [
    'Azadeh Bararsani (Senior Researcher at Ericsson AB) - email: azadeh.bararsani@ericsson.com'
    'Aneta Vulgarakis Feljan (Senior Researcher at Ericsson AB) - email: aneta.vulgarakis@ericsson.com'
]


def test_get_route_between_two_bus_stops(starting_bus_stop=None, ending_bus_stop=None,
                                         starting_bus_stop_name=None, ending_bus_stop_name=None):
    """
    :param starting_bus_stop: bus_stop_document
    :param ending_bus_stop: bus_stop_document
    :param starting_bus_stop_name: string
    :param ending_bus_stop_name: string
    """
    log(module_name='route_generator_test', log_type='INFO',
        log_message='get_route_between_two_bus_stops: starting')
    start_time = time.time()

    # response = {
    #     'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #     'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #     'route': {
    #         'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
    #         'distances_from_starting_node', 'times_from_starting_node',
    #         'distances_from_previous_node', 'times_from_previous_node'
    #     }
    # }
    response = get_route_between_two_bus_stops(
        starting_bus_stop=starting_bus_stop,
        ending_bus_stop=ending_bus_stop,
        starting_bus_stop_name=starting_bus_stop_name,
        ending_bus_stop_name=ending_bus_stop_name
    )
    starting_bus_stop = response.get('starting_bus_stop')
    ending_bus_stop = response.get('ending_bus_stop')
    route = response.get('route')

    if route is not None:
        total_distance = route.get('total_distance')
        total_time = route.get('total_time')
        node_osm_ids = route.get('node_osm_ids')
        points = route.get('points')
        edges = route.get('edges')
        distances_from_starting_node = route.get('distances_from_starting_node')
        times_from_starting_node = route.get('times_from_starting_node')
        distances_from_previous_node = route.get('distances_from_previous_node')
        times_from_previous_node = route.get('times_from_previous_node')

        output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
                 '\nending_bus_stop: ' + str(ending_bus_stop) + \
                 '\ntotal_distance: ' + str(total_distance) + \
                 '\ntotal_time: ' + str(total_time) + \
                 '\nnode_osm_ids: ' + str(node_osm_ids) + \
                 '\npoints: ' + str(points) + \
                 '\nedges: ' + str(edges) + \
                 '\ndistances_from_starting_node: ' + str(distances_from_starting_node) + \
                 '\ntimes_from_starting_node: ' + str(times_from_starting_node) + \
                 '\ndistances_from_previous_node: ' + str(distances_from_previous_node) + \
                 '\ntimes_from_previous_node: ' + str(times_from_previous_node)

    else:
        output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
                 '\nending_bus_stop: ' + str(ending_bus_stop) + \
                 '\nroute: None'

    print output

    elapsed_time = time.time() - start_time
    time.sleep(0.1)
    log(module_name='route_generator_test', log_type='INFO',
        log_message='test_get_route_between_two_bus_stops: finished - elapsed_time = ' +
                    str(elapsed_time) + ' sec')


def test_get_route_between_multiple_bus_stops(bus_stops=None, bus_stop_names=None):
    """
    :param bus_stops: [bus_stop_document]
    :param bus_stop_names: [string]
    """
    log(module_name='route_generator_test', log_type='INFO',
        log_message='get_route_between_multiple_bus_stops: starting')
    start_time = time.time()

    route_distance = 0
    route_traveling_time = 0

    # response = [{
    #     'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #     'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #     'route': {
    #         'total_distance', 'total_time', 'node_osm_ids', 'points', 'edges',
    #         'distances_from_starting_node', 'times_from_starting_node',
    #         'distances_from_previous_node', 'times_from_previous_node'
    #     }
    # }]
    response = get_route_between_multiple_bus_stops(
        bus_stops=bus_stops,
        bus_stop_names=bus_stop_names
    )
    for intermediate_response in response:
        starting_bus_stop = intermediate_response.get('starting_bus_stop')
        ending_bus_stop = intermediate_response.get('ending_bus_stop')
        intermediate_route = intermediate_response.get('route')

        if intermediate_route is not None:
            total_distance = intermediate_route.get('total_distance')
            route_distance += total_distance
            total_time = intermediate_route.get('total_time')
            route_traveling_time += total_time
            node_osm_ids = intermediate_route.get('node_osm_ids')
            points = intermediate_route.get('points')
            edges = intermediate_route.get('edges')
            distances_from_starting_node = intermediate_route.get('distances_from_starting_node')
            times_from_starting_node = intermediate_route.get('times_from_starting_node')
            distances_from_previous_node = intermediate_route.get('distances_from_previous_node')
            times_from_previous_node = intermediate_route.get('times_from_previous_node')

            output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
                     '\nending_bus_stop: ' + str(ending_bus_stop) + \
                     '\ntotal_distance: ' + str(total_distance) + \
                     '\ntotal_time: ' + str(total_time) + \
                     '\nnode_osm_ids: ' + str(node_osm_ids) + \
                     '\npoints: ' + str(points) + \
                     '\nedges: ' + str(edges) + \
                     '\ndistances_from_starting_node: ' + str(distances_from_starting_node) + \
                     '\ntimes_from_starting_node: ' + str(times_from_starting_node) + \
                     '\ndistances_from_previous_node: ' + str(distances_from_previous_node) + \
                     '\ntimes_from_previous_node: ' + str(times_from_previous_node)
        else:
            output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
                     '\nending_bus_stop: ' + str(ending_bus_stop) + \
                     '\nroute: None'

        print output

    route_average_speed = (route_distance / 1000) / (route_traveling_time / 3600)

    print '\nroute_distance: ' + str(route_distance / 1000) + \
          ' - route_traveling_time: ' + str(route_traveling_time / 60) + \
          ' - route_average_speed: ' + str(route_average_speed)

    elapsed_time = time.time() - start_time
    time.sleep(0.1)
    log(module_name='route_generator_test', log_type='INFO',
        log_message='test_get_route_between_multiple_bus_stops: finished - elapsed_time = ' +
                    str(elapsed_time) + ' sec')


def test_get_waypoints_between_two_bus_stops(starting_bus_stop=None, ending_bus_stop=None,
                                             starting_bus_stop_name=None, ending_bus_stop_name=None):
    """
    :param starting_bus_stop: bus_stop_document
    :param ending_bus_stop: bus_stop_document
    :param starting_bus_stop_name: string
    :param ending_bus_stop_name: string
    """
    log(module_name='route_generator_test', log_type='INFO',
        log_message='test_get_waypoints_between_two_bus_stops: starting')
    start_time = time.time()

    # response = {
    #     'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #     'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #     'waypoints': [[{
    #         '_id', 'starting_node': {'osm_id', 'point': {'longitude', 'latitude'}},
    #         'ending_node': {'osm_id', 'point': {'longitude', 'latitude'}},
    #         'max_speed', 'road_type', 'way_id', 'traffic_density'
    #     }]]
    # }
    response = get_waypoints_between_two_bus_stops(
        starting_bus_stop=starting_bus_stop,
        ending_bus_stop=ending_bus_stop,
        starting_bus_stop_name=starting_bus_stop_name,
        ending_bus_stop_name=ending_bus_stop_name
    )
    starting_bus_stop = response.get('starting_bus_stop')
    ending_bus_stop = response.get('ending_bus_stop')
    waypoints = response.get('waypoints')

    output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
             '\nending_bus_stop: ' + str(ending_bus_stop)
    print output

    for separate_waypoints in waypoints:
        print 'waypoints: ' + str(separate_waypoints)

    elapsed_time = time.time() - start_time
    time.sleep(0.1)
    log(module_name='route_generator_test', log_type='INFO',
        log_message='test_get_waypoints_between_two_bus_stops: finished - elapsed_time = ' +
                    str(elapsed_time) + ' sec')


def test_get_waypoints_between_multiple_bus_stops(bus_stops=None, bus_stop_names=None):
    """
    :param bus_stops: [bus_stop_document]
    :param bus_stop_names: [string]
    """
    log(module_name='route_generator_test', log_type='INFO',
        log_message='test_get_waypoints_between_multiple_bus_stops: starting')
    start_time = time.time()

    # response = [{
    #     'starting_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #     'ending_bus_stop': {'_id', 'osm_id', 'name', 'point': {'longitude', 'latitude'}},
    #     'waypoints': [[{
    #         '_id', 'starting_node': {'osm_id', 'point': {'longitude', 'latitude'}},
    #         'ending_node': {'osm_id', 'point': {'longitude', 'latitude'}},
    #         'max_speed', 'road_type', 'way_id', 'traffic_density'
    #     }]]
    # }]
    response = get_waypoints_between_multiple_bus_stops(
        bus_stops=bus_stops,
        bus_stop_names=bus_stop_names
    )
    for intermediate_response in response:
        starting_bus_stop = intermediate_response.get('starting_bus_stop')
        ending_bus_stop = intermediate_response.get('ending_bus_stop')
        waypoints = intermediate_response.get('waypoints')

        output = '\nstarting_bus_stop: ' + str(starting_bus_stop) + \
                 '\nending_bus_stop: ' + str(ending_bus_stop)
        print output

        for separate_waypoints in waypoints:
            print 'waypoints: ' + str(separate_waypoints)

    elapsed_time = time.time() - start_time
    time.sleep(0.1)
    log(module_name='route_generator_test', log_type='INFO',
        log_message='test_get_waypoints_between_multiple_bus_stops: finished - elapsed_time = ' +
                    str(elapsed_time) + ' sec')


if __name__ == '__main__':
    selection = ''

    while True:
        selection = raw_input(
            '\n0.  exit'
            '\n1.  test_get_route_between_two_bus_stops'
            '\n2.  test_get_route_between_multiple_bus_stops'
            '\n3.  test_get_waypoints_between_two_bus_stops'
            '\n4.  test_get_waypoints_between_multiple_bus_stops'
            '\nSelection: '
        )

        if selection == '0':
            break

        elif selection == '1':
            test_get_route_between_two_bus_stops(
                starting_bus_stop_name=testing_bus_stop_names[0],
                ending_bus_stop_name=testing_bus_stop_names[1]
            )

        elif selection == '2':
            test_get_route_between_multiple_bus_stops(
                bus_stop_names=testing_bus_stop_names
            )

        elif selection == '3':
            test_get_waypoints_between_two_bus_stops(
                starting_bus_stop_name=testing_bus_stop_names[0],
                ending_bus_stop_name=testing_bus_stop_names[1]
            )

        elif selection == '4':
            test_get_waypoints_between_multiple_bus_stops(
                bus_stop_names=testing_bus_stop_names
            )

        else:
            print 'Invalid input'
