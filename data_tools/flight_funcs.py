from random import randint

from data_tools.crew_funcs import *
from data_tools.upconn import *

db = client.metrics_tracker
flights = db.flights


def gen_random_flight():
    def random_date(start):
        return start + timedelta(days=randint(0, int((datetime.now()-start).days)),
                                 hours=randint(0, 23))

    d1 = datetime.strptime('1/1/2018 0000', '%m/%d/%Y %H%M')

    scheduled_takeoff = random_date(d1)
    scheduled_land = scheduled_takeoff + timedelta(hours=18)

    aircraft_type = random.choice(['KCMQ-9', 'KCMQ-10', 'KCMQ-46', 'KCMQ-135'])

    flight_number = f'ST{scheduled_takeoff.hour}{scheduled_land.hour}{aircraft_type.replace("-", "")}'

    return flight_number, aircraft_type, scheduled_takeoff, scheduled_land

def get_flight_query(*query):
    flight_list = [list(flight.values()) for flight in flights.find({}, *query)]

    return flight_list


def get_flight_column_query(*query):
    column_list = [key.title().replace('_', ' ') for key in flights.find_one({}, *query)]
    return column_list


def edit_flight():
    # get crew info
    # present crew info
    # allow to be changed
    # mongo update method
    pass


def add_flight(value):
    flight_info = {
        'flight_number': value[0],
        'aircraft_type': value[1],
        'crew_on_flight': value[2],
        'pilot_in_command': value[3],
        'scheduled_takeoff': value[4],
        'scheduled_land': value[5]
    }
    print(value[4], value[5])
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
