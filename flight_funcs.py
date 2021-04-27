from pymongo import MongoClient
import urllib.parse
import random
from crew_funcs import *

me = urllib.parse.quote_plus('LarryDCJ')
rd = urllib.parse.quote_plus('dismyside42')

client = MongoClient("mongodb+srv://%s:%s@cluster0.nhqsm.mongodb.net/metrics_tracker?retryWrites"
                     "=true&w=majority" % (me, rd), authSource='admin')

db = client.metrics_tracker
flights = db.flights

# retrieve single flight
def get_single_flight():
    flight = [list(flight.values()) for flight in flights.find_one()]
    print(flight)


# get entire flight list from database
def get_flight_query(excluded_fields=None):
    if excluded_fields is None:
        flight_list = [list(flight.values()) for flight in flights.find()]
    else:
        excluded_fields_pass = dict.fromkeys(excluded_fields, False)
        flight_list = [list(flight.values()) for flight in flights.find({}, excluded_fields_pass)]
    return flight_list

# get flight columns from db
def get_flight_column_query(excluded_fields=None):
    if excluded_fields is None:
        column_list = [key.title().replace('_', ' ') for key in flights.find_one()]
    else:
        excluded_fields_pass = dict.fromkeys(excluded_fields, False)
        column_list = [key.title().replace('_', ' ') for key in flights.find_one({}, excluded_fields_pass)]

    return column_list

# find flight via user string
def find_flight(user_input):
    result = db.flights.find({'crew_position': f'{user_input}'})
    return result

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
        'crew_on_flight': [],
        'pilot_in_command': '',
        'scheduled_takeoff': value[2],
        'scheduled_land': value[3]
    }
    try:
        flights.insert_one(flight_info)
    except:
        print('try again')

# delete flight
def delete_flight(flight_number):
    flight_id = {'_id': flight_number}
    flights.delete_one(flight_id)

# generates a random flight when added
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

    flight_number = f'SOSD{random.randint(10000,100000)}LEET'
    aircraft_type = random.choice(['KCQ-9', 'MQ-135', 'MC-46', 'KC-1', 'RQ-42'])

    return flight_number, aircraft_type, scheduled_takeoff, scheduled_land

def add_crew_to_flight(flight_number, employee_id):
    flights.update({'flight_number': flight_number}, {'$push': {'crew_on_flight': employee_id}})


def remove_crew_from_flight(flight_number, employee_id):
    flights.update({'flight_number': flight_number}, {'$pull': {'crew_on_flight': employee_id}})

def get_crew_from_flight(excluded_fields=None):
    employee_ids = flights.distinct('crew_on_flight')

    if excluded_fields is None:
        crew_list = [crews.find_one({'employee_id': employee_id}) for employee_id in employee_ids]
    else:
        excluded_fields_pass = dict.fromkeys(excluded_fields, False)
        crew_list = [list(crews.find_one({'employee_id': employee_id}, excluded_fields_pass).values()) for employee_id in employee_ids]
    for crew in crew_list:
        print(crew)

    return crew_list
