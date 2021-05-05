from crew_funcs import *
from upconn import *

db = client.metrics_tracker
flights = db.flights


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

    flight_number = f'SOSD{random.randint(10000, 100000)}LEET'
    aircraft_type = random.choice(['KCQ-9', 'MQ-135', 'MC-46', 'KC-1', 'RQ-42'])

    return flight_number, aircraft_type, scheduled_takeoff, scheduled_land


def get_flight_query():
    flight_list = [list(flight.values()) for flight in flights.find()]
    return flight_list

def get_flight_column_query():
    column_list = [key.title().replace('_', ' ') for key in flights.find_one()]
    return column_list

def edit_flight():
    # get crew info
    # present crew info
    # allow to be changed
    # mongo update method
    pass


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


def delete_flight(flight_number):
    flight_id = {'_id': flight_number}
    flights.delete_one(flight_id)


def add_crew_to_flight(flight_number, employee_id):
    flights.update({'flight_number': flight_number}, {'$push': {'crew_on_flight': employee_id}})


def remove_crew_from_flight(flight_number, employee_id):
    flights.update({'flight_number': flight_number}, {'$pull': {'crew_on_flight': employee_id}})


def get_crew_from_flight(flight_number, excluded_fields=None):
    employee_ids = flights.distinct('crew_on_flight', {'flight_number': flight_number})
    crew_list = [crews.find_one({'employee_id': employee_id}) for employee_id in employee_ids]

    if not crew_list:
        crew_list = [['' for row in range(1) for col in range(6)]]
    else:
        pass

    return crew_list
