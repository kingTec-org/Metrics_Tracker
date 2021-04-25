from pymongo import MongoClient
import urllib.parse
import random

me = urllib.parse.quote_plus('LarryDCJ')
rd = urllib.parse.quote_plus('dismyside42')

client = MongoClient("mongodb+srv://%s:%s@cluster0.nhqsm.mongodb.net/metrics_tracker?retryWrites"
                     "=true&w=majority" % (me, rd), authSource='admin')

db = client.metrics_tracker
flights = db.flights


# get entire flight list from database
def get_flight_query(excluded_fields=['_id', 'crew_on_flight']):
    flight_list = [list(flight.values())
                   for flight in flights.find({}, {f'{excluded_fields[0]}': False, f'{excluded_fields[1]}': False})]
    return flight_list


# get flight columns from db
def get_flight_column_query(excluded_fields=['_id', 'crew_on_flight']):
    column_list = [key.title().replace('_', ' ')
                   for key in flights.find_one({}, {f'{excluded_fields[0]}': False, f'{excluded_fields[1]}': False})]
    return column_list


# find flight via user string
def find_flight(user_input):
    result = db.flights.find({'crew_position': f'{user_input}'})
    return result


# #-----!!CRUD FUNCTIONS!!-----# #


# edit existing flight
def edit_flight():
    # get crew info
    # present crew info
    # allow to be changed
    # mongo update method
    pass


# add flight based on user input
def add_flight(value):
    flight_info = {
        '_id': value[0],
        'flight_number': value[0],
        'aircraft_type': value[1],
        'pilot_in_command': value[2],
        'scheduled_takeoff': value[3],
        'actual_takeoff': value[4],
        'scheduled_land': value[5],
        'actual_land': value[6]
    }
    flights.insert_one(flight_info)


# delete flight
def delete_flight(flight_number):
    flight_id = {'_id': flight_number}
    flights.delete_one(flight_id)


def gen_random_flight():
    takeoff = random.randint(0, 24)

    if takeoff in (range(0, 7)):
        land = takeoff + 18
    else:
        land = takeoff - 6

    if takeoff < 10:
        scheduled_takeoff = f'0{takeoff}00z'
    else:
        scheduled_takeoff = f'{takeoff}00z'

    if land < 10:
        scheduled_land = f'+0{land}00z'
    else:
        scheduled_land = f'{land}00z'

    flight_number = 'IBICF010112020000**Z'
    aircraft_type = random.choice(['KCQ-9', 'MQ-135', 'MC-46', 'KC-1', 'RQ-42'])
    pilot_in_command = ''
    actual_takeoff = ''
    actual_land = ''
    return flight_number, aircraft_type, pilot_in_command, \
           scheduled_takeoff, actual_takeoff, scheduled_land, actual_land
